class Account:  #  Clase que representa una cuenta bancaria

    def __init__(self, filepath):  #  Método inicializador que recibe la ruta del archivo; self y filepath son parámetros
        self.filepath = filepath  #  Almacena la ruta del archivo en un atributo de instancia
        with open(filepath, "r") as file:  #  Abre el archivo en modo lectura
            self.balance = int(file.read())  #  Lee el contenido del archivo y lo convierte a entero para establecer el saldo
    
    def withdraw(self, amount):  #  Método para retirar una cantidad de dinero
        self.balance = self.balance - amount  #  Resta la cantidad del saldo actual
    
    def deposit(self, amount):  #  Método para depositar una cantidad de dinero
        self.balance = self.balance + amount  #  Suma la cantidad al saldo actual

    def commit(self):  #  Método para guardar el saldo actualizado en el archivo
        with open(self.filepath, "w") as file:  #  Abre el archivo en modo escritura
            file.write((str(self.balance)))  #  Escribe el saldo actual en el archivo como cadena
            
class Checking(Account):  #  Clase que representa una cuenta corriente, hereda de Account
    """This class generates checking account objects"""

    type = "checking"

    def __init__(self, filepath, fee):  #  Método inicializador que recibe la ruta del archivo y una tarifa
        Account.__init__(self, filepath)  #  Llama al inicializador de la clase base Account
        self.fee = fee  #  Almacena la tarifa en un atributo de instancia

    def transfer(self, amount):  #  Método para transferir una cantidad de dinero
        self.balance = self.balance - amount - self.fee  #  Resta la cantidad y la tarifa del saldo actual

jacks_Checking = Checking("/home/zetawiser/Documentos/Programación/Curso_python/OOP/account/jack.txt", 1)  #  Crea una instancia de Checking con la ruta del archivo y una tarifa de 1
jacks_Checking.transfer(310)  #  Realiza una transferencia de 310
print(jacks_Checking.balance)  #  Imprime el saldo después de la transferencia
jacks_Checking.commit()  #  Guarda el saldo actualizado en el archivo
print(jacks_Checking.type)


john_Checking = Checking("/home/zetawiser/Documentos/Programación/Curso_python/OOP/account/john.txt", 1)  #  Crea una instancia de Checking con la ruta del archivo y una tarifa de 1
john_Checking.transfer(310)  #  Realiza una transferencia de 310
print(john_Checking.balance)  #  Imprime el saldo después de la transferencia
john_Checking.commit()  #  Guarda el saldo actualizado en el archivo
print(john_Checking.type)
print(john_Checking.__doc__)