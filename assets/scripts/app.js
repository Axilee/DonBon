window.addEventListener('load',function(){
  document.querySelector('body').classList.add("loaded")  
});

// Dark / light mode

const switchTheme = () => {
  const rootElem = document.documentElement
  let dataTheme = rootElem.getAttribute('data-theme'),
    newTheme

  newTheme = (dataTheme === 'light') ? 'dark' : 'light'

  rootElem.setAttribute('data-theme', newTheme)
}

document.querySelector('#theme-switcher').addEventListener('click', switchTheme)
