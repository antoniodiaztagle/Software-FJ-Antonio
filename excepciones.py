
"""
Modulo de excepciones personalizadas
Proyecto: Software FJ
Autor: Antonio Jose Diaztagle Pacheco
"""


class ErrorSistema(Exception):
    """Excepcion base del sistema."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se genera cuando los datos ingresados no son validos."""
    pass


class ClienteNoEncontradoError(ErrorSistema):
    """Se genera cuando un cliente no existe."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no esta disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva presenta inconsistencias."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se genera cuando se intenta realizar una operacion no permitida."""
    pass
