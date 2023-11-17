# Tu Habi

Este proyecto consiste de dos partes principales: frontend y backend. Además de esto el proyecto se trabjará dockerizado.

## Frontend

Para el frontend del proyecto se trabajará con las siguientes tecnologías:

- React
- Next
- Tailwind

Para el desarrollo se realizarán unos bocetos (wireframe), mediante los cuales se identifican módulos y componentes necesarios.Una vez se tienen estos, se procede a su implementación. La implementación de los módulos/componentes implica también la implementación de los servicios para la comunicación con el back.

## Backend

Para el frontend del proyecto se trabajará con las siguientes tecnologías:

- Django
- Django Rest Framework
- Django environ
- Django Cors
- Psycopg

Para el desarrollo se realizará el esquema de la arquitectura y la comunicación de los componentes. Luego de esto se procede a implementar uno a uno de los componentes haciendo uso de la metoldología TDD para ello. Cuando se tengan implementados los servicios, se procederá a crear una colección de postman para la prueba y monitoreo de estos.

## Dudas de implementación

### Primer duda

En los requerimientos se menciona que no se pueden modificar y/o alterar los registros de la base de datos. Dada la estrucura que esta presenta, se considera necesario, en pro de la velocidad en las consultas y de la carga hacia esta, realizar unos cambios en la estructura de la misma. Para esto, se hace un backup de la base de datos y se realiza la restauración en una base de datos en el ambiente de desarrollo (Docker). Sin embargo, la aplicación se probará con la base de datos provista, de tal manera que se asegure la compatibilidad con BD remotas.

### Segunda duda

Algunas de los requerimientos estipulados son omitidos, dado que no se entiende lo que se pide, estos son:

- El primer requerimiento debe ser funcional.
- En el primer requerimiento, crea un archivo JSON con datos de filtro esperados del
frontend.
- El segundo requerimiento es conceptual, extiende el modelo con un diagrama ER y
código SQL.

### Tercera duda

Para el cumplimiento de los requisitos de 'Me gusta' se ha optado por la siguiente aproximación: cada vez que un usuario agregue una propiedad a sus 'Me gusta', esta se añadirá tanto en el local storage como en la BD (a través de un request al Backend). Cuando el usuario se identique en la plataforma, se pedrirá el listado de las propiedades que el usuario ha marcado como 'Me gusta' y se cargarán en el local storage. Esta aproximación permite que esta funcionalidad sea multiplataforma (o multidispositivo) de manera asíncrona, es decir que NO soportará la navegación de un mismo usuario en más de un dispositivo y/o plataforma a la vez.

### Cuarta duda

Este apartado más que una duda es una aclaración a la aproximación de desarrollo. Aunque se entiende la importancia de adaptar y trabajar con un buen flujo de git (manejo de ramas, PR, estrategias de merge, y demás), en este proyecto se trabajará con una única rama (develop), por dos razones:

- Es un desarrollo a cargo de una sola persona.
- No es proyecto de alta complejidad y su desarrollo es secuencial, por lo que todo se puede abordar con una sola rama.

Sin embargo, sí se opta por manejar un [estándar para los commits](https://www.conventionalcommits.org/en/v1.0.0/). [En esta página](https://nitayneeman.com/posts/understanding-semantic-commit-messages-using-git-and-angular/) hay más detalles de los tipos de commits.