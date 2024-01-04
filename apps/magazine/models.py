import os
from io import BytesIO

from django.db import models
from django.core.files.base import ContentFile
from django.conf import settings

import fitz  # PyMuPDF
from PIL import Image

class Magazine(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    pdf = models.FileField(upload_to='pdfs', verbose_name="PDF файл")

    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журналы"

    def __str__(self):
        return self.title

    def get_images(self):
        """
        Извлекает изображения со страниц PDF и сохраняет их в формате WEBP.
        Возвращает список путей к сохраненным изображениям.
        """
        if not self.pdf:
            return []  # Если PDF нет, то и изображений быть не может

        pdf = fitz.open(self.pdf.path)
        image_paths = []

        for page_num in range(len(pdf)):
            page = pdf[page_num]
            pix = page.get_pixmap()

            # Конвертируем Pix в PIL Image
            img_data = BytesIO(pix.tobytes("ppm"))
            img = Image.open(img_data)

            img_io = BytesIO()
            # Сохраняем изображение в формате WEBP с определённым уровнем качества
            img.save(img_io, format="WEBP", quality=80)  # Меняйте значение quality для управления сжатием
            img_content = ContentFile(img_io.getvalue())

            # Формируем путь к изображению
            filename = f'magazine_{self.id}_page_{page_num + 1}.webp'
            webp_path = os.path.join(settings.MEDIA_ROOT, 'magazines', filename)

            # Проверяем, не существует ли изображение уже
            if not os.path.exists(webp_path):
                with open(webp_path, 'wb') as image_file:
                    image_file.write(img_content.read())

            # Добавляем URL изображения к списку
            image_paths.append(os.path.join(settings.MEDIA_URL, 'magazines', filename))

        pdf.close()
        return image_paths

    def get_first_page_image_url(self):
        """
        Извлекает изображение первой страницы PDF и сохраняет его в формате WEBP.
        Возвращает путь к сохраненному изображению.
        """
        if not self.pdf:
            return None  # Если PDF нет, то и изображения первой страницы быть не может

        pdf = fitz.open(self.pdf.path)
        
        # Берём только первую страницу PDF
        page = pdf[0]
        pix = page.get_pixmap()
        img_data = BytesIO(pix.tobytes("ppm"))
        img = Image.open(img_data)

        img_io = BytesIO()
        img.save(img_io, format="WEBP", quality=80)  # Сохраняем в формате WEBP
        img_io.seek(0)  # Возвращаем указатель в начало файла
        
        # Формируем имя файла для первой страницы
        filename = f'magazine_{self.id}_page_1.webp'
        webp_path = os.path.join(settings.MEDIA_ROOT, 'magazines', filename)

        # Сохраняем изображение, если оно ещё не существует
        if not os.path.exists(webp_path):
            with open(webp_path, 'wb') as image_file:
                image_file.write(img_io.getvalue())
        
        pdf.close()
        return os.path.join(settings.MEDIA_URL, 'magazines', filename)  # Возвращаем URL изображения