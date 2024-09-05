# RoomCraft: Your ideal room 
La idea de este proyecto es recoger los datos de la pagina web de Ikea (https://www.ikea.com/es/es/), guardarlos en una base de datos y utilizarlos enla aplicación separados por secciones, necesarios para armar una habitación, como pueden ser:camas,escritorios,estanterías...
Y poder armar un presupuesto aproximado.

# Software utilizado 📝
El proyecto estará compuesto por Python con el Framework Django para la parte web y en la parte de web scraping empecé utilizando Beautiful soap pero no me daba el output correspondiente ya que si observamos la página web de Ikea, hay demasiadas capas hasta llegar a los elementos deseados, por lo que decidí utilizar Scrapy.
Por otro lado,la base de datos en sql, cada elemento de la habitación tendrá su propia tabla en la base de datos.

