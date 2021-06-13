var items_on_page = 3;

var page_count = 1;

var div_num = document.querySelectorAll(".num");
if (div_num.length > items_on_page)
    page_count = Math.ceil(div_num.length / items_on_page);

for (let i = 0; i < div_num.length; i++) {
    if (i < items_on_page) {
        div_num[i].style.display = "block";
    }
}

var paginator = document.querySelector(".paginator");
var page = "";
for (let i = 0; i < page_count; i++) {
    page += "<span data-page=" + i * items_on_page + "  id=\"page" + (i + 1) + "\">" + (i + 1) + "</span>";
}
paginator.innerHTML = page;

var main_page = document.getElementById("page1");
main_page.classList.add("paginator_active");

function pagination(event) {
    var e = event || window.event;
    var target = e.target;
    var id = target.id;

    if (target.tagName.toLowerCase() != "span") return;

    var num_ = id.substr(4);
    var data_page = +target.dataset.page;
    main_page.classList.remove("paginator_active");
    main_page = document.getElementById(id);
    main_page.classList.add("paginator_active");

    var j = 0;
    for (let i = 0; i < div_num.length; i++) {
        let data_num = div_num[i].dataset.num;
        if (data_num <= data_page || data_num >= data_page)
            div_num[i].style.display = "none";

    }
    for (let i = data_page; i < div_num.length; i++) {
        if (j >= items_on_page)
          break;
        div_num[i].style.display = "block";
        j++;
    }
}