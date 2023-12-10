window.addEventListener('storage', function(event) {
  if (event.key === 'theme') {
    // 检查深夜模式的新值，并相应地更新页面
    if (event.newValue === 'dark') {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  }
});
document.addEventListener('DOMContentLoaded', (event) => {
  if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark-mode');
    // 如果有切换按钮，也更新其文本
    var modeText = document.getElementById('toggle-mode');
    if (modeText) {
      modeText.textContent = 'Light Mode';
    }
  }
});
