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

