class calculadora:

    def sumar(self, a, b):
        return a + b
    
    def restar(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre 0")
        return a / b
    
    def potencia(self, base, exponente):
        return base ** exponente
    

if __name__ == "__main__":
    
    calc = calculadora()

    print("2 + 3 =", calc.sumar(2, 3))
    print("10 - 4 =", calc.restar(10, 4))
    print("3 x 5 =", calc.multiplicar(3, 5))
    print("10 / 2 =", calc.dividir(10, 2))
