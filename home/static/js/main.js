// Exibição do menu mobile
let btnMenu = document.querySelector('#btnMobile');

function abrirMenuMobile() {
    let navMenu = document.querySelector('.menu-container');
    navMenu.classList.toggle('menu-ativo');
}

btnMenu.onclick = abrirMenuMobile;
// Fim código acima


  /*document.getElementById ("mm1").addEventListener ("click", myFunction, false); function myFunction() { document.getElementById("historico").style.backgroundColor = "red"; } */


var imageCount = 0;
var currentImage = 0;
var images = new Array();
 
images[0] = 'https://res.cloudinary.com/wagner/image/upload/v1568229227/foto1_b2whz1.jpg';
images[1] = 'https://res.cloudinary.com/wagner/image/upload/v1568229227/foto2_x1ngon.jpg';
images[2] = 'https://res.cloudinary.com/wagner/image/upload/v1568229227/foto3_gxawxf.jpg';

 
var preLoadImages = new Array();
for (var i = 0; i < images.length; i++)
{
   if (images[i] == "")
      break;
 
   preLoadImages[i] = new Image();
   preLoadImages[i].src = images[i];
   imageCount++;
}
 
function startSlideShow()
{
   if (document.body && imageCount > 0)
   {
      document.getElementById("historico").style.backgroundImage = "url("+images[currentImage]+")";    
      document.getElementById("historico").style.backgroundAttachment = "fixed";
      document.getElementById("historico").style.backgroundRepeat = "no-repeat";
      document.getElementById("historico").style.backgroundsize = "cover";

 
      currentImage = currentImage + 1;
      if (currentImage > (imageCount-1))
      { 
         currentImage = 0;
      }
      setTimeout('startSlideShow()', 4000);
   }
}
startSlideShow();
  
  