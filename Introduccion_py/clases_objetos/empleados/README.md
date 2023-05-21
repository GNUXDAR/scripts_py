# Funcionamiento de Clases
El archivo main.py actúa como el punto de entrada de la aplicación. Aquí es donde se crean instancias de las clases Empresa, Departamento y Empleado, y se realiza la interacción principal con esos objetos.

1. Importaciones: En el inicio del archivo, se importan las clases Empresa, Departamento y Empleado desde sus respectivos archivos.

2. Creación de objetos:

   * Se crea una instancia de la clase Empresa llamada empresa utilizando el constructor Empresa().
   * Se crean instancias de la clase Departamento y se asignan a variables como departamento1, departamento2, etc., utilizando el constructor Departamento().
   * Se crean instancias de la clase Empleado y se asignan a variables como empleado1, empleado2, etc., utilizando el constructor Empleado().
3. Asignación de empleados a departamentos: Los objetos de la clase Empleado creados anteriormente se asignan a los objetos de la clase Departamento correspondientes utilizando el método agregar_empleado() de la clase Departamento.

Asignación de departamentos a la empresa: Los objetos de la clase Departamento creados anteriormente se asignan al objeto de la clase Empresa utilizando una comprension de listas en la clase de empresa.

Obtención de información de la empresa: Se utiliza el método obtener_informacion() de la clase Empresa para obtener la información de la empresa, que incluye la información de todos los departamentos y sus respectivos empleados, mediante una concatenacion de clases.

Impresión de la información: Se utiliza la función print() para imprimir la información obtenida en el paso anterior.

En resumen, el archivo main.py crea instancias de las clases Empresa, Departamento y Empleado, las relaciona entre sí mediante los métodos entrelazados entre las clases y luego obtiene e imprime la información de la empresa utilizando el método obtener_informacion() de la clase Empresa.
