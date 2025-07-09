const elm_icon_burger = document.getElementById('icon-burger');
const elm_sidebar = document.getElementById('sidebar');
const elm_tombol_open_close_sidebar = document.getElementById('tombol-open-close-sidebar');
const elm_icon_close = document.getElementById('icon-close');

elm_tombol_open_close_sidebar.addEventListener("click", (e) => {
    e.preventDefault();
    elm_sidebar.classList.toggle('hidden');
    elm_icon_burger.classList.toggle('hidden');
    elm_icon_close.classList.toggle('hidden');
})