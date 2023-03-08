
window.onpointermove = event => { 
  const { clientX, clientY } = event;
  const cursorEfect = document.getElementById("cursorEfect");


  cursorEfect.animate({
    left: `${clientX}px`,
    top: `${clientY}px`
  }, { duration: 3000, fill: "forwards" });
}

window.addEventListener('load',function(){
  document.querySelector('body').classList.add("loaded")  
});