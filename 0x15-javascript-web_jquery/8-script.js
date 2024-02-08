const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
let movies_list = $("#list_movies");
$.get(url, function(data, textStatus) {
  const results = data["results"];
  results.forEach(function(element) {
    movies_list.append($("<li></li>").text(element["title"]));
  });
});
