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
  const saveSettings = document.querySelector(".save-settings");
  const restoreSettings = document.querySelector(".restore-settings"); 
  
  openModal.addEventListener("click", () => {
    modal.showModal();
  });
  
  closeModal.addEventListener("click", () => {
    modal.close();
  });

  saveSettings.addEventListener("click", () => {
    modal.close();
    $(".Message--green").removeClass("is-hidden");
  });
  
  restoreSettings.addEventListener("click", () => {
    //dodać funkcje przywracania domyślnych ustawień
    //tez kurwa nie wiem na chuj
  });


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
    setInterval(function(){
      $(".Message--green").addClass("is-hidden");
    }, 5000); //Czas podany w milisekundach do ukrycia popup'u 
  });

  $(document).ready(function() {
    setInterval(function(){
      $(".Message--red").fadeOut(2000, function (){
        $(this).addClass("is-hidden").show();
      });
    }, 5000); //Czas podany w milisekundach do ukrycia popup'u 
  });
  
