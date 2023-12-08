from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from datetime import datetime
from django.contrib import messages
from apps.blog.views import get_weather_data
from asgiref.sync import async_to_sync

from . import models  # Подключите вашу модель Settings и User
from apps.index.models import Settings
def register(request):
    current_date = datetime.now()
    setting = Settings.objects.latest('id')
    temperature, weather_condition = async_to_sync(get_weather_data)()


    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        agree = request.POST.get('agree')

        if not agree:
            messages.error(request, "Вы должны согласиться с условиями предоставления услуг.")
            return render(request, 'users/register-32.html', locals())
        
        if password != confirm_password:
            messages.error(request, "Пароли не совпадают.")
            return render(request, 'users/register-32.html', locals())

        if not all([username, password, email, phone]):
            messages.error(request, "Пожалуйста, заполните все поля.")
            return render(request, 'users/register-32.html', locals())

        # Создайте пользователя и установите его атрибуты
        user = models.User.objects.create_user(username=username, email=email, password=password)
        user.phone = phone
        user.save()

        # Аутентифицируйте пользователя и выполните вход
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile', user.id)  # Перенаправьте на профиль пользователя

    return render(request, 'users/register-32.html', locals())


def profile(request,id):
    setting = Settings.objects.latest('id')
    user = models.User.objects.get(id=id)
    if request.method == "POST":
        if 'update_account' in request.POST:
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            user.first_name = first_name
            user.phone = phone
            user.email = email
            user.address = address
            user.save()
            return redirect('profile', request.user.id)
        if 'change_password' in request.POST:
            old_password = request.POST['old_password']
            new_password1 = request.POST['new_password1']
            new_password2 = request.POST['new_password2']
            user = request.user

            # Проверяем, совпадает ли введенный старый пароль с текущим паролем пользователя
            if user.check_password(old_password):
                # Проверяем, совпадают ли новые пароли
                if new_password1 == new_password2:
                    # Устанавливаем новый пароль
                    user.set_password(new_password1)
                    user.save()
                    
                    # Авторизуем пользователя с новым паролем
                    user = authenticate(username=user.username, password=new_password1)
                    if user:
                        login(request, user)

                    messages.success(request, 'Пароль успешно изменен.')
        if 'profile_images' in request.POST:
            username = request.POST.get('username')
            profile_image = request.FILES.get('profile_image')
            user.username = username
            user.profile_image = profile_image
            user.save()
            return redirect('profile', request.user.id)
    return render(request, 'users/settings-profile.html', locals())

def get_latest_settings():
    return Settings.objects.latest('id')

def user_login(request):
    setting = Settings.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # Получаем значение "Remember me"

        try:
            user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            messages.error(request, 'Пользователь с таким именем не существует.')
            return redirect('login')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Устанавливаем срок действия сессии, основываясь на "Remember me"
            if remember_me:
                # Если "Remember me" установлен, устанавливаем срок действия на 2 недели
                request.session.set_expiry(1209600)  # 2 недели в секундах
            else:
                # Если "Remember me" не установлен, сессия истекает при закрытии браузера
                request.session.set_expiry(0)

            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'Неправильный пароль')
            return redirect('login')
    
    return render(request, 'users/login-32.html', locals())


