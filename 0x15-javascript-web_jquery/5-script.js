/* JQQUERY to add element to already existing list */
let my_list = $("UL.my_list");
$("#add_item").on("click", function(event) {
  my_list.append('<li>Item</li>');
});
