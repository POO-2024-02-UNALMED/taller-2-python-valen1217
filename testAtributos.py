from main import Asiento, Motor, Auto

def testAtributosMotor():
    motor = Motor(1234, "gasolina")
    assert motor.registro == 1234
    assert motor.tipo == "gasolina"

def testAtributosAsiento():
    asiento = Asiento("rojo", 500, 5678)
    assert asiento.color == "rojo"
    assert asiento.precio == 500
    assert asiento.registro == 5678

def testAtributosAuto():
    motor = Motor(1234, "gasolina")
    asientos = [Asiento("rojo", 500, 1234), None, None]
    auto = Auto("ModeloY", 20000, asientos, motor, 1234)
    assert auto.modelo == "ModeloY"
    assert auto.precio == 20000
    assert auto.asientos == asientos
    assert auto.motor == motor
    assert auto.registro == 1234
