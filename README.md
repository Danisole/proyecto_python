## Tercera Pre entrega de Python - Django :clipboard:

##### La tercera pre entrega del curso de python de CoderHouse dictado por el prof. Franco Gabriel Di Martino, por el tutor Enzo Martin Zotti y la breve pero no menos importante participacion de porf. Norman Beltran. Esta nueva entrega tiene como tema principal trabajar con una plantilla de frontend y enlazarla con backend proveniente de python con django. Las consignas fueron las siguientes

#### Objetivo 
##### Desarrollar una WEB Django con patrón MVT subida a Github.

#### Consigna

##### Se debe entregar

- Link de GitHub con el proyecto totalmente subido a la plataforma.
- Proyecto Web Django con patrón MVT que incluya:
        1. Herencia de HTML.
        2. Por lo menos 3 clases en models.
        3. Un formulario para insertar datos a todas las clases de tu models.
        4. Un formulario para buscar algo en la BD
        5. Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.

#### Formato  

##### Link al repositorio de GitHub con el nombre “Tercera pre-entrega+Apellido”.

#### Pasos :gear:

 ##### 1. Para la confección de este entregable se realizo un modelo de la plantilla a usar en papel para luego codificarla con Bootstrap y Css.

 ##### 2. Se uso el editor de codigo Visual Studio Code donde se trabajo con la extension Python que podemos encontrar en la galeria de extensiones.

 ##### 3. Tambien se instalo Django en su ultima version para poder llevar a cabo el proyecto con este Framework.

 ##### 4. Se inicio un nuevo proyecto en django creando una carpeta, la cual vamos a abrir desde Visual Studio Code y en la consola escribimos el comando django-admin startproject + nombre de nuestro proyecto


 ##### 5. Luego tipeamos" python manage.py migrate" y veificamos que todo este en orden con el comando "python manage.py runserver" al correr django veremos una pagina de inicio proporcionada por el framework.

##### 6. Funcionando django vamos a crear nuestro primer archivo "views.py",  Vamos a nuestro archivo views.py, e importamos los elementos de un Response: 
from django.http import HttpResponse

##### 7. Con todos estos pasos podemos coemnzar a trabajar en nuestra pagina.
 ##### 8. Otro paso para la creacion de es bloq fue crear la app AppCoder donde se alojaron tantos los template como toda la informacion.

 ##### 9. Para este blog se crearon una pagina de inicio y 3 formularios para el correcto manejop de la informacion que se aloja en SQL lite.

 ###### Todo esto y mas podras ver en mi [GitHub](https://github.com/Danisole/) 


