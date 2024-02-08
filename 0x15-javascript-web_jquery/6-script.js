/* Jquery to change the text of the header*/
let header = $("header");
$("#update_header").on("click", function(event) {
  header.text("New Header!!!");
});
