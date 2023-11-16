for (var i = 1; i <= 10; i++) {
  $("#flipbook").turn("addPage", "<div style='background-size: cover;'><img src='/media/magazines/" + i + ".webp' style='width: 100%; height: auto;'></div>");
}

// Подключение обработчиков событий после загрузки документа
document.addEventListener('DOMContentLoaded', function() {
  // Получение элемента книги и инициализация turn.js
  var flipbook = document.getElementById('flipbook');
  // Инициализируйте turn.js на вашем элементе книги здесь
  
  // Обновление индикатора страницы
  function updatePageIndicator() {
    var currentPage = $(flipbook).turn('page');
    var totalPages = $(flipbook).turn('pages');
    document.getElementById('page-indicator').textContent = currentPage + '/' + totalPages;
  }
  
  // Перелистывание на первую страницу
  document.getElementById('nav-first').addEventListener('click', function() {
    $(flipbook).turn('page', 1);
    updatePageIndicator();
  });

  // Перелистывание на предыдущую страницу
  document.getElementById('nav-prev').addEventListener('click', function() {
    $(flipbook).turn('previous');
    updatePageIndicator();
  });

  // Перелистывание на следующую страницу
  document.getElementById('nav-next').addEventListener('click', function() {
    $(flipbook).turn('next');
    updatePageIndicator();
  });

  // Перелистывание на последнюю страницу
  document.getElementById('nav-last').addEventListener('click', function() {
    var lastPage = $(flipbook).turn('pages');
    $(flipbook).turn('page', lastPage);
    updatePageIndicator();
  });

  // При каждом перелистывании обновлять индикатор страницы
  $(flipbook).bind('turned', function(event, page, view) {
    updatePageIndicator();
  });
  
  // Инициализация индикатора страницы
  updatePageIndicator();
});
