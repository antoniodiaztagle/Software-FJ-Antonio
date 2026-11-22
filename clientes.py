
"""
Modulo de gestion de clientes
Proyecto: Software FJ
Autor: Antonio Jose Diaztagle Pacheco
"""

import re
from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):
    """
    Representa un cliente registrado en Software FJ.
    """

    def __init__(self, identificador, nombre, correo, telefono):

        super().__init__(identificador)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    def validar_datos(self):
        """Verifica que los datos del cliente sean correctos."""

        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise DatosInvalidosError(
                "El nombre del cliente es obligatorio."
            )

        if not isinstance(self.__correo, str) or not re.fullmatch(
            r"[\w.+-]+@[\w-]+\.[\w.-]+", self.__correo
        ):
            raise DatosInvalidosError(
                "El correo electronico no es valido."
            )

        if (
            not isinstance(self.__telefono, str)
            or not self.__telefono.isdigit()
            or len(self.__telefono) < 7
        ):
            raise DatosInvalidosError(
                "El telefono debe contener al menos 7 digitos."
            )

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        """Muestra la informacion del cliente."""

        return (
            f"Identificacion: {self.identificador}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Telefono: {self.__telefono}"
        )
