$(document).ready(function() {
    // Инициализация flipbook
    var flipbook = $("#flipbook").turn({
        width: 800,
        height: 600,
        autoCenter: true
    });

    // Добавление страниц
    for (var i = 1; i <= 10; i++) {
        flipbook.turn("addPage", "<div style='background-size: cover;'><img src='/media/magazines/" + i + ".webp' style='width: 100%; height: auto;'></div>");
    }

    // Инициализация Hammer.js
    var hammertime = new Hammer(flipbook[0]);
    hammertime.on('swipe', function(e) {
        if (e.direction == Hammer.DIRECTION_LEFT) {
            flipbook.turn('next');
        } else if (e.direction == Hammer.DIRECTION_RIGHT) {
            flipbook.turn('previous');
        }
    });

    // Обработчики для навигационных кнопок
    $("#nav-first").on('click', function() {
        flipbook.turn('page', 1);
    });

    $("#nav-prev").on('click', function() {
        flipbook.turn('previous');
    });

    $("#nav-next").on('click', function() {
        flipbook.turn('next');
    });

    $("#nav-last").on('click', function() {
        flipbook.turn('page', flipbook.turn('pages'));
    });

    // Обновление индикатора страниц при перелистывании
    flipbook.bind('turned', function(event, page, view) {
        $("#page-indicator").text(page + "/" + flipbook.turn('pages'));
    });
});
$(document).ready(function() {
    var currentScale = 1;
    var zoomStep = 0.1;

    function zoomIn() {
        currentScale += zoomStep;
        $('#flipbook').css('transform', 'scale(' + currentScale + ')');
        $('#flipbook').css('transform-origin', 'center center');
    }

    function zoomOut() {
        currentScale = Math.max(currentScale - zoomStep, zoomStep);
        $('#flipbook').css('transform', 'scale(' + currentScale + ')');
    }

    function zoomReset() {
        currentScale = 1;
        $('#flipbook').css('transform', 'none');
    }

    $('#zoom-in').click(zoomIn);
    $('#zoom-out').click(zoomOut);
    $('#zoom-reset').click(zoomReset);
});
