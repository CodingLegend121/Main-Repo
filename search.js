function draw() {
  let searchInput = document.getElementById('searchId').value;
  let searchBtn = document.getElementById('btn').href;
  let Gsearch = document.getElementById('searchIdG').value;
  searchBtn = (searchInput);
  if (searchBtn == 'myHomeWeb' || searchBtn == '427' || searchBtn == 'execute') {
    searchBtn = 'blog.html';
  } else if (searchBtn == 'google' || searchBtn == 'Google') {
    searchBtn = google()
  } else if (searchBtn == 'wikipedia' || searchBtn == 'Wikipedia') {
    searchBtn = wikipedia()
  } else if (searchBtn == 'youtube' || searchBtn == 'Youtube') {
    searchBtn = 'youtube.html'
  } else {
    searchBtn = ("#" + searchInput);
  }
  Gsearch = ('https://google.com/' + Gsearch)
  document.getElementById('btnG').href = Gsearch;
  document.getElementById('btn').href = searchBtn;
}

function google() {
  document.getElementById('Gsearch').style.visibility = "visible";
}

function wikipedia() {
  document.getElementById('Wsearch').style.visibility = "visible";
}