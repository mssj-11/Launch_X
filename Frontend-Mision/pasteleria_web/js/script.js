/*  BUTTON TOOGGLE START */
let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{

    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');

}
/*  BUTTON TOOGGLE END */



/*  ingredientes BUTTON START   */
const details = document.querySelectorAll(".ingre");

details.forEach((ingre) => {

    ingre.addEventListener("click", () => {
        ingre.classList.toggle("active");
    });

});
/*  ingredientes BUTTON END   */