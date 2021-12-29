const profilCollapse = document.querySelector('#profilSideCollapse')
const profilOffcanvas = document.querySelector('.profil.offcanvas-collapse')
const profilClose = document.querySelector('#offCanvasCloseProfil')

profilCollapse.addEventListener('click', function () {
  profilOffcanvas.classList.toggle('open')
})

profilClose.addEventListener('click', function () {
  profilOffcanvas.classList.toggle('open')
})

