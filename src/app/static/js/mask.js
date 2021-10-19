/* $(document).ready(function () {
  $('#cpf').mask('000.000.000-00');
  $('#ra').mask('0000000000000');
}); */

// Mascaras
document.addEventListener("DOMContentLoaded", function () {
  IMask(document.getElementById('cpf'), { mask: '000.000.000-00' });
  IMask(document.getElementById('ra'), { mask: '0000000000000' });
});
