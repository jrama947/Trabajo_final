# Trabajo_final
Se implementó web de información de destinos de viaje, en la cual se puede acceder a diferentes secciones y de cada una de ellas siempre volver al inicio. Además, es posible mediante formularios agregar registros a la base de datos y consultarlos.

El proyecto "Tercera_pre_entrega_Rama" incluye:

Base de datos 'db.sqlite3' donde se alojan las tablas Destinos, Atracciones, Alojamientos, Actividades y users creados en la aplicación 'AppTerEnt'.
Archivo settings.py donde se instala la aplicación'AppTerEnt'.
Archivo urls.py donde se definieron la url 'admin/' que da acceso a la administración del sitio; url 'app/' para incluir todas las urls definidas en 'AppTerEnt'.

La apliación 'AppTerEnt' incluye:

Archivo 'views.py' donde se definen las vistas de las diferentes pantallas de la web: Inicio, Destinos, Atracciones, Actividades, Alojamientos, formulario y buscar. Estas views hacen referencia a diferentes html donde están definidos los diseños de cada pantalla. Cada view cuenta con su respectivo html bajo la misma denominación.

Archivo 'urls.py' donde se definen las diferentes url que cuenta la web. Existe una url por cada view definida.

Archivo 'models.py' donde se definieron los modelos para la base de datos. Los modelos presentan la siguiente estructura: Destinos city - Char country Char category - Char popularity - Int

Actividades name - Char difficulty - Char duration - Int

Alojamientos name - Char city - Char country - Char adress - Char stars - Int

Atracciones name - Char city - Char category - Int

Archivo 'forms.py' donde se definieron la estructura de los diferentes modelos (Formulario y Buscar) tanto para el ingreso de datos a la BD (clase Formulario) como para la búsqueda de datos (clase Buscar).

Archivo 'admin.py' donde se registraron todos los modelos creados, de manera de habilitar el acceso del administrador a los mismos.

Carpeta 'AppTerEnt' dentro de 'templates' donde se definieron todos los html a utilizar para las vistas. Se definió un html base denominado 'tempbase' donde se incluye el diseño que se compartirá por todas las demás vistas de la web. Este diseño fue heredado por el resto de los html de manera tal de evitar repetición de codificación. Se definió como diseño "fijo" de la web el head, nav class y el footer. En el resto de los html se definió el diseño propio de cada vista, modificando los textos e imágenes a mostrar en cada una de ellas. Las imágenes se almacenan dentro de la carpeta ´static/AppTerEnt/assets/img/.

Carpeta 'migrations' donde se guardan archivos .py con las diferentes migraciones de los modelos a la base de datos.

Pasos para validación:

Levantar proyecto en VS Code.
Ejecutar en consola python manage.py runserver para levantar un servidor.
Acceder al servidor levantado
Agregar a la url del servidor /app/welcome para visitar la página de bienvenida. Desde esta pantalla se podrá ingresar y/o registrar un nuevo usuario, además de visitar una sección "about me".
Mientras no exists usuario logueado haciendo click en 'Travel MyB' volvemos a la página de bienvenida.
Una vez ingresado un usuario correctamente, se visualizará la página de inicio con mayor información de bienvenida, así como nuevas opciones en la barra de navegación: las diferentes secciones del blog y también la opción de desloguearse y editar datos del usuario.
Desde la página de inicio se puede acceder a las diferentes secciones haciendo click en los nombres de la barra superior de la pantalla.
Haciendo click en 'Travel MyB' volvemos a la página de inicio desde cualquier pantalla.
Agregando a la url del servidor /admin/ accedemos al sitio administrador. User: jrama Pass: espartero1427
