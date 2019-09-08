// When the user clicks on <div>, open the popup
function Popup() {
  var popup = document.getElementById('userPopup');
  console.log(popup);
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
    Popup("registerPopup")
    e.preventDefault();
         $.ajax({
             url: $(this).attr('action'),
             method: "GET",
             success: function(data){ $('#target').html(data) }
         });
  });
});