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

// function search() {
//   var input = document.getElementById("search").value;
//   var url = "./api/search?keyword=" + input;
//   var iframe = document.getElementById("recipeframe");
//   iframe.setAttribute("src", url)
// }