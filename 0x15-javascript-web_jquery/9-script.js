/* Jquery to say hello in french */
const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
$(document).ready(function() {
  $.get(url, function(data, textStatus) {
    const hello = data["hello"];
    $("#hello").text(hello);
  });
});
