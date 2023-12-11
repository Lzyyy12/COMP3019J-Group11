window.onload = function () {
  deleteuser();
}

function deleteuser() {
  var userdeletelist = document.querySelectorAll(".btn_delete");
  for (let i = 0; i < userdeletelist.length; i++) {
    userdeletelist[i].onclick = function () {
      var inputNode = this;
      var userid = this.getAttribute("user-id");
      var data = { userId: userid };
      $.ajax({
        url: "delete_user",
        data: data,
        type: "post",
        success: function (response) {
          if (response == 'delete succeeded') {
            var parentNode = inputNode.parentNode.parentNode;
            var grandParentNode = parentNode.parentNode;
            grandParentNode.removeChild(parentNode);
          }
          alert(response);
        }
      });
    }
  }
}

document.addEventListener('DOMContentLoaded', function () {
  var tags = document.querySelectorAll('.tags-list a'); // 获取所有标签

  tags.forEach(function (tag) {
    tag.addEventListener('click', function () {
      // 首先移除所有按钮的 'active-tag' 类
      tags.forEach(function (t) {
        t.classList.remove('active-tag');
      });

      // 然后给当前点击的按钮添加 'active-tag' 类
      tag.classList.add('active-tag');
    });
  });
});

function hideNavLinks() {
  document.querySelector('.nav-links').style.display = 'none';
}
function showNavLinks() {
  document.querySelector('.nav-links').style.display = 'flex';
}

// Get a list of navigation links and assign data-index attributes
var navlist = document.querySelectorAll(".nav-link");
for (let i = 0; i < navlist.length; i++) {
  navlist[i].setAttribute("data-index", i);
  navlist[i].onclick = function () {
    var index = this.getAttribute("data-index");

    for (let i = 0; i < navlist.length; i++) {
      if (index == i)
        navlist[i].style.color = "#FFFA05";
      else
        navlist[i].style.color = "#FFF";
    }
    // Update the color of the clicked link and adjust the iframe source accordingly
    var iframe = document.getElementById("manageframe");
    switch (index) {
      case "0":
        iframe.setAttribute("src", "./api/manage_recipe?type=all")
        break;
      case "1":
        iframe.setAttribute("src", "./api/manage_recipe?type=eastern")
        break;
      case "2":
        iframe.setAttribute("src", "./api/manage_recipe?type=western")
        break;

    }
  };
}

function search_user() {
  var input = document.getElementById("search_user").value;
  var url = "./search_user?keyword=" + input;
  $.ajax({
    url: url,
    type: "get",
    success: function (response) {
      var recipes = document.getElementById("recipes");
      html = '<div class="table-box"><table>'
        + '<tr><th id="user-id">ID</th><th id="user-name">Name</th><th id="opt-delete"></th></tr>';
      response.forEach(function (item, index) {
        html = html + '<tr><td>' + response[index].id + '</td><td>' + response[index].name + '</td>'
          + '<td><input type="button" class="btn_delete" user-id=' + response[index].id + ' value="Delete"/></td></tr>';
      });
      recipes.innerHTML = html;
      deleteuser();
    }
  });
}

function search_recipe() {
  var input = document.getElementById("search_recipe").value;
  var url = "./search_recipe?keyword=" + input;
  $.ajax({
    url: url,
    type: "get",
    success: function (response) {
      var recipes = document.getElementById("recipes");

      var html = '';
      response.forEach(function (item, index) {
        html = html + '<a href="./manage_edit_recipe/' + item.id + '" class="recipe">'
          + '<img src=' + item.path + ' class="img recipe-img" alt="" />'
          + '<h5>' + item.name + '</h5></a>';
      })
      recipes.innerHTML = html;
    }
  });
}