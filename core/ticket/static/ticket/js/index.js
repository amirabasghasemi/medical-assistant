//Codes of the user panel...=
function openCity(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}
//Codes of the tickets section for tabbox...=>
function openbox(evt, boxName) {
  var i, tabbox, tabbar;
  tabbox = document.getElementsByClassName("tabbox");
  for (i = 0; i < tabbox.length; i++) {
    tabbox[i].style.display = "none";
  }
  tabbar = document.getElementsByClassName("tabbar");
  for (i = 0; i < tabbar.length; i++) {
    tabbar[i].className = tabbar[i].className.replace(" active", "");
  }
  document.getElementById(boxName).style.display = "block";
  evt.currentTarget.className += " active";
}
/*dark mode javascript code...
function toggleDarkLight() {
  var body = document.getElementById("body");
  var currentClass = body.className;
  body.className = currentClass == "dark-mode" ? "light-mode" : "dark-mode";
}
*/
//............................
