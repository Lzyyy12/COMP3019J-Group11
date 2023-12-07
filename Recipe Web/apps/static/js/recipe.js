function addIngredient() {
    var input = document.getElementById("newIngredient").value;
    var colour = document.createElement("option");
    colour.textContent = input;
    
    var item = document.getElementById("ingredientSelect");
    item.add(colour);
}

function ajax_submit(username) {
    var input = document.getElementById("search").value;
    var url = "./api/search?keyword=" + input;
    var iframe = document.getElementById("recipeframe");
    iframe.setAttribute("src", url)
}

function search() {
    var input = document.getElementById("search").value;
    var url = "./search?keyword=" + input;
    $.ajax({
        url: url,
        type: "get",
        success: function (response) {
            var recipes = document.getElementById("recipes");

            var html = '';
            response.forEach(function (item, index) {
                html = html + '<a href="single-recipe.html" class="recipe">'
                    + '<img src=' + item.path + ' class="img recipe-img" alt="" />'
                    + '<h5>' + item.name + '</h5></a>';
            })
            recipes.innerHTML = html;
        }
    });
}