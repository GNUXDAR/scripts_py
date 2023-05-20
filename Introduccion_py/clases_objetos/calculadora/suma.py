class Calculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, num):
        self.resultado += num

    def restar(self, num):
        self.resultado -= num

    def multiplicar(self, num):
        self.resultado *= num

    def dividir(self, num):
        self.resultado /= num


# Ejemplo de uso
calculadora = Calculadora()
calculadora.sumar(5)
calculadora.multiplicar(3)
calculadora.restar(2)
calculadora.dividir(4)

print(calculadora.resultado)  # Imprime: 3.25