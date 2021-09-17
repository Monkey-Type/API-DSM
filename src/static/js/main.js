var menu = document.getElementById("menu");
var hamburger = document.getElementById("nav");
hamburger.addEventListener("click", () => {
  if (menu.classList.contains('toggled')) {
    menu.classList.remove('toggled')
  }
  else {
    menu.classList.add('toggled')
  }
});