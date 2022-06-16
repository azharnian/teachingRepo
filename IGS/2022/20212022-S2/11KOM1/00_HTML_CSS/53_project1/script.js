document.addEventListener('DOMContentLoaded', () => {

  document.querySelector('.menu-toggle').addEventListener('click', function(){

    document.querySelectorAll('.menu-toggle-item').forEach((item, i) => {

      // if (!item.classList.contains('clicked')) {
      //   item.classList.add('clicked');
      // }
      // else {
      //   item.classList.remove('clicked');
      // }

      item.classList.toggle('clicked');
      document.querySelector('.menu-nav').classList.toggle('clicked');
    });


  })

})
