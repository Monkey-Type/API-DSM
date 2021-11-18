/* var menu = document.getElementById("menu");
var hamburger = document.getElementById("nav");
hamburger.addEventListener("click", () => {
  if (menu.classList.contains('toggled')) {
    menu.classList.remove('toggled')
  }
  else {
    menu.classList.add('toggled')
  }
}); 
*/

// Popup
var popup = document.getElementById("popup")
var popupBg = document.getElementById("popupBg")
var btnPopup = document.getElementById("btnpop")

function closeEdit() {
  popup.classList.remove('popup-active')
  document.body.style.overflow = "auto"
}


btnPopup.addEventListener("click", () => {
  popup.classList.add('popup-active')
  document.body.style.overflow = "hidden"
})

popupBg.addEventListener("click", () => {
  popup.classList.remove('popup-active')
  document.body.style.overflow = "auto"
});


function abrirPopup(id) {
  modal = document.querySelector("[data-id='" + id + "']");
  modal.classList.add('popup-active')
  document.body.style.overflow = "hidden"
}

function fecharPopup(id) {
  modal = document.querySelector("[data-id='" + id + "']");
  modal.classList.remove('popup-active')
  document.body.style.overflow = "auto"
}

function stop(event) {
  event.stopPropagation();
}


// deletar post
function deletarPost(postId) {
  fetch('/deletar-post', {
    method: 'POST',
    body: JSON.stringify({ postId: postId })
  }).then((_res) => {
    window.location.href = "/editar";
  });
}
function arquivarPost(postId) {
  fetch('/arquivar-post', {
    method: 'POST',
    body: JSON.stringify({ postId: postId })
  }).then((_res) => {
    window.location.href = "/";
  });
}

function togglefilter() {
  filtro = document.getElementById('filtro')
  filtro.style.display = 'block';
  document.body.style.overflow = 'hidden';
}

function closefilter() {
  filtro = document.getElementById('filtro')
  filtro.style.display = 'none';
  document.body.style.overflow = 'visible';
}