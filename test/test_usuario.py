import unittest
import usuario

class UsuarioTest (unittest.TestCase):

    def test_saludar_deberia_devolver_hola(self):

        #ARRANGE
        saludoEsperado = "Hola"

        #ACT
        saludoRecibido = usuario.saludar()

        #ASSERT
        self.assertEqual(saludoEsperado,saludoRecibido)