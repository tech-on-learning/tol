// Testimonials
$('#testi-carousel').owlCarousel({
    items:1,
    margin: 0,
    dots: true,
    nav: false,
    autoplay: true,
    autoplayHoverPause: true,
    smartSpeed: 450,
    dotsEach: true,
    autoplaySpeed: 999,
    loop:true,
    stagePadding: 0,
    dotsSpeed: 0,
    fade: true
});

// Preloader
$(window).on('load', function () {
    $('#PreKS').delay(0).fadeOut('slow');
    $('body').delay(0).css({
        'overflow': 'visible'
    });
});