// When the user clicks on <div>, open the popup
function Popup() {
  var popup = document.getElementById('userPopup');
  //popup.classList.toggle("show");
  if (popup.style.visibility == "visible") {
    popup.style.visibility = "hidden";
  } else {
    popup.style.visibility = "visible";
  }
  //if (popup[0].getAttribute("visibility"))
  //popup[0].setAttribute("style", "visibility: visible"); //hidden
}
$(document).ready(function(e){
  $("#register_press").click(function(e){
    ajax($(this), e);
  });
  $("#login_press").click(function(e){
    ajax($(this), e);
  });  
});
function ajax(press, e){
  Popup()
  e.preventDefault();
  $.ajax({
      url: press.attr('action'),
      method: "GET",
      success: function(data){ $('#target').html(data) }
  });
}
