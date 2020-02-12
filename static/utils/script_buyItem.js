function d(){
    var d=document;
    var v=false;
    d.addEventListener("mouseover",function(){
        try {
            var k = event.target.parentNode;
            var m = k.parentNode.parentNode.id;
            var lm = event.target; 
            var n = lm.parentNode.parentNode.id;
        }catch(e) {
            return;
        }
        if(m=="itm_pre" || n=="itm_pre"){
            if(n=="itm_pre"){
                k=lm;
            }
            var a = d.getElementsByClassName("itm_image");
            var l = a.length;
            try {
                for(var i in d.getElementsByClassName("itm_pre_div")){d.getElementsByClassName("itm_pre_div")[i].removeAttribute("open");}
            }catch(e){}
            try{ if(!(k.getAttribute("open"))) k.setAttribute("open","");}catch(e){}
            var n = +k.getAttribute("no");
            n--;
            for(var i in a){
                try{
                    if(a[i].getAttribute("show")==""){
                        a[i].removeAttribute("show");
                        a[i].setAttribute("hide","");
                    }
                }catch(e){}
            }
            try {
                a[n].setAttribute("show","");
                a[n].removeAttribute("hide");
            }catch(e){}
        }
        try{
            k=event.target.id;
            if(k=="itm_zoom_pst"){
                v=true;
            }
        }catch(e){alert(e);}

    });
    d.addEventListener("mousemove",function(){
        var kl = event.target;
        if(kl.id=="itm_zoom_pst"){
            var x = Math.min(Math.max(0,event.offsetX),420);
            var y = Math.min(Math.max(0,event.offsetY),420);
            // console.log(x+" "+y);
            var k = d.getElementById('item_menubar_div').getElementsByTagName("div");
            var l = d.getElementById('item_menubar_div').getAttribute("no");
            l=+l;
            l<=0?l=1:l--;
            k[l].getElementsByTagName("img")[0].style=" width:1000px; height:1000px; position:relative; left:"+(x*-580/420)+"px; top:"+(y*-580/420)+"px; ";
        }
    });
    d.addEventListener("click",function(){
        if((event.target.tagName=="SPAN" && event.target.parentNode.parentNode.id=="itm_preview")||(event.target.id=="itm_preview")||(event.target.parentNode.id=="itm_preview")){
            d.getElementById('item_menubar').style='';
            d.body.style="overflow:hidden;";
            document.getElementsByClassName('container')[0].scrollTop=0;
        }
        if((event.target.tagName=="SPAN" && event.target.parentNode.parentNode.id=="itm_zoom_pre")||(event.target.id=="itm_zoom_pre")||(event.target.parentNode.id=="itm_zoom_pre")){
            var k = d.getElementById('item_menubar_div').getElementsByTagName("div");
            var l = d.getElementById('item_menubar_div').getAttribute("no");
            l=+l;
            l<=0?l=1:l--;
            var x = Math.min(Math.max(0,event.offsetX),420);
            var y = Math.min(Math.max(0,event.offsetY),420);
            k[l].style="";
            k[l].getElementsByTagName("img")[0].style=" width:1000px; height:1000px; position:relative; left:"+(x*-580/420)+"px; top:"+(y*-580/420)+"px; ";
            d.getElementById("itm_zoom_pre").removeAttribute("open");
            d.getElementById("itm_zoom_pst").setAttribute("open","");

            // k[l].getElementsByTagName("img")[0].style="transition:all 0.25s ease-in; width:1000px; height:1000px; position:relative; top:0px; left:0px; ";
            
        }
        var k = event.target.parentNode.id;
        if(k=="more"){
            d.getElementById("itm_pre").setAttribute("open","");
            d.getElementById("itm_pre_scr").setAttribute("open","");
        }
        k = event.target.className;
        try{if(k.includes(" nxt")){
            {d.getElementById("itm_pre").setAttribute("track","2");d.getElementById("itm_pre_scr").setAttribute("track","2");}
        }else if(k.includes(" pre")){d.getElementById("itm_pre").setAttribute("track","1");d.getElementById("itm_pre_scr").setAttribute("track","1");}}catch(e){}
        kl = event.target;
        if(kl.id=="itm_zoom_pst"){
            var k = d.getElementById('item_menubar_div').getElementsByTagName("div");
            var l = d.getElementById('item_menubar_div').getAttribute("no");
            l=+l;
            l<=0?l=1:l--;
            k[l].getElementsByTagName("img")[0].style="";
            kl.removeAttribute("open");
            k[l].style="position;relative; top:50%; left:50%; transform:translateX(-50%) translateY(-50%);"
            d.getElementById("itm_zoom_pre").setAttribute("open","");
        }
    });
}
d();

function fjk(n){
    try{n=n+"";
    var d = document;
    var kl = d.getElementById("itm_zoom_pst");
    var k = d.getElementById('item_menubar_div').getElementsByTagName("div");
    var l = d.getElementById('item_menubar_div').getAttribute("no");
    l=+l;
    l<=0?l=1:l--;
    k[l].getElementsByTagName("img")[0].style="";
    k[l].style="position;relative; top:50%; left:50%; transform:translateX(-50%) translateY(-50%);"
    kl.removeAttribute("open");
    d.getElementById("itm_zoom_pre").setAttribute("open","");
    d.getElementById("item_menubar_div").setAttribute("no",n);}catch(e){return;}
    try{d.getElementsByClassName("mnubar_itm2")[l].removeAttribute("open");
    d.getElementsByClassName("mnubar_itm2")[n-1].setAttribute("open","");}catch(e){}
}