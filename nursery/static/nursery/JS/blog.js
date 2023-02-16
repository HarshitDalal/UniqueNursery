var viewsByWidth = 0;
let responsive = [
    {breakpoint:{width:0,viewsByWidth:1}},
    {breakpoint:{width:767,viewsByWidth:2}},
    {breakpoint:{width:1080,viewsByWidth:4}},
]
for (let i = 0; i < responsive.length; i++) {
    if (window.innerWidth>responsive[i].breakpoint.width) {
        viewsByWidth = responsive[i].breakpoint.viewsByWidth;
    }
}

var swiper = new Swiper(".mySwiper", {
    slidesPerView: viewsByWidth,
    spaceBetween: 30,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    
    navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
    },
  });