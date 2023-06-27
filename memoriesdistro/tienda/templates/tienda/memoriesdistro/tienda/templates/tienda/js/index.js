
{% comment %}
    carro de compra
{% endcomment %}

console.log("El archivo JS se ha cargado correctamente");

var array_productos = [];

if (localStorage.getItem('PRODUCTOS')) {
    array_productos = JSON.parse(localStorage.getItem('PRODUCTOS')) || [];
}

function comprar(id) {

    var producto = $('#producto-' + id);

    var p = {
        id: id,
        img: producto.data('img'),
        nombre: producto.data('nombre'),
        precio: producto.data('precio')
    };

    array_productos.push(p);

    console.log(array_productos);

    localStorage.setItem('PRODUCTOS', JSON.stringify(array_productos));

    llenar_carrtio();
}

function llenar_carrtio() {
    $('#carrito-producto').html('');   
    var texto = '';
    var total = 0;
    array_productos.forEach(producto => {
                // console.log(producto);
        texto = texto + `
                        <tr>
                        <td><img src="${producto.img}" width="50px"></td>
                        <td>${producto.nombre}</td>
                        <td>$${producto.precio}</td>
                        </tr>
                        `;

        total += producto.precio;
    });

    $('#carrito-producto').append(texto);         
    $('#carrito-precio').html(total);        
}


{% comment %}
    Validaciones
{% endcomment %}
function validarNombre(params) {

    var textoSalida = document.getElementById("fb-nombre");
    var nombre = params.value;

    if (nombre.length >= 3 && nombre.length <=20) {
        textoSalida.classList.remove("text-danger");
        textoSalida.classList.add("text-success");

        params.classList.remove("is-invalid");
        params.classList.add("is-valid");

    } else if (nombre.length>20){
        textoSalida.innerHTML = 'El nombre no puede exceder los 20 caracteres.';
        textoSalida.classList.remove("text-success");
        textoSalida.classList.add("text-danger");

        params.classList.remove("is-valid");
        params.classList.add("is-invalid");
    } else{
        textoSalida.innerHTML = 'El nombre es requerido y debe tener al menos 3 caracteres.';
        textoSalida.classList.remove("text-success");
        textoSalida.classList.add("text-danger");

        params.classList.remove("is-valid");
        params.classList.add("is-invalid");
    }
}

function validarApellido(params) {

    var textoSalida = document.getElementById("fb-apellido");
    var nombre = params.value;

    if (nombre.length >= 3 && nombre.length <=20) {
        textoSalida.classList.remove("text-danger");
        textoSalida.classList.add("text-success");

        params.classList.remove("is-invalid");
        params.classList.add("is-valid");

    } else if (nombre.length>20){
        textoSalida.innerHTML = 'El apellido no puede exceder los 20 caracteres.';
        textoSalida.classList.remove("text-success");
        textoSalida.classList.add("text-danger");

        params.classList.remove("is-valid");
        params.classList.add("is-invalid");
    } else{
        textoSalida.innerHTML = 'El apellido es requerido y debe tener al menos 3 caracteres.';
        textoSalida.classList.remove("text-success");
        textoSalida.classList.add("text-danger");

        params.classList.remove("is-valid");
        params.classList.add("is-invalid");
    }
}

function validarNumero(params) {

    var textoSalida = document.getElementById("fb-fono");
    var num = params.value;

    if (num.length >= 7 && num.length <=10) {
        textoSalida.classList.remove("text-danger");
        textoSalida.classList.add("text-success");

        params.classList.remove("is-invalid");
        params.classList.add("is-valid");

    } else if (num.length>10){
        textoSalida.innerHTML = 'El número teléfonico no puede exceder los 10 digitos.';
        textoSalida.classList.remove("text-success");
        textoSalida.classList.add("text-danger");

        params.classList.remove("is-valid");
        params.classList.add("is-invalid");
    } else{
        textoSalida.innerHTML = 'El número teléfonico es requerido y debe tener al menos 7 digitos.';
        textoSalida.classList.remove("text-success");
        textoSalida.classList.add("text-danger");

        params.classList.remove("is-valid");
        params.classList.add("is-invalid");
    }
}

// var expr= /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;
// $(document).ready(function(){
//     $("#bEnviar"),clic(function(){
//         var email = $("#email").val();

//         if(email =="" || !expr.test(email)){
//             $("#invalidEmail").fadeIn();
//             return false;
//         }else{
//             $("#invalidEmail").fadeOut();
            
//         }
//     });
// });

function validarContraseña(params) {

    var textoSalida = document.getElementById("fb-contraseña");
    var contra = params.value;

    if (contra.length >= 8 && contra.length <=15) {
        textoSalida.classList.remove("text-danger");
        textoSalida.classList.add("text-success");

        params.classList.remove("is-invalid");
        params.classList.add("is-valid");

    } else if (contra.length>15){
        textoSalida.innerHTML = 'La contraseña no puede exceder los 15 caracteres.';
        textoSalida.classList.remove("text-success");
        textoSalida.classList.add("text-danger");

        params.classList.remove("is-valid");
        params.classList.add("is-invalid");
    } else{
        textoSalida.innerHTML = 'La contraseña es requerido y debe tener al menos 8 digitos.';
        textoSalida.classList.remove("text-success");
        textoSalida.classList.add("text-danger");

        params.classList.remove("is-valid");
        params.classList.add("is-invalid");
    }
}