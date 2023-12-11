function hideNavLinks() {
  document.querySelector('.nav-links').style.display = 'none';
}
function showNavLinks() {
  document.querySelector('.nav-links').style.display = 'flex';
}

document.addEventListener('DOMContentLoaded', function() {
    var changeLinks = document.querySelectorAll('.tags-list .change a'); // 只获取前四个链接

    changeLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            // 首先移除所有前四个链接的 'active' 类
            changeLinks.forEach(function(lnk) {
                lnk.classList.remove('active');
            });

            // 然后给当前点击的链接添加 'active' 类
            this.classList.add('active');
        });
    });
});


// Function to get an element by its selector, throwing an error if not found
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


// Get a list of navigation links and assign data-index attributes
var navlist = document.querySelectorAll(".nav-link");
var iframe = document.getElementById("recipeframe");
var currentPageType = getCurrentPageType(); // 获取当前页面类型的函数

for (let i = 0; i < navlist.length; i++) {
  navlist[i].setAttribute("data-index", i);
  navlist[i].onclick = function () {
    var index = this.getAttribute("data-index");

    // 更新链接颜色
    updateNavLinksColor(navlist, index);

    // 根据页面类型和点击的 nav-link 更新 iframe 的 src
    updateIframeSource(iframe, currentPageType, index);
  };
}

function getCurrentPageType() {
  // 这里添加逻辑来判断当前是哪个页面，返回 'main', 'favorite' 或 'posted'
  if (window.location.href.includes('main')) {
    return 'main';
  } else if (window.location.href.includes('favorite')) {
    return 'favorite';
  } else if (window.location.href.includes('user')) {
    return 'user';
  }
  return 'main'; // 默认返回 'main'
}

function updateNavLinksColor(navlist, selectedIndex) {
  for (let i = 0; i < navlist.length; i++) {
    navlist[i].style.color = (selectedIndex == i) ? "#FFFA05" : "#FFF";
  }
}

function updateIframeSource(iframe, pageType, index) {
  var src;
  switch (pageType) {
    case 'main':
      src = `./api/get_recipe?type=${getRecipeType(index)}`;
      break;
    case 'favorite':
      src = `./api/get_favorite?type=${getRecipeType(index)}`;
      break;
    case 'user':
      src = `./api/get_posted_recipe?type=${getRecipeType(index)}`;
      break;
  }
  iframe.setAttribute('src', src);
}

function getRecipeType(index) {
  switch (index) {
    case "0": return "all";
    case "1": return "eastern";
    case "2": return "western";
  }
  return "all"; // 默认返回 'all'
}

document.getElementById('toggle-mode').addEventListener('click', function() {
  var modeText = document.getElementById('toggle-mode');
  document.body.classList.toggle('dark-mode');

  // 检查当前是否已经应用了深夜模式
  if (document.body.classList.contains('dark-mode')) {
    modeText.textContent = 'Light Mode'; // 如果是深夜模式，改为 "Light Mode"
    localStorage.setItem('theme', 'dark'); // 保存深夜模式设置
  } else {
    modeText.textContent = 'Dark Mode'; // 否则，改为 "Dark Mode"
    localStorage.removeItem('theme'); // 移除深夜模式设置
  }
});

// 页面加载时检查本地存储中的主题设置
document.addEventListener('DOMContentLoaded', (event) => {
  if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-mode');
    document.getElementById('toggle-mode').textContent = 'Light Mode';
  }
});
