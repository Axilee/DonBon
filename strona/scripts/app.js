// Side bar toggle
$(document).ready(function() {

    function toggleSidebar() {
        $(".button").toggleClass("active");
        $(".sidebar-item").toggleClass("active");
        $("sidebar").toggleClass("nav-right visible-xs");
        $(".page-content").toggleClass("active");
        $('.sidebar').toggleClass('active');

    }
  
    $(".button").on("click tap", function() {
        toggleSidebar();
    });
});


  

// Loader strony
window.addEventListener('load',function(){
    document.querySelector('body').classList.add("loaded")  
  });
  
// TXT Effect 
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  let interval = null;
  
  document.getElementById("txt-effect").onmouseover = (event) => {
    let iteration = 0;
  
    clearInterval(interval);
  
    interval = setInterval(() => {
      event.target.innerText = event.target.innerText
        .split("")
        .map((letter, index) => {
          if (index < iteration) {
            return event.target.dataset.value[index];
          }
  
          return letters[Math.floor(Math.random() * 26)];
        })
        .join("");
  
      if (iteration >= event.target.dataset.value.length) {
        clearInterval(interval);
      }
  
      iteration += 1 / 3;
    }, 30);
  };

// Otwieranie modalu z ustawieniami 
  const modal = document.querySelector("#modal");
  const openModal = document.querySelector(".settings-open");
  const closeModal = document.querySelector(".settings-close");
  const restoreSettings = document.querySelector(".restore-settings"); 
  
  openModal.addEventListener("click", () => {
    modal.showModal();
  });
  
  closeModal.addEventListener("click", () => {
    modal.close();
  });

  
  restoreSettings.addEventListener("click", () => {
    //dodać funkcje przywracania domyślnych ustawień
    //tez kurwa nie wiem na chuj
  });

//Sidebar w modalu 
  $(function () {
    "use strict";

    $(".menu-box-tab:first").addClass("setting-active");
    $(".settings-inside:first").addClass("setting-active");
    
    $(".menu-box-tab").on("click", function () {
      $(".menu-box-tab").removeClass("setting-active");
      $(this).addClass("setting-active");
  

      var targetContent = $(this).attr("href");
      $(".settings-inside").removeClass("setting-active");
      $(targetContent).addClass("setting-active");
    });
  });

//Notyfikacje
  $(document).ready(function() {
    $('.save-settings').click(function() {
      $('.Message').addClass('is-hidden');
      $('.Message--green').removeClass('is-hidden');
      setTimeout(function() {
        $('.Message--green').addClass('hidding');
        setTimeout(function() {
          $('.Message--green').addClass('is-hidden');
          $('.Message--green').removeClass('hidding');
        }, 400);
      }, 5000);
    });
  });

  $(document).ready(function() {
    setInterval(function(){
      $(".Message--red").fadeOut(2000, function (){
        $(this).addClass("is-hidden").show();
      });
    }, 7000); //Czas podany w milisekundach do ukrycia popup'u 
  });
  

//Stronnicowanie
  var pr = $('.paginate.left');
  var pl = $('.paginate.right');
  var pageNames = ['DonBon', 'AxBon', 'BierBon', 'JarBon', 'BauBon']; // tablica nazw stron

  pr.click(function() { slide(-1) });
  pl.click(function() { slide(1) });

  var index = 0, total = 5; //Liczba stron

  var startX = null;
  var dragging = false;

  function slide(offset) {
    index = Math.min(Math.max(index + offset, 0), total - 1);

    function getPages(index) {
      var prevPage = index > 0 ? pageNames[index - 1] : null;
      var nextPage = index < pageNames.length - 1 ? pageNames[index + 1] : null;
      var currentPage = pageNames[index];
    return [prevPage, currentPage, nextPage];
    }

    var [prevPage, currentPage, nextPage] = getPages(index);

    $('.prev-page').text(prevPage || '');
    $('.current-page').text(currentPage || '');
    $('.next-page').text(nextPage || '');

    pr.attr('data-state', index === 0 ? 'disabled' : '');
    pl.attr('data-state', index === total - 1 ? 'disabled' : '');

    if (currentPage === 'DonBon') {
      $('.app-container').css('display', 'block');
      $('.app-container2').css('display', 'none');
    } else if (currentPage === 'AxBon') {
      $('.app-container').css('display', 'none');
      $('.app-container2').css('display', 'block');
    }
  }

  slide(0);

  var counter = $('.counter');

    counter.mousedown(function(event) {
    startX = event.pageX;
    dragging = true;
  });

  $(document).mousemove(function(event) {
    if (dragging) {
      var diffX = event.pageX - startX;
    if (Math.abs(diffX) > 50) { // przesuwanie jeżeli jest większa różnica niż 50px
      slide(diffX > 0 ? -1 : 1); // jeśli przesuwamy w prawo (diffX > 0), to zmniejszamy index o 1, w przeciwnym przypadku zwiększamy o 1
      startX = event.pageX;
      }
    }
  });

  $(document).mouseup(function(event) {
    dragging = false;
  });

  





 
