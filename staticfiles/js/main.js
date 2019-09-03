// Exibição do menu mobile
let btnMenu = document.querySelector('#btnMobile');

function abrirMenuMobile() {
    let navMenu = document.querySelector('.menu-container');
    navMenu.classList.toggle('menu-ativo');
}

btnMenu.onclick = abrirMenuMobile;
// Fim código acima