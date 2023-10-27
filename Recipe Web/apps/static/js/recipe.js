var recipe = document.querySelectorAll(".recipe");

function eastern() {
    recipe[0].style.display = "block";
    recipe[1].style.display = "";
    recipe[2].style.display = "";
}

function westerne() {
    recipe[0].style.display = "";
    recipe[1].style.display = "block";
    recipe[2].style.display = "";
}

function turkish() {
  recipe[0].style.display = "";
  recipe[1].style.display = "";
  recipe[2].style.display = "block";
}