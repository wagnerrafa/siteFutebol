// Exibição do menu mobile
let btnMenu = document.querySelector('#btnMobile');

function abrirMenuMobile() {
    let navMenu = document.querySelector('.menu-container');
    navMenu.classList.toggle('menu-ativo');
}

btnMenu.onclick = abrirMenuMobile;
// Fim código acima
/* 
let num1 = 0;
function calcular() {
casa = document.getElementById("casa");
console.log(casa);
fora = document.getElementById("fora");
console.log(fora);
if (casa > fora){
num1=num1++
}
let elemResult = document.getElementById("resul");
    elemResult.textContent = num1++;
    alert(num1);
  }

   */