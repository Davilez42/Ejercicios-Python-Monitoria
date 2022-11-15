class Automovil:
    def __init__(self) -> None:
        self.marca = "ford"
        self.motor = "dasd"
        self.material = "acero"
        self.modelo = "12323"

    def arrancar(self):
        print("RUNN!")

carro =  Automovil()
print(carro.marca)