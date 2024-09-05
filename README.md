# RoomCraft: Your ideal room 🏠🚪 
 
La idea de este proyecto es recoger los datos de la pagina web de Ikea (https://www.ikea.com/es/es/), guardarlos en una base de datos y utilizarlos en la aplicación separados por secciones, necesarios para armar una habitación, como pueden ser:camas,escritorios,estanterías...
Y poder armar un presupuesto aproximado.

# Software utilizado 📝🐍🕷️<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Django_logo.svg/250px-Django_logo.svg.png" alt="Django Logo" width="80"/>

El proyecto estará compuesto por Python con el Framework Django para la parte web y en la parte de web scraping empecé utilizando Beautiful soap pero no me daba el output correspondiente ya que si observamos la página web de Ikea, hay demasiadas capas hasta llegar a los elementos deseados, por lo que decidí utilizar Scrapy.
Por otro lado,la base de datos en mongodb, ya que así además de practicar lo aprendido, puedo guardar los datos gratuitamente en Atlas.

# Outputs del Spider de Scrapy 🕷️ 🖥️


# Base de datos 🗂️
La primera idea que se me vino a la cabeza fue de hacer una sola tabla diferenciando los elementos por categora, pero debido a que tengo que guardar imagenes y la cantidad de elementos a guardar, esa idea que hacia inviable, por lo que decidí que cada categoría, o tipo de mueble tuviese una tabla.

# Interfaz de la aplicación 🎨
En este proyecto me he querido centrar en la parte de la recolección de datos y la subida de estos a la base de datos, por lo que el frontend de la apliación es bastante sencillo.
