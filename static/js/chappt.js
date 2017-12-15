$(document).ready(function(){
    // the "href" attribute of the modal trigger must specify the modal ID that wants to be triggered
    $('.modal').modal();
    
    //funcion para insertar en los mesajes los distintos emojis
    $('.emoticono').click( function() {
        //seleccionamos el texto del mensaje
       $('#id_texto').val($('#id_texto').val() + ' '+this.id);
        
    });
    
    
    
  });