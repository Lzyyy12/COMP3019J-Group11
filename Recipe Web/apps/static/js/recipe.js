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

var recipe_type = "{{ recipe_type }}";
function search(searchType) {
    var input = document.getElementById("search").value;
    var url = "./search?keyword=" + input + "&search_type=" + searchType + "&recipe_type=" + recipe_type;
    $.ajax({
        url: url,
        type: "get",
        success: function (response) {
            var recipes = document.getElementById("recipes");

            var html = '';
            response.forEach(function (item, index) {
                html = html + '<a href="./recipe_detail/' + item.id + '" class="recipe">'
                    + '<img src=' + item.path + ' class="img recipe-img" alt="" />'
                    + '<h5>' + item.name + '</h5></a>';
            })
            recipes.innerHTML = html;
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
  // 获取添加行按钮
  var addRowButton = document.getElementById('addRow');
  // 获取删除行按钮
  var deleteRowButton = document.getElementById('deleteRow');

  // 添加行的事件监听器
  addRowButton.addEventListener('click', function() {
    var tableBody = document.querySelector('#ingredientsTable tbody');
    var newRow = document.createElement('tr');
    var ingredientCell = document.createElement('td');
    var amountCell = document.createElement('td');

    var ingredientInput = document.createElement('input');
    ingredientInput.setAttribute('type', 'text');
    ingredientInput.setAttribute('name', 'ingredient[]');
    ingredientCell.appendChild(ingredientInput);

    var amountInput = document.createElement('input');
    amountInput.setAttribute('type', 'text');
    amountInput.setAttribute('name', 'amount[]');
    amountCell.appendChild(amountInput);

    newRow.appendChild(ingredientCell);
    newRow.appendChild(amountCell);
    tableBody.appendChild(newRow);
  });

  // 删除行的事件监听器
  deleteRowButton.addEventListener('click', function() {
    var tableBody = document.querySelector('#ingredientsTable tbody');
    if (tableBody.rows.length > 0) {
      tableBody.deleteRow(-1); // 删除最后一行
    } else {
      alert('表格中没有更多行可以删除！');
    }
  });
});


function handleFileSelected() {
    var oFReader = new FileReader();
        var file = document.getElementById('id_for_file').files[0];
        oFReader.readAsDataURL(file);
        oFReader.onloadend = function(oFRevent){
            var filePath = oFRevent.target.result;

            var image = document.getElementById("recipe-image");
            image.setAttribute('src', filePath);
        }
}

function uploadimage(username) {
    var formData = new FormData;
    var file = $('[name="photo"]')[0].files[0];
    formData.append("file", file);
    $.ajax({
        url: "/api/upload",
        data: formData,
        type: "post",
        async: false,
        contentType: false,
        processData: false,
        success: function (msg) {
            alert("image upload sucecced");
            $('[name="imagepath"]').val(msg.filename);
        }
    });
}
// 当本地存储发生变化时触发