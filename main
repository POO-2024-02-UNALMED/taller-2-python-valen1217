class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevo_color):
        colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevo_color in colores_permitidos:
            self.color = nuevo_color
        else:
            print("Color no permitido.")


class Motor:
    def __init__(self, numero_registro, tipo):
        self.registro = numero_registro
        self.tipo = tipo

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        if nuevo_tipo in ["electrico", "gasolina"]:
            self.tipo = nuevo_tipo
        else:
            print("Tipo de motor no permitido.")

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos 
        self.motor = motor       
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificarIntegridad(self):
        registros = [self.registro, self.motor.registro]
        registros.extend(asiento.registro for asiento in self.asientos if isinstance(asiento, Asiento))

        if all(r == self.registro for r in registros):
            return "Auto original"
        else:
            return "Las piezas no son originales"



if __name__ == "__main__":
    motor = Motor(1234, "gasolina")
    asiento1 = Asiento("rojo", 500, 1234)
    asiento2 = Asiento("verde", 400, 1234)
    asientos = [asiento1, asiento2]
    auto = Auto("ModeloX", 15000, asientos, motor, 1234)

    print(auto.cantidadAsientos())  
    print(auto.verificarIntegridad()) 

    asiento1.cambiarColor("amarillo")
    motor.cambiarRegistro(4321)
    print(auto.verificarIntegridad()) 
