import scrapy
from ikea_scrap.pipelines import IkeaScrapPipeline

class IkeaproductSpider(scrapy.Spider):
    name = "Productos"
    #url principal
    start_urls = ['https://www.ikea.com/es/es/cat/camas-bm003/',
                'https://www.ikea.com/es/es/cat/escritorios-mesas-ordenador-20649/',
                'https://www.ikea.com/es/es/cat/mesitas-noche-20656/',
                'https://www.ikea.com/es/es/cat/armarios-19053/'
                ]

    def parse(self, response):
        # Seleccionamos todos los divs bajo //*[@id="product-list"]/div[2]
        product_divs = response.xpath('//*[@id="product-list"]/div[2]/div')

        # Iterar sobre cada div encontrado, es decir, cada producto
        for index, product_div in enumerate(product_divs, start=1):
            # Construir el XPath específico para cada div
            '''En este caso,algunos elementos como el precio o el titulo ikea ya los pone como atributos de 
            las etiquetas'''
            producto = f'//*[@id="product-list"]/div[2]/div[{index}]//@data-product-name'
            precio = f'//*[@id="product-list"]/div[2]/div[{index}]//@data-price'
            refid = f'//*[@id="product-list"]/div[2]/div[{index}]//@data-ref-id'
            description = f'(//span[@class="plp-price-module__description"])[{index}]/text()'
            imagen=f'//*[@id="product-list"]/div[2]/div[{index}]/div/div[2]/a[contains(@href, "https")]/img[1]/@src'

        # Extraer el atributo data-product-name usando el XPath construido
            product_name = response.xpath(producto).get()
            product_price = response.xpath(precio).get()
            product_refid = response.xpath(refid).get()
            product_description = response.xpath(description).get()
            product_imagen = response.xpath(imagen).get()

            # 'MONTAMOS' cada producto con lo encontrado.
            if product_name:
                yield {
                    'data-product-name': product_name,
                    'data-price': product_price,
                    'data-pref-id': product_refid,
                    'data-description': product_description,
                    'data-imagen': product_imagen
                }

        # Verificar si existe una siguiente página y seguirla hasta que no haya más páginas.
        next_page = response.xpath('//a[contains(@href, "https") and contains(@class, "plp-btn plp-btn--small plp-btn--secondary")][last()]/@href')
        if next_page:
            yield response.follow(next_page, callback=self.parse)
