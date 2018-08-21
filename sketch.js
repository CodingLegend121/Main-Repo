function openNav() {
  document.getElementById("mySidenav").style.width = "13vw";
  document.getElementById("main").style.marginLeft = "12vw";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

if (window.innerWidth < 650) {
  console.log('Hooray!');
}

function openUrl(url) {
  window.open(url, "_blank")
}