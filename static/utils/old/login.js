function f(n){
    n = +n;
    switch(n){
        case 0 :
            document.getElementById("help1").style="";
            break;
        case 1 :
            document.getElementById("help2").style="";
            break;
        case 2 :
                document.getElementById("help1").style="display:none;";
                break;
        case 3 :
                document.getElementById("help2").style="display:none;";
                break;
    }
}