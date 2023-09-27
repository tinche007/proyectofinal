Descripción del Proyecto
Página Web destinada a brindar la mayor información posible al viajero que quiera visitar distintos lugares turisticos de Argentina.

##¿Cómo se usa?

Ubicarse en la carpeta desde una terminal y ejecutar el servidor con el comando 'python manage.py runserver'
Ingresar al server brindado por IP.
Contará con 2 comandos para agregar a la url de IP para poder navegar:
/app1/
/admin
Distintas pantallas del sitio:
Desde "/app1/" podrá ingresar al menú principal del sitio donde contara con un resumen de la información que podrá encontrar dentro del site. Este menú le permitirá navegar e ingresar a (siempre agregando "/app1/" adelante):

/obligatorio/ - EL CUAL NOS OBLIGA A INICIAR SESIÓN PARA PODER NAVEGAR POR EL SITIO, SALVO POR LA SECCIÓN "/about/".

/registro/ - PARA REGISTRARSE EN EL SITIO.

/login/ - PARA INICIAR SESIÓN EN EL SITIO.

/logout/ - PARA CERRAR SESIÓN.

/perfil/ - PARA INGRESAR AL PERFIL DE LA CUENTA LOGUEADA.

/eliminarCuenta/ - PARA CONFIRMAR LA ELIMINACIÓN DE LA CUENTA.

/cuentaEliminada/ - CONFIRMACIÓN DE CUENTA ELIMINADA.

/provincias/ - PARA INGRESAR A LAS DISTINTAS PROVINCIAS CON LAS QUE CUENTA EL SITIO.

/opiniones/ - PARA INGRESAR A LA SECCIÓN DE OPINIONES DEL SITIO.

/about/ - PARA SABER SOBRE LA WEB Y SUS CREADORES.

/no_hay_pagina_aun/ - PANTALLA QUE MOSTRAMOS EN LAS SECCIONES QUE AÚN NO SE MOSTRARON.

Primeros pasos:
A fin de navegar por las secciones de la página web, se requiere que el usuario inicie sesión o se registre si no cuenta con un perfil creado. Una vez registrado, podrá iniciar sesión, que le permitirá navegar por las distintas pantallas mencionadas anteriormente.

¿Que se puede hacer en el sitio?
Los usuarios pueden realizar las siguientes accciones:

Iniciar sesión y navegar por las distintas provincias que poseen opiniones de sus puntos turisticos (actualmente nos encontramos con 3 provincias en funcionamiento, 6 construyendose y las restantes serán agregadas en un futuro).
Editar el perfil de Usuario y su avatar.
Cambiar la contraseña de Usuario.
Cerrar Sesión.
Nota: La opción de editar y/o eliminar el comentario/opinion propio, solo se permite al usuario dueño de la opinión. En el caso de eliminar cualquier comentario/opinion, solo se permite a los usuarios admin.

##/admin Allí podrán loguearse e ingresar como administrador, donde tendrán permisos para:

Acceder a paneles de administrador
Crear nuevos usuarios
Crear nuevos datos en la BBDD
Usuarios
Los superusuarios son los siguientes: #Usuario 1:

Usuario: admin
Contraseña: 123456
#Usuario 2:

Usuario: admin3
Contraseña: 123456
Pruebas Realizadas
Ver archivo titulado "Tests Proyecto Argentravel Python.xlsx".
