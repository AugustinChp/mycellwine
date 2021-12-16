(function () {
  'use strict'
  document.querySelector('#profilSideCollapse').addEventListener('click', function () {
    document.querySelector('.profil.offcanvas-collapse').classList.toggle('open')
  })

  document.querySelector('#offCanvasCloseProfil').addEventListener('click', function () {
    document.querySelector('.profil.offcanvas-collapse').classList.toggle('open')
  })


  document.querySelector('#offCanvasCloseNotification').addEventListener('click', function () {
    document.querySelector('.notification.offcanvas-collapse').classList.toggle('open')
  })
})()
