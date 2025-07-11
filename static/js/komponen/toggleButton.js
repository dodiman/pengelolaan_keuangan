const elm_icon_burger = document.getElementById('icon-burger');
const elm_sidebar = document.getElementById('sidebar');
const elm_tombol_open_close_sidebar = document.getElementById('tombol-open-close-sidebar');
const elm_icon_close = document.getElementById('icon-close');

elm_tombol_open_close_sidebar.addEventListener("click", (e) => {
    e.preventDefault();
    // tampil & sembunyikan sidebar
    if (elm_sidebar.classList.contains("hidden")) {
        elm_sidebar.classList.remove('hidden');
        elm_sidebar.classList.add("flex")
        elm_icon_burger.classList.remove('hidden');
        elm_icon_burger.classList.add("flex")
        elm_icon_close.classList.remove('hidden');
        elm_icon_burger.classList.add("flex")
    } else {
        elm_sidebar.classList.remove("flex");
        elm_sidebar.classList.add("hidden")
        elm_icon_burger.classList.remove("flex");
        elm_icon_burger.classList.add("hidden");
        elm_icon_close.classList.remove('flex');
        elm_icon_close.classList.add('hidden');
    }
})