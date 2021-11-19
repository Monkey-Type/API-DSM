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

btnPopup.addEventListener("click", () => {
  popup.classList.add('popup-active')
  document.body.style.overflow = "hidden"
})

popupBg.addEventListener("click", () => {
  popup.classList.remove('popup-active')
  document.body.style.overflow = "auto"
})


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
// BTN - INPUT
window.onload = function () {
  // Image
  var fileupload_img = document.getElementById("FileUp");
  var filePath_file = document.getElementById("Filepath");
  var button_file = document.getElementById("FileUpBTN");
  button_file.onclick = function () {
    fileupload_img.click();
  };
  fileupload_img.onchange = function () {
    var fileName = fileupload_img.value.split('\\')[fileupload_img.value.split('\\').length - 1];
    filePath_file.innerHTML = "<b>Arquivos: </b> " + fileName;
  };
  // Files
  var fileupload_file = document.getElementById("FilesUp");
  var filePath_file = document.getElementById("FilesPatch");
  var button_file = document.getElementById("FilesUpBTN");
  button_file.onclick = function () {
    fileupload_file.click();
  };
  fileupload_file.onchange = function () {
    var fileName = fileupload_file.value.split('\\')[fileupload_file.value.split('\\').length - 1];
    filePath_file.innerHTML = "<b>Arquivos: </b> " + fileName;
  };
};