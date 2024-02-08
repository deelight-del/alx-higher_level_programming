$(document).ready(function() {
  const item = "<li>Item</li>";
  let tag = $("ul.my_list");
  $("#add_item").on("click", function(event) {
    tag.append(item);
  });
  $("#remove_item").on("click", function(event) {
    tag.children("li").last().remove();
  });
  $("#clear_list").on("click", function(event) {
    tag.empty();
  });
});
