/******************************************/
const container = document.querySelector("#container-carousel");
const carousel = document.querySelector(".carousel");
let section = document.querySelectorAll(".library");
let sectionLast = section[section.length - 1];

const btnL = document.querySelector(".left-arrow");
const btnR = document.querySelector(".right-arrow");

carousel.insertAdjacentElement('afterbegin', sectionLast);

function next(){
    let sectionFirst= document.querySelectorAll(".library")[0];
    carousel.style.marginLeft = "calc((-(100vw - 5rem) / 5) * 2)";
    carousel.style.transition = "all 0.5s";
    setTimeout(function(){
        carousel.style.transition = "none";
        carousel.insertAdjacentElement('beforeend', sectionFirst);
        carousel.style.marginLeft = "calc(-(100vw - 5rem) / 5)";
    }, 500);
    console.log("iteracion");
}

function prev(){
    let section = document.querySelectorAll(".library");
    let sectionLast = section[section.length - 1];
    carousel.style.marginLeft = "-0.5rem";
    carousel.style.transition = "all 0.5s";
    setTimeout(function(){
        carousel.style.transition = "none";
        carousel.insertAdjacentElement('afterbegin', sectionLast);
        carousel.style.marginLeft = "calc(-(100vw - 5rem) / 5)";
    }, 500);
}

/*
function init(){
    setInterval(function(){
        next();
    }, 5000);
}

window.onload = init;
*/
btnR.addEventListener('click', function(){
    next();
});

btnL.addEventListener('click', function(){
    prev();
});

/******************************************/


/******************************************/
const collageContainer = document.querySelector("#collage-carousel");
const collageCarousel = document.querySelector(".collage-carousel");
let collageSection = document.querySelectorAll(".history");
let collageSectionLast = collageSection[collageSection.length - 1];

const btnLC = document.querySelector(".collage-left-arrow");
const btnRC = document.querySelector(".collage-right-arrow");

collageCarousel.insertAdjacentElement('afterbegin', collageSectionLast);

function nextC(){
    let collageSectionFirst= document.querySelectorAll(".history")[0];
    collageCarousel.style.marginLeft = "calc((-(100vw - 5rem) / 5) * 2)";
    collageCarousel.style.transition = "all 0.5s";
    setTimeout(function(){
        collageCarousel.style.transition = "none";
        collageCarousel.insertAdjacentElement('beforeend', collageSectionFirst);
        collageCarousel.style.marginLeft = "calc(-(100vw - 5rem) / 5)";
    }, 500);
    console.log("iteracion");
}

function prevC(){
    let collageSection = document.querySelectorAll(".history");
    let collageSectionLast = collageSection[collageSection.length - 1];
    collageCarousel.style.marginLeft = "-0.5rem";
    collageCarousel.style.transition = "all 0.5s";
    setTimeout(function(){
        collageCarousel.style.transition = "none";
        collageCarousel.insertAdjacentElement('afterbegin', collageSectionLast);
        collageCarousel.style.marginLeft = "calc(-(100vw - 5rem) / 5)";
    }, 500);
}

/*
function init(){
    setInterval(function(){
        next();
    }, 5000);
}

window.onload = init;
*/
btnRC.addEventListener('click', function(){
    nextC();
});

btnLC.addEventListener('click', function(){
    prevC();
});

/******************************************/



/******************************************/
const categoryContainer = document.querySelector("#category-carousel");
const categoryCarousel = document.querySelector(".category-carousel");
let categorySection = document.querySelectorAll(".category");
let categorySectionLast = categorySection[categorySection.length - 1];

const btnLCA = document.querySelector(".category-left-arrow");
const btnRCA = document.querySelector(".category-right-arrow");

categoryCarousel.insertAdjacentElement('afterbegin', categorySectionLast);

function nextCA(){
    let categorySectionFirst= document.querySelectorAll(".category")[0];
    categoryCarousel.style.marginLeft = "calc((-(100vw - 5rem) / 5) * 2)";
    categoryCarousel.style.transition = "all 0.5s";
    setTimeout(function(){
        categoryCarousel.style.transition = "none";
        categoryCarousel.insertAdjacentElement('beforeend', categorySectionFirst);
        categoryCarousel.style.marginLeft = "calc(-(100vw - 5rem) / 5)";
    }, 500);
    console.log("iteracion");
}

function prevCA(){
    let categorySection = document.querySelectorAll(".category");
    let categorySectionLast = categorySection[categorySection.length - 1];
    categoryCarousel.style.marginLeft = "-0.5rem";
    categoryCarousel.style.transition = "all 0.5s";
    setTimeout(function(){
        categoryCarousel.style.transition = "none";
        categoryCarousel.insertAdjacentElement('afterbegin', categorySectionLast);
        categoryCarousel.style.marginLeft = "calc(-(100vw - 5rem) / 5)";
    }, 500);
}

/*
function init(){
    setInterval(function(){
        next();
    }, 5000);
}

window.onload = init;
*/
btnRCA.addEventListener('click', function(){
    nextCA();
});

btnLCA.addEventListener('click', function(){
    prevCA();
});

/******************************************/