// Execute sticky check when user scrolls
window.onscroll = function () { stickyCheck() };

var nav = document.getElementById("nav");
var sticky = nav.offsetTop;

// Function to add sticky class to nav bar when it reaches the top of the window and remove it otherwise
function stickyCheck() {

    if (window.pageYOffset >= sticky) {
        nav.classList.add("sticky")
    } else {
        nav.classList.remove("sticky");
    }
}

