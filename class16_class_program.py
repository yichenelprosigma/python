import random
from datetime import datetime,date
import getpass
import pwinput

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
        #fecha de caducidad
        today=datetime.now()
        five_years_late=today.year+5
        self.expirationDate =date(five_years_late,today.month,today.day)
    
    
    # Métodos:
    # Mostrar saldo
    def displayinformation(self) -> None:
        print("\n=================== Información de la cuenta ==========================")
        print(f"Número de la cuenta: {self.accountNumber}")
        print(f"Titular de la cuenta: {self.HolderName}")
        print(f"Saldo de la cuenta: {self.balance} euros")

    # Mostrar datos sensible
    def displayinformationsecret(self) -> None:
        password=pwinput.pwinput("Introduzca una contraseña",mask="*")
        if password==self.password:
            print("\n========================== Información secreta de la cuenta ==========================")
            print(f"cvv:{self.cvv }")
            print(f"Número de la cuenta: {self.accountNumber}")
            print(f"Fecha de caducidad: {self.expirationDate}")
        else:
            print("La contraseña está mal")
    def deposit(self):
        print("============ Entrando el apartido de ingreso ==========")
        deposit=int(input("¿Cuánto quiere ingresar usted? "))
        self.balance += deposit
        print("===========Has ingresado de manera correctamente====================")
        self.displayinformation()
    def withdrawal(self):
        
        print("======================== Sacar dinero =====================")
        withdrawal= int(input("¿Cuánto dinero quiere retirar usted? "))
        password=int(input("introduzca su contraseña para retirar el dinero: "))
        password.getpass()
        if password == self.password:
            if withdrawal <= self.balance:
                print("======================mensaje de exito =============")
                self.balance=-withdrawal
                print("No se puede hacer esta retirar ya que su saldo es mayor que lo que quiere retirar")
                print(f"Has sacado {withdrawal} euros en su cuenta")
                self.displayinformation()
            else:
                print(f"No tiene dinero suficiente para retirar este dinero")
        else:
            print("la contraseña está mal")

    #hacer una transferencia
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
    while True:
        print("\n--- Bienvenido al sistema de gestión del geometría ---")
        print("1. Crear cuenta")
        print("2. Mostrar información de la cuenta")
        print("3. Mostrar los datos secretas")
        print("4. Ingreso")
        print("5. Sacar dinero")
        print("6. Transferencia")
        print("0. Salir")
        option = int(input("\nSeleccione una opción: "))
        print(option)
        match option:
            case 1:
                print("crear la cuenta")
                # modificación se tiene que crear automaticamente
                accountnumber=input("selecciona un número para su cuenta:")
                holderName=input("Introduzca su nombre:")
                # modificación: comprobar si son 6 digitos y si es segura y por ultimo si la contraseña es igual
                # password=int(input("Introduzca una contraseña para su cuenta:"))
                # Forma 1 con el getpass no se ve la contraseña
                # password=getpass.getpass("Introduzca una contraseña para su cuenta:")
                # checkpassword= getpass.getpass("Confirmar la contraseña")

                # Forma 2 
                password=pwinput.pwinput("Introduzca una contraseña",mask="*")
                checkPassword=pwinput.pwinput("Confirma la contraseña",mask="*")
                if password== checkPassword:
                    print("Configuración correcta")
                else:
                    print("no está bien, hazlo de nuevo")
                # crear un objeto de la clase de account
                # modificación todos la información de los clientes 
                client1=Account("accountNumber","holderName",password)
                print("=============== Lo lograste con éxito=========")
                print(" has creado la cuenta de manera correcta")
                client1.displayinformation()
            case 2:
                client1.displayinformation()
            case 3:
                client1.displayinformationsecret()
            case 4:
                client1.displayinformation()
            case 5:
                client1.withdrawal()
            case 6:
                client1.transfer()
            case 0:
                print("Saliendo...")
                break
                
if __name__ == "__main__":
    main()