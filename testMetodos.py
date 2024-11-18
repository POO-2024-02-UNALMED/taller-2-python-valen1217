from main import Asiento, Motor, Auto

def testMetodoCambiarColor():
    a1 = Asiento("blanco", 5000, 435)
    a2 = Asiento("blanco", 5000, 435)
    
    a1.cambiarColor("naranja")
    a2.cambiarColor("verde")
    
    assert a1.color == "blanco"  
    assert a2.color == "verde" 

def testMetodoCambiarRegistro():
    m = Motor(4, "gasolina")
    m.cambiarRegistro(423)
    assert m.registro == 423

def testMetodoAsignarTipo():
    m1 = Motor(4, "normal")
    m2 = Motor(4, "normal")
    
    m1.asignarTipo("hibrido")
    m2.asignarTipo("electrico")
    
    assert m1.tipo == "normal" 
    assert m2.tipo == "electrico"

def testMetodoCantidadAsientos():
    a = Auto("model 3", 33000, list(), Motor(4, "electrico"), 341)
    a.asientos = [Asiento("blanco", 5000, 435), None, None, Asiento("blanco", 5000, 435), None]
    assert a.cantidadAsientos() == 2

def testMetodoVerificarIntegridad():
    a1 = Auto("model 3", 33000, [Asiento("blanco", 5000, 32), None, None, Asiento("blanco", 5000, 32), None],
              Motor(32, "electrico"), 32)  # Ajustar registro del motor
    a2 = Auto("model 3", 33000, [Asiento("blanco", 5000, 40), None, None, Asiento("blanco", 5000, 32), None],
              Motor(32, "electrico"), 32)  # El motor tiene el registro correcto, pero un asiento no

    assert a1.verificarIntegridad() == "Auto original"
    assert a2.verificarIntegridad() == "Las piezas no son originales"

