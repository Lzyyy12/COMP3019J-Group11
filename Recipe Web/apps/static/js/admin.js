window.onload = function() {
  var userdeletelist = document.querySelectorAll(".btn_delete");
  for (let i = 0; i < userdeletelist.length; i++) {
    // userdeletelist[i].setAttribute("data-index", i);
    userdeletelist[i].onclick = function () {
    // var index = this.getAttribute("data-index");
    //   userdeletelist.forEach(function (item, index) {
    // })
    // };
      var inputNode = this;
      var userid = this.getAttribute("user-id");
      var data = {userId: userid};
      //url = "delete_user";
      $.ajax({
        url: "delete_user",
        data: data,
        type: "post",
        success: function (response) {
          var parentNode = inputNode.parentNode.parentNode
          var grandParentNode = parentNode.parentNode
          grandParentNode.removeChild(parentNode)

          alert(response);
        }
      });
    }
  }
}

// function search() {
//   var input = document.getElementById("search").value;
//   var url = "./api/search?keyword=" + input;
//   var iframe = document.getElementById("recipeframe");
//   iframe.setAttribute("src", url)
// }