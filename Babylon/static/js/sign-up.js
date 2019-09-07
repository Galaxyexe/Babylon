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
$(document).ready(function(e){
  $("#register_form").submit(function(e){
    console.log("A")
    e.preventDefault();
         $.ajax({
             url: $(this).attr('action'),
             method: $(this).attr('method'),
             success: function(data){ $('#target').html(data) }
         });
  });
});