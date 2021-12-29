const modalClose = document.querySelector("#modalClose")
const modal = document.querySelector(".modal")
const joinCellar = document.querySelector("#joinCellar")
const joinCellarModal = document.querySelector("#joinCellarModal")
const createNewCellar = document.querySelector("#createNewCellar")
const inviteCodeField = document.querySelector("#inviteCodeField")

createNewCellar.addEventListener('click', function(){
    inviteCodeField.value='';
});

joinCellar.addEventListener('click', function(){
    joinCellarModal.style.display='block';
});

modalClose.addEventListener('click', function(){
    modal.style.display='none';
});