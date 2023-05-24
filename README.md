# API

Descripción Proyecto

Consideraciones

No es necesario completar todo el examen, según el avance se evaluará el
conocimiento de la persona.
 El examen se presenta en un repositorio publico con su respectivo Docker-
Compose para poder realizar la ejecución y validación.
 Se puede considerar modificaciones que se consideren como mejoras y se detallen
en un readme.

1. Generar un Rest API (Python-Flask) con al menos 3 controladores (CRUD), utilizando
una arquitectura hexagonal y que respete los principios SOLID.
2. El API antes mencionada debe contar con al menos 4 tablas, algunas de ellas deben
estar relacionadas entre ellas. Esto puede ser realizado con un ORM o sin el mismo lo
importante es que los métodos deberán ser consumidos sin problemas.
3. 1 de los endpoint de los 3 controladores generados debe consultar con una tabla de al
menos 2MM de registros, debe contar con paginación.
4. Debe contar con 1 patrón de repositorio genérico con al menos 1 de 2 ORM que se
utilizan actualmente.
5. Generar 1 2da API en Python (Python-Flask) que envíe información a la 1ra API puede
ser por cualquier cosa.
6. La comunicación entre las API debe ser por 2 medios, a través de un broker (cualquiera
a su preferencia, Kafka, RabbitMQ) y vía HTTP (circuit break).
7. Todo esto debe estar en 1 contenedor y subido a un repositorio público de GitHub.

# Arquitectura del proyecto

- Version python: Python 3.10.6
- Entorno virtual: virtualenv 20.16.3
- Nombre del Proyecto: votaciones
  - psycopg2 2.9.6 --> base de datos postgres
  - Archivo requirements.txt: Contenido de las librerias utilizadas

Nota: 
* El proyecto se crea con una base de datos POSTGRES, nombre de la base de datos "apimok".
* Se crea una carpeta con nombre mermaiddb, la cual contiene el MER y el DER, de la base de datos
* se debe asignar una contraseña al archivo config.py para la base de datos

urls api


1. http://localhost:5000/users

{
  "name": "John Doe",
  "email": "john@example.com"
}

2. http://localhost:5000/suppliers
{
  "name": "example",
  "address": "example",
  "telephone": "00000"
}


3. http://localhost:5000/products

{
  "name": "Nombre del producto",
  "price": 9.99,
  "supplier_id": 1
}

4. http://localhost:5000/customers

{
  "name": "John Doe",
  "email": "john@gmail.com"
}

ejemplo 

![image](https://github.com/edimoredev/mok_api_project/assets/125479887/50eea2c8-b757-4f68-8678-a3173c4efc97)

DOCKER 

* Se crea los archivos docker-compose.yml y dockerfile, con su respectiva configuración

![image](https://github.com/edimoredev/mok_api_project/assets/125479887/d78b7f05-acab-48fe-b80c-6a070d78755b)

* se realiza el levantamiento del contenedor  docker compose "docker compose up"

![image](https://github.com/edimoredev/mok_api_project/assets/125479887/d3808f53-1a5f-4841-bd31-a736107770a1)

* Arranque del servicio 

![image](https://github.com/edimoredev/mok_api_project/assets/125479887/01380cf2-194d-4751-bb1d-2a54fd5398d8)

* comprobación del servicio

![image](https://github.com/edimoredev/mok_api_project/assets/125479887/3670ec34-da55-42b0-a347-84a3011b3084)

* insertar un usuario

![image](https://github.com/edimoredev/mok_api_project/assets/125479887/a588ac0e-b4d0-4e84-82e7-805b9e5e4cb2)

* Agregando una proveedora

![image](https://github.com/edimoredev/mok_api_project/assets/125479887/2afa61df-3a91-4e82-bc46-1cb12f0b8087)

* agregando un producto

![image](https://github.com/edimoredev/mok_api_project/assets/125479887/70604c76-ed42-4149-a7ac-2d42db63526d)

* consultando los productos

![image](https://github.com/edimoredev/mok_api_project/assets/125479887/3f8e8988-3c9c-47a8-b622-c72f3a177c07)







