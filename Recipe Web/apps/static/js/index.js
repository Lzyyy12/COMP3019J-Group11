const getElement = (selector) => {
    const element = document.querySelector(selector)
  
    if (element) return element
    throw Error(
      `Please double check your class names, there is no ${selector} class`
    )
  }
  
const links = getElement('.nav-links')
const navBtnDOM = getElement('.nav-btn')

navBtnDOM.addEventListener('click', () => {
  links.classList.toggle('show-links')
})

// function all_recipe() {
//   var iframe = document.getElementById("recipeframe");
//   iframe.setAttribute("src", "./api/get_recipe?type=all")
// }

// function eastern() {
//   var iframe = document.getElementById("recipeframe");
//   iframe.setAttribute("src", "./api/get_recipe?type=eastern")
// }

// function western() {
//   var iframe = document.getElementById("recipeframe");
//   iframe.setAttribute("src", "./api/get_recipe?type=western")
// }

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

    var iframe = document.getElementById("recipeframe");
    switch (index) {
      case "0":
        iframe.setAttribute("src", "./api/get_recipe?type=all")
        break;
      case "1":
        iframe.setAttribute("src", "./api/get_recipe?type=eastern")
        break;
      case "2":
        iframe.setAttribute("src", "./api/get_recipe?type=western")
        break;
    }
  };
}