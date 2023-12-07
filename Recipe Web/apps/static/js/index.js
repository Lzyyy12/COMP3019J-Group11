
function hideNavLinks() {
  document.querySelector('.nav-links').style.display = 'none';
}
// Function to get an element by its selector, throwing an error if not found
const getElement = (selector) => {
  const element = document.querySelector(selector);

  if (element) return element;
  throw Error(
    `Please double check your class names, there is no ${selector} class`
  );
}

// Get the navigation links and the navigation button elements
const links = getElement('.nav-links');
const navBtnDOM = getElement('.nav-btn');

// Add a click event listener to the navigation button to toggle the class for showing links
navBtnDOM.addEventListener('click', () => {
  links.classList.toggle('show-links')
})

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

// function search() {
//   var input = document.getElementById("search").value;
//   var url = "./api/search?keyword=" + input;
//   var iframe = document.getElementById("recipeframe");
//   iframe.setAttribute("src", url)
// }