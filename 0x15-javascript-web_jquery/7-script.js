const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
tag = $("#character");
$.get(url, function(data, textualStatus) {
  const name = data["name"];
  tag.text(name);
})
