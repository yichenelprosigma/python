import random
from datetime import datetime,date
#Un sistema de gestión de cuentas bancarias
# 1. Account class: -Número de la cuenta (int),
# -Titular de la cuenta(int)
# -Fecha de seguridad (date)
# -código de seguridad cvv 3 dígitos(int)
# -saldo(int)
# -Información de ingreso, transferencia y retiro [lista] (de información)
# -Número de tarjeta(int)

#Métodos :
# - Mostrar saldo
# - Hacer una transferencia
# - Hacer un ingreso
# - Retirar/sacar dinero

class Account:
    # Atributos
    def __init__(self,accountNumber,HolderName:str,password:int,balance:float=0.0):
        self.accountNumber= accountNumber
        self.HolderName=HolderName
        self.balance=balance
        self.password=password
        self.cvv= random.randint(0,999)
        print(self.cvv)
        #fecha de caducidad
        today=datetime.now()
        five_years_late=today.year+5
        self.expirationDate =date(five_years_late,today.month,today.day)
        print(self.expirationDate)
    
    
    # Métodos:
    # Mostrar saldo
    def displayinformation(self) -> None:
        print("\n=================== Información de la cuenta ==========================")
        print(f"Número de la cuenta: {self.accountNumber}")
        print(f"Titular de la cuenta: {self.HolderName}")
        print(f"Saldo de la cuenta: {self.balance} euros")

    
    def displayinformationsecret(self) -> None:
        password=int(input("introduzca su contraseña para ver información:"))
        if password== self.password:
            print("\n========================== Información secreta de la cuenta ==========================")
            print(f"cvv:{self.cvv }")
            print(f"Número de la cuenta: {self.accountNumber}")
            print(f"Fecha de caducidad: {self.expirationDate}")
    def transfer(self):
        print("Quieres hacer una transferencia ")
        Iban= input("Iban del destinario: ")
        beneficiaryName= input("Nombre del beneficiario: ")
        amount= float(input("Introduzca el importe:"))
        concept= input("Concepto: ")
        password=int(input("introduzca su contraseña para hacer la transferencia: "))
        if password== self.password:
            if amount <= self.balance:
                print("No se puede hacer esta transferencia ya que su saldo es mayor que la transferencia")
            else:
                print("========================= Mensaje de éxito ====================")
                print(f"Número de Iban: {Iban} ")
                print(f"Nombre del beneficiario: {beneficiaryName} ")
                print(f"Importe: {amount} ")
                print(f"Concepto: {concept} ")
        else:
            print("La contraseña está mal.")

# función principal
def main():
    objAccount=Account("1234 5678 9999","Luis Alberto",123456)
    objAccount.displayinformation()
    objAccount.displayinformationsecret()
    objAccount.transfer()
if __name__ =="__main__":
    main()