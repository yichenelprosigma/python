# clase Calculadora
# ¿Qué atributos necesitamos?
# x,y
# ¿Qué métodos necesitamos?
# +,-,*,/, modulo , potencia

class Calculator:
    def __init__(self):
        self.result=0    # inicializar resultado=0
        self.history=[]  # una lista para guardar los resultados
    def add(self, x, y):
        self.result= x + y
        self.history.append(self.result)
        return self.result
        

    def subtract (self, x, y):
        self.result = x - y
        self.history.append(self.result)
        return self.result

    def multiply(self, x , y):
        self.result= x * y
        self.history.append(self.result)
        return self.result
    #shift + alt + arriba/ abajo para copiar el codigo
    def divide(self, x , y):
        if y == 0:
            print("no se puede realizar la división con 0")
        else:
            self.result= x / y
            self.history.append(self.result)
            return self.result
    def module(self, x , y):
        if y == 0:
            print("no se puede realizar la división con 0")
        else:
            self.result= x // y #operador módulo
            self.history.append(self.result)
            return self.result
    def power(self, x, y):
        self.result=pow(x,y)
        self.history.append(self.result)
        return self.result
    def show_history(self):
        return self.history #mostrar directamente el historial
    
    def clear_history(self):
        self.history.clear()    # eliminar el historial
        return "Ya he eliminado mi historial"

# El objeto de la clase
obj_calculator= Calculator()
print(obj_calculator.add(10,5))
print(obj_calculator.power(7,9))
print(obj_calculator.subtract(50, 25))
print(obj_calculator.divide(6, 7))
print(obj_calculator.multiply(42, 2))
print(obj_calculator.module(5, 2))
print(obj_calculator.show_history)
