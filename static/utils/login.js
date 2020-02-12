function f(n){
    n = +n;
    switch(n){
        case 0 :
            document.getElementById("help1").style="";
            document.getElementById("help2").style="display:none;";
            break;
        case 1 :
            document.getElementById("help2").style="";
            document.getElementById("help1").style="display:none;";
            break;
        case 2 :
        case 3 :
	    document.getElementById("help1").style="display:none;";
            document.getElementById("help2").style="display:none;";
            break;
    }
}
	
function f2(d){
	d=d+"";
	var k = document.getElementById(d);
	var g = k.value; 
	if(g){k.setAttribute("hastext","");}else{k.removeAttribute("hastext");}
}