

document.getElementsByClassName("contt")[0].onclick = ()=>{
    gjdkkjh();
}

function gjbkkjh(a,b){
    a=+a;
    if(b.className=="opt"){ 
        switch (a) {
            case 1 : document.body.setAttribute("m","o");gjdkkjh(); break;
            case 2 : document.body.setAttribute("m","w");gjdkkjh(); break;
            case 3 : document.body.setAttribute("m","e");gjdkkjh(); break;
            case 4 : document.body.setAttribute("m","n");gjdkkjh(); break;
            case 5 : document.body.setAttribute("m","s");gjdkkjh(); break;
            case 6 : document.body.setAttribute("m","h");gjdkkjh(); break;
            
            default : document.body.setAttribute("m","o"); break;
        }
    }else{
        console.log("Wish you best of Luck !!");
    }
}

function gjdkkjh(){
    if(document.body.getAttribute("h")){
        switch(document.body.getAttribute("h")){
            case "h" : document.body.setAttribute("h","o"); break;
            case "o" : document.body.setAttribute("h","h"); break;
        }
        if(document.body.getAttribute("h") && (document.body.getAttribute("h") !="h" && document.body.getAttribute("h") !="o")){
            document.body.setAttribute("h","h");
        }
    }
}




function one_click() {
    if(!!document.getElementById("menu_check").checked){
        document.getElementById("menu").style="background:#f8f8f8; box-shadow:0 0 6px 0 rgba(0,0,0,0.23);";
        document.getElementsByClassName("info")[0].style="display:block; position:absolute; top:72px; background:rgba(20,20,20,0.5);";
        document.documentElement.style="overflow: hidden !important;";
        document.body.style="overflow: hidden !important;";
        document.getElementsByClassName("inner_info")[0].style="display:block;";

        setTimeout(() => {
            document.getElementsByClassName("inner_info")[0].style="display:block; transform:translate(0,0);";
        }, 10);

    }else{
        document.getElementById("menu").style="";
        
        document.getElementsByClassName("inner_info")[0].style="display:block; transform:translate(-100%,0);";

        setTimeout(() => {
            document.documentElement.style="overflow-Y:auto !important;";
            document.body.style="overflow-Y:auto !important;";
            document.getElementsByClassName("inner_info")[0].style="";
            document.getElementsByClassName("info")[0].style="";
        }, 200);
    }

}

const func_1 = document.getElementById("menu_check").addEventListener("click",()=>{
    one_click();
});


function two_click (){
    if(!!document.getElementById("menu_check2").checked && ( window.innerWidth <=600 )){
        document.getElementsByClassName("mini_search")[0].style="transition:0.5s;"
        document.getElementsByClassName("right_header")[0].style="touch-action:none; transition:0.5s; transform:translate(105px,0px);";
        document.getElementsByClassName("mid_header")[0].style="transition:0.5s; transform:translate(0,-100px); ";
        document.getElementsByClassName("mini_search")[0].className="mini_search collap";        
        document.getElementsByClassName("mini_search")[0].getElementsByTagName("svg")[0].style="display:none;";
        document.getElementsByClassName("mini_search")[0].getElementsByTagName("svg")[1].style="";
        setTimeout(() => {
            document.getElementsByClassName("right_header")[0].style="";
            document.getElementsByClassName("sign")[0].style="display:none;"; 
            document.getElementsByClassName("sign")[1].style="display:none;"; 
            document.getElementsByClassName("mid_header")[0].style="";
            document.getElementsByClassName("mini_search")[0].className="mini_search collap2";
            document.getElementsByClassName("logo")[0].style="opacity:0;";
            document.getElementsByClassName("search")[0].style="display:flex !important; position:absolute; left:70px; width:calc(100% - 50px);";
            document.getElementsByClassName("input_text")[0].style="";
            document.getElementsByClassName("input_text")[0].getElementsByTagName("input")[0].style="width:100%;";
        }, 500);
    }else{
            document.getElementsByClassName("mini_search")[0].className="mini_search collap";
            document.getElementsByClassName("right_header")[0].style="";
            document.getElementsByClassName("sign")[0].style=""; 
            document.getElementsByClassName("sign")[1].style=""; 
            document.getElementsByClassName("mid_header")[0].style="";
            document.getElementsByClassName("logo")[0].style="";
            document.getElementsByClassName("mini_search")[0].getElementsByTagName("svg")[1].style="display:none;";
            document.getElementsByClassName("mini_search")[0].getElementsByTagName("svg")[0].style="";
            document.getElementsByClassName("search")[0].style="";
            document.getElementsByClassName("input_text")[0].style="";
            document.getElementsByClassName("input_text")[0].getElementsByTagName("input")[0].style="";
    }
}

const func_2 = document.getElementById("menu_check2").addEventListener("click",()=>{
    two_click();
});

var puppet = true;

window.onresize = ()=>{
    if(puppet && window.innerWidth>600){
        puppet=!puppet;
        two_click();
    }else{
        if(!puppet){
            puppet=!puppet;
            two_click();
        }
    }
};
