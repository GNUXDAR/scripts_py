# Conexion a endpoints de una API REst

# Steps
$ cd CRUD  
$ python3 -m venv .venv  
$ . .venv/bin/activate ó source .venv/bin/activate  
$ python3 -m pip install flask flask_cors  

# show
$ curl http://localhost:5000/products  

# POST  
En la terminal, ejecuta el siguiente comando para agregar un producto a la lista. Esto será una solicitud POST a la cual pasarás el parámetro del producto como un JSON.  

$ curl -X POST -H "Content-Type: application/json" \
    -d '{"id": 145, "name": "Pen", "price": 2.5}' \
    http://localhost:5000/products  

    curl http://localhost:5000/products/145  

## POSTMAN
To send input as JSON, choose raw->body->JSON.

{  
    "id":146,  
    "name":"Laptop Bag",  
    "price":45.00  
}  

# GET
http://localhost:5000/products 

# PUT
http://127.0.0.1:5000/products/146  

{
    "price":42.00
}

# DELETE
http://127.0.0.1:5000/products/146