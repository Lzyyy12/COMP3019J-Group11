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
