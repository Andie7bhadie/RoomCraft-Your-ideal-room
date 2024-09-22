import pymongo
from itemadapter import ItemAdapter
    
class MongoPipeline: 
    nombre_coleccion= 'camas'
    #Vamos a utilizar el método init para conectarnos a mongo utilizando los siguientes parámetros uri de mongo y Nombre de la base de datos

    def __init__(self, mongo_uri, mongo_db):
            self.mongo_uri = mongo_uri 
            self.mongo_db = mongo_db

    @classmethod #Creamos una instancia del pipeline directamente desde el objeto crawler de Scrapy
    def from_crawler(cls, crawler):
        return cls(
            #el objeto crawler proporciona info sobre el proceso de rastreo
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )
    #Este inicia cuando se lanza la araña
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    #Y este finaliza la araña
    def close_spider(self, spider):
        self.client.close()
    #Cada vez que la araña saca un elemento se llama a este metodo y hace un insert
    def process_item(self, item, spider):
        self.db[self.nombre_coleccion].insert_one(ItemAdapter(item).asdict())
