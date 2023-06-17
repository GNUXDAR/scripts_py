# Prueba tecnica
Esta es un ejemplo de una prueba tecnica...
# Request Example
curl --location --request GET '{provider_host}/getAllSkuOffers/:sku'  
curl --location --request GET 'http://127.0.0.1:8000/getAllSkuOffers/23'


# Response Status:
200 OK Successful response  

# Successful Response Body:
{
    "sku": "xxx", //string
    "offers": [
        {
            "id": 0, // integer
            "price": 00.00, // decimal
            "stock": 0, // integer - Cantidad de ofertas disponible
            "shipping_price": 0.00, // decimal
            "delivery_date": 2023-05-27, // date
            "can_be_refunded": true, // boolean - Determina si un producto
            tiene devolución.
            "status": "new", // string (new,used,renew)
            "guarantee": true, // boolean - Determina si un producto tiene
            garantía.
            "seller": {
                "name": "xxxx", // string
                "qualification": 0, // integer - Range: 0-5 - Promedio de
                calificaciones.
                "reviews_quantity": 0, // integer - Cantidad de calificaciones
                tiene el seller.
            }
        },
    ]
}

# Error Response Body:

{
"error": "Reason"//string -> Descripción del error
}


# Fast API
[FastAPI](https://fastapi.tiangolo.com/)  

# env
$ cd my-project  
$ python3 -m venv .venv  
$ . .venv/bin/activate ó source .venv/bin/activate  

# Install
$ pip install fastapi  
$ pip install uvicorn  

# Run
$ uvicorn main:app --reload  
open in browser: http://127.0.0.1:8000  

# Docs of API
http://127.0.0.1:8000/docs  
http://127.0.0.1:8000/redoc  

# Note  
* This is API  
* module in Magento2 in link [Modulo - GetProvider](https://github.com/GNUXDAR/Actecnology/tree/main/GetProvider)