
function one_click() {
    if(!!document.getElementById("menu_check").checked){
        document.getElementById("menu").style="background:#f8f8f8; box-shadow:0 0 6px 0 rgba(0,0,0,0.23);";
        document.getElementsByClassName("info")[0].style="display:block; position:absolute; top:72px; background:rgba(20,20,20,0.5);";
        document.getElementsByClassName("container")[0].style="overflow: hidden; width:calc(100% - 10px);";
        document.getElementsByClassName("inner_info")[0].style="display:block;";

        setTimeout(() => {
            document.getElementsByClassName("inner_info")[0].style="display:block; transform:translate(0,0);";
        }, 10);

    }else{
        document.getElementById("menu").style="";
        
        document.getElementsByClassName("inner_info")[0].style="display:block; transform:translate(-100%,0);";

        setTimeout(() => {
            document.getElementsByClassName("container")[0].style="";
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
    f();
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


//Slide : This function is for the slideshow

let slide = 0;


let interval = setInterval(() => {
    document.getElementsByClassName("movement")[0].style="pointer-events:none;";  
    set(1,-1);
}, 5000);


document.getElementsByClassName("pre")[0].onclick = function(){
    document.getElementsByClassName("movement")[0].style="pointer-events:none;";
    if(!!interval){
        clearInterval(interval);
    }
    interval = setInterval(() => {
        document.getElementsByClassName("movement")[0].style="pointer-events:none;";
        set(1,-1);
    }, 5000);
    set(0,-1);   
}
document.getElementsByClassName("next")[0].onclick = function(){
    document.getElementsByClassName("movement")[0].style="pointer-events:none;";
    if(!!interval){
        clearInterval(interval);
    }
    
    interval = setInterval(() => {
        document.getElementsByClassName("movement")[0].style="pointer-events:none;";
        set(1,-1);
    }, 5000);

    set(1,-1);   
}

function set(k,r) {
    let p = slide;
    let m = document.getElementsByClassName("dir")[0].getElementsByTagName("div");
    let n = document.getElementsByClassName("now");
    let l = n.length;
    if((r-1)==(slide)){
        return;
    }
    (k == 1) ? ( slide<(l-1) ) ? slide++ : slide=0 : ( slide!=0 ) ? slide-- : slide=l-1  ;

    if(r>0){
        
    if(!!interval){
        clearInterval(interval);
    }
    interval = setInterval(() => {
        document.getElementsByClassName("movement")[0].style="pointer-events:none;";
        set(1,-1);
    }, 5000);
        slide = r-1;     
    }
        m[(p*2)+1].setAttribute("is","0");
        m[(slide*2)+1].setAttribute("is","1");
        slider(slide , p , n);

}

function slider(s, p , n ){
    
    var d = document.getElementsByClassName("container")[0].scrollTop ;
    
    n[s].setAttribute("val","");
    n[p].setAttribute("zero","0");

    setTimeout(() => {
        n[s].setAttribute("zero","");        
        n[p].setAttribute("val","hid");  
        document.getElementsByClassName("movement")[0].style="";
        f();
        if(d<500) document.getElementsByClassName("container")[0].scrollTo(0,d);        
    }, 150);
}

function roll(r){
    set(0,r);
}