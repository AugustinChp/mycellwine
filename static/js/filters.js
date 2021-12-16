(function(){
  const dropDownItem = document.querySelectorAll('#dropdownSortButton, .sort-item');
  const sortItem = document.querySelectorAll('.sort-item');

  for (let i = 0; i < dropDownItem.length; i++) {
    dropDownItem[i].addEventListener("click", function() {
      document.querySelector('.sort-menu').classList.toggle("show");
      });
  }

  for (let i = 0; i < sortItem.length; i++) {
    sortItem[i].addEventListener("click", function() {
      document.querySelector('#sortValue').innerHTML = sortItem[i].innerHTML;
      });
  }
})()