window.onload = function() {
  var userdeletelist = document.querySelectorAll(".btn_delete");
  for (let i = 0; i < userdeletelist.length; i++) {
    userdeletelist[i].onclick = function () {
      var inputNode = this;
      var userid = this.getAttribute("user-id");
      var data = {userId: userid};
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

document.addEventListener('DOMContentLoaded', function() {
    var tags = document.querySelectorAll('.tags-list a'); // 获取所有标签

    tags.forEach(function(tag) {
        tag.addEventListener('click', function() {
            // 首先移除所有按钮的 'active-tag' 类
            tags.forEach(function(t) {
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
