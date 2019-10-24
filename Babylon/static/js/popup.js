
// Toggles visibility

function popupVisible() {
    var popup = document.getElementById('bg-modal')

    //popup.classList.toggle("show");
    if (popup.style.visibility == "visible") {
      popup.style.visibility = "hidden";
    } else {
      popup.style.visibility = "visible";
    }
  }

  // Enables ajax

$(document).ready(function(e){
    $("#login-press").click(function(e){
      ajax($(this), e);
    });  
    $("#register-press").click(function(e){
      ajax($(this), e);
    });  
  });
function ajax(press, e, popupCall){
if(!popupCall)popupVisible();
e.preventDefault();
$.ajax({
    url: press.attr('action'),
    method: "GET",
    success: function(data){ $('#bg-modal').html(data) }
});
}
