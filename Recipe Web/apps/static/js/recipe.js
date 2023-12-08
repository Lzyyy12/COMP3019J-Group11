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

document.addEventListener('DOMContentLoaded', function() {
  // 获取添加行按钮
  var addButton = document.getElementById('addRowButton');

  // 添加点击事件监听器
  addButton.addEventListener('click', function() {
    // 创建新的表格行和单元格
    var newRow = document.createElement('tr');
    var ingredientCell = document.createElement('td');
    var amountCell = document.createElement('td');

    // 创建输入框：食材
    var ingredientInput = document.createElement('input');
    ingredientInput.setAttribute('type', 'text');
    ingredientInput.setAttribute('name', 'ingredient[]');
    ingredientCell.appendChild(ingredientInput);

    // 创建输入框：用量
    var amountInput = document.createElement('input');
    amountInput.setAttribute('type', 'text');
    amountInput.setAttribute('name', 'amount[]');
    amountCell.appendChild(amountInput);

    // 将单元格添加到行
    newRow.appendChild(ingredientCell);
    newRow.appendChild(amountCell);

    // 将新行添加到表格的 tbody
    var tableBody = document.querySelector('#ingredientsTable tbody');
    tableBody.appendChild(newRow);
  });
});
