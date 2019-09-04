// When the user clicks on <div>, open the popup
function Popup(className) {
  var popup = document.getElementsByClassName(className);
  console.log(popup);
  //popup.classList.toggle("show");
  if (popup[0].style.visibility == "visible") {
    popup[0].style.visibility = "hidden";
  } else {
    popup[0].style.visibility = "visible";
  }
  //if (popup[0].getAttribute("visibility"))
  //popup[0].setAttribute("style", "visibility: visible"); //hidden
}
