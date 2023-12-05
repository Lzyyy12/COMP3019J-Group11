function addIngredient() {
    var input = document.getElementById("newIngredient").value;
    var colour = document.createElement("option");
    colour.textContent = input;
    
    var item = document.getElementById("ingredientSelect");
    item.add(colour);
}

function ajax_submit(username) {
    let formData = new FormData;
    let file = $('[name="photo"]')[0].files[0];
    formData.append("file", file);
    $.ajax({
        url: "./upload",
        data: formData,
        type: "post",
        async: false,
        contentType: false,
        processData: false,
        success: function (msg) {
            alert(msg.filename);
            // $('[name="photo"]').val(msg)
            // $("#imgId").prop("src", msg)
        }
    });
}
