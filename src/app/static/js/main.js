/* var menu = document.getElementById("menu");
var hamburger = document.getElementById("nav");
hamburger.addEventListener("click", () => {
  if (menu.classList.contains('toggled')) {
    menu.classList.remove('toggled')
  }
  else {
    menu.classList.add('toggled')
  }
}); */

// Popup
var popup = document.getElementById("popup")
var popupBg = document.getElementById("popupBg")
var btnPopup = document.getElementById("btnpop")

btnPopup.addEventListener("click", () => {
  popup.classList.add('popup-active')
  document.body.style.overflow = "hidden"
})

popupBg.addEventListener("click", () => {
  popup.classList.remove('popup-active')
  document.body.style.overflow = "auto"
})

// deletar post
function deletarPost(postId) {
  fetch('/deletar-post', {
    method: 'POST',
    body: JSON.stringify({ postId: postId })
  }).then((_res) => {
    window.location.href = "/editar";
  });
}