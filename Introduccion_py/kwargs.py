#es obligatorio el nombre del parametro cuando se trabaje con kwargs
def get_product(**datos):
    print(datos)

get_product(id="id", name="shoes", sku="nike001")

## acceder a los parametros en la funcion
def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="01", name="shoes", sku="nike001")
