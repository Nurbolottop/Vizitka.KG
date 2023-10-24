//  Preloader
jQuery(window).on("load", function () {
    $("#preloader").fadeOut(500);
    $("#main-wrapper").addClass("show");
});

(function ($) {
    "use strict";

    //to keep the current page active
    $(function () {
        for (
            var nk = window.location,
                o = $(".settings-menu a, .menu a")
                    .filter(function () {
                        return this.href == nk;
                    })
                    .addClass("active")
                    .parent()
                    .addClass("active");
            ;

        ) {
            // console.log(o)
            if (!o.is("li")) break;
            o = o.parent().addClass("show").parent().addClass("active");
        }
    });

    // Transaction history hove active
    $(".invoice-content").on("mouseover", "li", function () {
        $(".invoice-content li.active").removeClass("active");
        $(this).addClass("active");
    });

    // Balance Details widget of Home page
    $(".balance-stats").on("mouseover", function () {
        $(".balance-stats.active").removeClass("active");
        $(this).addClass("active");
    });

    //Bills widget of balance page
    $(".bills-widget-content").on("mouseover", function () {
        $(".bills-widget-content.active").removeClass("active");
        $(this).addClass("active");
    });

    $('.content-body').css({ 'min-height': (($(window).height())) + 50 +'px' });
})(jQuery);


// Dark light toggle switch
(function () {
    let onpageLoad = localStorage.getItem("theme") || "";
    let element = document.body;
    element.classList.add(onpageLoad);
    document.getElementById("theme").textContent =
        localStorage.getItem("theme") || "light";
})();

function themeToggle() {
    let element = document.body;
    element.classList.toggle("dark-theme");

    let theme = localStorage.getItem("theme");
    if (theme && theme === "dark-theme") {
        localStorage.setItem("theme", "");
    } else {
        localStorage.setItem("theme", "dark-theme");
    }
}
