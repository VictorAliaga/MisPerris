// Guardamos el slider en una variable

var slider = $('#slider');

// Guardamos los botones en otras variables

var botonanterior = $('#boton-anterior');
var botonsiguiente = $('#boton-siguiente');

// Traspasamos la ultima imagen al principio, para que el slider sea infinito

$('#slider section:last').insertBefore('#slider section:first');


// posicionamos la primera imagen en el primer lugar del carrusel

slider.css('margin-left', '-'+100+'%');

// Funcion siguienteIMG para mover el carrusel a la derecha y posicionar la primera de las ultima

function siguienteIMG()
{
    slider.animate({
        marginLeft:'-'+200+'%'
    } ,700, function(){
        $('#slider section:first').insertAfter('#slider section:last');
        slider.css('margin-left','-'+100+'%');  
    });
}

// Funcion anteriorIMG para mover el carrusel a la izquierda y posicionar la ultima de las primera

function izquierdaIMG()
{
    slider.animate({
        marginLeft:0
    } ,700, function(){
        $('#slider section:last').insertBefore('#slider section:first');
        slider.css('margin-left','-'+100+'%');  
    });
}

// Si hacemos click en el boton siguiente se ejecutara la funcion siguienteIMG

botonsiguiente.on('click', function()
{
    siguienteIMG();
});

// Si hacemos click en el boton anterior se ejecutara la funcion anteriorIMG

botonanterior.on('click', function()
{
    izquierdaIMG();
});

// Movimiento Automatico del carrusel

function automatico()
{
    interval = setInterval(function(){
        siguienteIMG();
    }, 5000);
}

automatico();