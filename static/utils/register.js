
document.body.addEventListener("scroll",()=>{
    !(document.body.scrollTop>5) ? document.getElementById("logo").setAttribute("b","h") : document.getElementById("logo").setAttribute("b","s");
});