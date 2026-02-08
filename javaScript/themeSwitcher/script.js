const themes = [
  {name: "light", message: "Hello sunshine. Light theme is on!"},
  {name: "dark", message: "The night is yours. Dark theme is on!"},
  {name: "ocean", message: "Blue skies and high tides. Ocean theme is on!"},
  {name: "nord", message: "The frost has settled. Nord theme is on!"}
];

const themeBtn = document.getElementById("theme-switcher-button");
const themeMenu = document.getElementById("theme-dropdown")
const menuItem = document.querySelectorAll('[role="menuitem"]');
const liveRegion = document.querySelector('[aria-live="polite"]');

themeBtn.addEventListener("click", () => {
  const isHidden = themeMenu.toggleAttribute("hidden");
  themeBtn.setAttribute("aria-expanded", String(!isHidden));
  
});


menuItem.forEach(item => {
  item.addEventListener("click", () => {

  const selectedTheme = item.id.replace("theme-", "");

  document.body.classList.forEach(className => {
    if(className.startsWith("theme-")){
      document.body.classList.remove(className);
    }
  });
  document.body.classList.add(`theme-${selectedTheme}`);
  
  const theme = themes.find(t => t.name === selectedTheme)
  if(theme){
    liveRegion.textContent = theme.message;
  }
  themeMenu.setAttribute("hidden", "");
  themeBtn.setAttribute("aria-expanded", "false");
  });
});

  