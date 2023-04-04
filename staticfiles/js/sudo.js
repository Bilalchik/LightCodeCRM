    // создаем объект Swiper и настраиваем его
    var mySwiper = new Swiper('.swiper-container', {
      slidesPerView: 3, /* показываем сразу 3 слайда */
      spaceBetween: 30,
      loop: false, /* включаем бесконечный скролл */
      autoHeight: true,
      centeredSlides: true, /* делаем активный слайд по центру */
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true, /* делаем точки навигации кликабельными */
      },
    });

    // добавляем обработчик события click для слайдов
    var slides = document.querySelectorAll('.swiper-slide');
    for (var i = 0; i < slides.length; i++) {
      slides[i].addEventListener('click', function () {
        mySwiper.slideToLoop(this.dataset.swiperSlideIndex);
      });
    }
    slides.forEach((item, index) => {
    item.setAttribute('data-swiper-slide-index', index)
    })


