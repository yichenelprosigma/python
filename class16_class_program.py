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
    def __init__(self,accountNumber,HolderName:str,balance:float=0.0):
        self.accountNumber= accountNumber
        self.HolderName=HolderName
        self.balance=balance
    
    # Métodos:
    # Mostrar saldo
    def displayinformation(self):
        print("\n=================== Información de la cuenta ==========================")
        print(f"Número de la cuenta: {self.accountNumber}")
        print(f"Titular de la cuenta: {self.HolderName}")
        print(f"Saldo de la cuenta: {self.balance} euros")

    

# función principal
def main():
    objAccount=Account("1234 5678 9999","Luis Alberto")
    objAccount.displayinformation()
if __name__ =="__main__":
    main()