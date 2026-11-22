
"""
Programa principal del sistema Software FJ
Autor: Antonio Jose Diaztagle Pacheco

Ejecuta simulaciones para comprobar el funcionamiento
de clientes, servicios y reservas.
"""

from gestor import GestorSistema
from clientes import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)


def ejecutar_prueba(numero, descripcion, operacion, gestor):
    """Ejecuta una prueba y controla sus posibles excepciones."""

    print(f"\nPRUEBA {numero}: {descripcion}")

    try:
        resultado = operacion()

    except Exception as error:
        print(f"ERROR CONTROLADO: {error}")
        gestor.logger.error(
            "Prueba %s - %s: %s",
            numero,
            descripcion,
            error
        )

    else:
        print("RESULTADO: Operacion realizada correctamente.")

        if resultado is not None:
            print(resultado)

        gestor.logger.info(
            "Prueba %s - %s: exitosa",
            numero,
            descripcion
        )


def main():

    print("=" * 60)
    print("SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("Autor: Antonio Jose Diaztagle Pacheco")
    print("=" * 60)

    gestor = GestorSistema()

    # -------------------------------------------------
    # PRUEBA 1: Registro de un cliente.
    # -------------------------------------------------

    cliente1 = Cliente(
        "C001",
        "Carlos Martinez",
        "carlos@gmail.com",
        "3001234567"
    )

    ejecutar_prueba(
        1,
        "Registro de cliente valido",
        lambda: gestor.registrar_cliente(cliente1),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 2: Registro de otro cliente.
    # -------------------------------------------------

    cliente2 = Cliente(
        "C002",
        "Laura Gomez",
        "laura@gmail.com",
        "3107654321"
    )

    ejecutar_prueba(
        2,
        "Registro de segundo cliente",
        lambda: gestor.registrar_cliente(cliente2),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 3: Registro de cliente duplicado.
    # -------------------------------------------------

    ejecutar_prueba(
        3,
        "Intento de registrar cliente duplicado",
        lambda: gestor.registrar_cliente(cliente1),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 4: Datos invalidos de cliente.
    # -------------------------------------------------

    ejecutar_prueba(
        4,
        "Creacion de cliente con correo invalido",
        lambda: Cliente(
            "C003",
            "Pedro Ramirez",
            "correo_incorrecto",
            "3001234567"
        ),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 5: Registro de sala.
    # -------------------------------------------------

    sala = ReservaSala(
        "S001",
        "Sala de reuniones",
        100000,
        True,
        10
    )

    ejecutar_prueba(
        5,
        "Registro de servicio de sala",
        lambda: gestor.registrar_servicio(sala),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 6: Registro de alquiler de equipo.
    # -------------------------------------------------

    equipo = AlquilerEquipo(
        "E001",
        "Alquiler de computadores",
        50000,
        True,
        "Computador portatil"
    )

    ejecutar_prueba(
        6,
        "Registro de servicio de alquiler de equipo",
        lambda: gestor.registrar_servicio(equipo),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 7: Registro de asesoria.
    # -------------------------------------------------

    asesoria = AsesoriaEspecializada(
        "A001",
        "Asesoria tecnologica",
        150000,
        True,
        "Desarrollo de software"
    )

    ejecutar_prueba(
        7,
        "Registro de asesoria especializada",
        lambda: gestor.registrar_servicio(asesoria),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 8: Servicio no disponible.
    # -------------------------------------------------

    equipo_no_disponible = AlquilerEquipo(
        "E002",
        "Equipo fuera de servicio",
        40000,
        False,
        "Proyector"
    )

    ejecutar_prueba(
        8,
        "Registro de servicio no disponible",
        lambda: gestor.registrar_servicio(equipo_no_disponible),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 9: Tarifa invalida.
    # -------------------------------------------------

    ejecutar_prueba(
        9,
        "Creacion de servicio con tarifa invalida",
        lambda: ReservaSala(
            "S002",
            "Sala invalida",
            -50000,
            True,
            5
        ),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 10: Creacion de reserva.
    # -------------------------------------------------

    ejecutar_prueba(
        10,
        "Creacion de reserva valida",
        lambda: gestor.crear_reserva(
            "R001",
            "C001",
            "S001",
            2
        ),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 11: Confirmacion de reserva.
    # -------------------------------------------------

    ejecutar_prueba(
        11,
        "Confirmacion de reserva con impuesto y descuento",
        lambda: gestor.confirmar_reserva(
            "R001",
            19,
            10
        ),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 12: Procesamiento de reserva.
    # -------------------------------------------------

    ejecutar_prueba(
        12,
        "Procesamiento de reserva confirmada",
        lambda: gestor.procesar_reserva("R001"),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 13: Reserva con cliente inexistente.
    # -------------------------------------------------

    ejecutar_prueba(
        13,
        "Creacion de reserva con cliente inexistente",
        lambda: gestor.crear_reserva(
            "R002",
            "C999",
            "S001",
            2
        ),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 14: Duracion invalida.
    # -------------------------------------------------

    ejecutar_prueba(
        14,
        "Creacion de reserva con duracion invalida",
        lambda: gestor.crear_reserva(
            "R003",
            "C001",
            "S001",
            -2
        ),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 15: Reserva de servicio no disponible.
    # -------------------------------------------------

    ejecutar_prueba(
        15,
        "Intento de reservar un servicio no disponible",
        lambda: gestor.crear_reserva(
            "R004",
            "C001",
            "E002",
            1
        ),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 16: Creacion de segunda reserva valida.
    # -------------------------------------------------

    ejecutar_prueba(
        16,
        "Creacion de segunda reserva valida",
        lambda: gestor.crear_reserva(
            "R005",
            "C002",
            "E001",
            3
        ),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 17: Cancelacion de reserva pendiente.
    # -------------------------------------------------

    ejecutar_prueba(
        17,
        "Cancelacion de reserva pendiente",
        lambda: gestor.cancelar_reserva("R005"),
        gestor
    )

    # -------------------------------------------------
    # PRUEBA 18: Intento de procesar reserva cancelada.
    # -------------------------------------------------

    ejecutar_prueba(
        18,
        "Procesamiento de reserva cancelada",
        lambda: gestor.procesar_reserva("R005"),
        gestor
    )

    # -------------------------------------------------
    # RESUMEN FINAL.
    # -------------------------------------------------

    print("\n" + "=" * 60)
    print("RESUMEN DEL SISTEMA")
    print("=" * 60)

    print(f"Clientes registrados: {len(gestor.listar_clientes())}")
    print(f"Servicios registrados: {len(gestor.listar_servicios())}")
    print(f"Reservas creadas: {len(gestor.listar_reservas())}")

    print("\nCLIENTES:")

    for cliente in gestor.listar_clientes():
        print(cliente.mostrar_informacion())

    print("\nSERVICIOS:")

    for servicio in gestor.listar_servicios():
        print(servicio.mostrar_informacion())

    print("\nRESERVAS:")

    for reserva in gestor.listar_reservas():
        print(reserva.mostrar_informacion())

    print("\n" + "=" * 60)
    print("SIMULACIONES FINALIZADAS")
    print("Consulte logs/sistema.log para revisar los registros.")
    print("=" * 60)


if __name__ == "__main__":

    try:
        main()

    except Exception as error:
        print(f"Error general del sistema: {error}")

    finally:
        print("\nEjecucion del programa finalizada.")
