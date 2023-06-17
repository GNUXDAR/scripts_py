from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Path, HTTPException
from typing import Optional, List, Dict
from datetime import date

app = FastAPI()

products = []

class Product:
    def __init__(self, sku: str, name: str, price: float):
        self.sku = sku
        self.name = name
        self.price = price

# def create_products():
    # crear produstos con SKU
    # products.append(Product("SKU1", "Product 1", 10.00))
    # products.append(Product("SKU2", "Product 2", 20.00))
    # products.append(Product("SKU3", "Product 3", 30.00))
def create_products():
    # Crear productos con SKU y el formato JSON esperado
    product1 = {
        "sku": "SKU1",
        "offers": [
            {
                "id": 1,
                "price": 10,
                "stock": 10,
                "shipping_price": 15,
                "delivery_date": "2023-07-15",
                "can_be_refunded": True,
                "status": "new",
                "guarantee": True,
                "seller": {
                    "name": "Nike",
                    "qualification": 5,
                    "reviews_quantity": 10
                }
            }
        ]
    }

    product2 = {
        "sku": "SKU2",
        "offers": [
            {
                "id": 1,
                "price": 20,
                "stock": 20,
                "shipping_price": 25,
                "delivery_date": "2023-07-20",
                "can_be_refunded": True,
                "status": "new",
                "guarantee": True,
                "seller": {
                    "name": "Adidas",
                    "qualification": 4,
                    "reviews_quantity": 8
                }
            }
        ]
    }

    product3 = {
        "sku": "SKU3",
        "offers": [
            {
                "id": 1,
                "price": 30,
                "stock": 30,
                "shipping_price": 35,
                "delivery_date": "2023-07-25",
                "can_be_refunded": True,
                "status": "new",
                "guarantee": True,
                "seller": {
                    "name": "Puma",
                    "qualification": 3,
                    "reviews_quantity": 6
                }
            }
        ]
    }

    # Agregar los productos a la lista
    products.append(product1)
    products.append(product2)
    products.append(product3)

create_products()

class Book(BaseModel):
    title: str
    author: str
    page: int
    editor: Optional[str]

@app.get('/')
def index():
    return {"message": "Hello to tiendamia.com"}

# parametros variables
# @app.get('/book/{id}')
# def show_book(id: int):
#     return {"data": id}

# Request de un SKU
@app.get('/getAllSkuOffers/{sku}')
def get_all_sku_offers(sku: str):
    product = {
        "sku": sku,
        "offers": [
            {
                "id": 1, # integer
                "price": 10.00, # float
                "stock": 10,  # integer - Cantidad de ofertas disponible
                "shipping_price": 15.00, # float
                "delivery_date": date(2023, 7, 15), # date
                "can_be_refunded": True,  # boolean - Determina si un producto tiene devolución.
                "status": "new",  # string (new,used,renew)
                "guarantee": True,  # // boolean - Determina si un producto tiene garantía.
                "seller": {
                    "name": "Nike", # string
                    "qualification": 5,  # // integer - Range: 0-5 - Promedio de calificaciones.
                    "reviews_quantity": 10  # // integer - Cantidad de calificaciones tiene el seller.
                }
            },{
                "id": 2, # integer
                "price": 20.00, # float
                "stock": 20,  # integer - Cantidad de ofertas disponible
                "shipping_price": 25.00, # float
                "delivery_date": date(2023, 7, 15), # date
                "can_be_refunded": True,  # boolean - Determina si un producto tiene devolución.
                "status": "new",  # string (new,used,renew)
                "guarantee": True,  # // boolean - Determina si un producto tiene garantía.
                "seller": {
                    "name": "Adidas", # string
                    "qualification": 5,  # // integer - Range: 0-5 - Promedio de calificaciones.
                    "reviews_quantity": 10  # // integer - Cantidad de calificaciones tiene el seller.
                }
            }
        ]
    }
    return product

# save product
@app.get('/products')
def get_products():
    return products

# validate type
class Seller(BaseModel):
    name: str
    qualification: int
    reviews_quantity: int


class Offer(BaseModel):
    id: int
    price: float
    stock: int
    shipping_price: float
    delivery_date: date
    can_be_refunded: bool
    status: str
    guarantee: bool
    seller: Seller


class Product(BaseModel):
    sku: str
    offers: List[Offer]


@app.post("/createProduct")
def create_product(product: Product):
    # Aquí puedes acceder a los campos del producto y realizar las operaciones necesarias
    # Los datos ya están validados de acuerdo con la estructura definida en el modelo

    # Ejemplo: Acceder al SKU
    sku = product.sku

    # Ejemplo: Acceder a la primera oferta
    first_offer = product.offers[0]
    offer_id = first_offer.id
    offer_price = first_offer.price

    # Realizar la lógica para crear el producto o realizar otras operaciones

    # Devolver una respuesta de éxito
    return {"message": "Producto creado exitosamente"}

######################
# @app.post("/createProduct")
# def create_product(product: Dict[str, any]):
    # Aquí puedes realizar la lógica para crear el producto en tu base de datos u otro sistema
    # Verificar los datos recibidos y realizar las validaciones necesarias

    # Por ejemplo, si el SKU ya existe, puedes lanzar una excepción HTTP
    # if product_exists(product["sku"]):
    #     raise HTTPException(status_code=400, detail="El SKU ya existe")

    # Aquí puedes realizar las operaciones necesarias para crear el producto
    # Por ejemplo, guardar el producto en la base de datos

    # Devolver una respuesta de éxito
    # return {"message": "Producto creado exitosamente"}


# def product_exists(sku: str) -> bool:
    # Aquí puedes implementar la lógica para verificar si el producto ya existe en tu sistema
    # Por ejemplo, realizar una consulta a la base de datos y verificar si el SKU ya está registrado
    # Devuelve True si el producto existe, False de lo contrario
    # return False
