function fun_1(){
    x = document.querySelector(".navbar")
    x.style.backgroundColor="rgb(245, 244, 244)"
}

function datselect(){
    var d1 = document.getElementById("Sportselect");
    var d2 = document.getElementById("Bookselect");
    var d3 = document.getElementById("Misciselect");
    var d4 = document.getElementById("Movieselect");
    var displ1 = d1.options[d1.selectedIndex].text;
    var displ2 = d2.options[d2.selectedIndex].text;
    var displ3 = d3.options[d3.selectedIndex].text;
    var displ4 = d4.options[d4.selectedIndex].text;
    var interests = [displ1,displ2,displ3,displ4];
    console.log(interests) 
}