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

//Notyfikacje
  $(document).ready(function() {
    var clickCount = 0;
  
    $('.save-settings').click(function() {
      clickCount++;
  
      if (clickCount >= 5) {
        $('.Message').removeClass('Message--green').addClass('Message--red');
      }
  
      $('.Message').removeClass('is-hidden');
  
      setTimeout(function() {
        $('.Message').addClass('flyOut');
        setTimeout(function() {
          $('.Message').addClass('is-hidden').removeClass('flyOut');
          $('.Message').removeClass('Message--red').addClass('Message--green');
          clickCount = 0;
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
  


//Pagination
  var pr = document.querySelector('.paginate.left');
  var pl = document.querySelector('.paginate.right');
  var pageNames = ['DonBon', 'AxBon', 'BierBon', 'JarBon', 'BauBon']; // tablica nazw stron

  pr.onclick = slide.bind(this, -1);
  pl.onclick = slide.bind(this, 1);

  var index = 0, total = 5; //Liczba stron

  var startX = null;
  var dragging = false;

  function slide(offset) {
    index = Math.min(Math.max(index + offset, 0), total - 1);

    pr.setAttribute('data-state', index === 0 ? 'disabled' : '');
    pl.setAttribute('data-state', index === total - 1 ? 'disabled' : '');

    function getPages(index) {
      var prevPage = index > 0 ? pageNames[index - 1] : null;
      var nextPage = index < pageNames.length - 1 ? pageNames[index + 1] : null;
      var currentPage = pageNames[index];
    
      if (currentPage === 'DonBon') {
        document.querySelector('.app-container').style.display = 'block';
        document.querySelector('.app-container2').style.display = 'none';
      } else if (currentPage === 'AxBon') {
        document.querySelector('.app-container').style.display = 'none';
        document.querySelector('.app-container2').style.display = 'block';
      }
    
      return [prevPage, currentPage, nextPage];
    }
    
    var [prevPage, currentPage, nextPage] = getPages(index);

    document.querySelector('.prev-page').textContent = prevPage || '';
    document.querySelector('.current-page').textContent = currentPage || '';
    document.querySelector('.next-page').textContent = nextPage || '';


  }

  slide(0);

  var counter = document.querySelector('.counter');

  counter.addEventListener('mousedown', function(event) {
    startX = event.pageX;
    dragging = true;
  });

  document.addEventListener('mousemove', function(event) {
    if (dragging) {
      var diffX = event.pageX - startX;
      if (Math.abs(diffX) > 50) { // przesuwanie jest większa różnica niż 50px
        slide(diffX > 0 ? -1 : 1); // jeśli przesuwamy w prawo (diffX > 0), to zmniejszamy index o 1, w przeciwnym przypadku zwiększamy o 1
        startX = event.pageX;
      }
    }
  });

document.addEventListener('mouseup', function(event) {
  dragging = false;
});






 
