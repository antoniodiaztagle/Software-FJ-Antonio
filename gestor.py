
"""
Modulo gestor central del sistema
Proyecto: Software FJ
Autor: Antonio Jose Diaztagle Pacheco

Administra clientes, servicios y reservas.
Registra los eventos y errores del sistema.
"""

import logging
from pathlib import Path

from excepciones import (
    DatosInvalidosError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError
)

from reservas import Reserva


class GestorSistema:
    """Administra las operaciones del sistema Software FJ."""

    def __init__(self):

        # Listas internas para almacenar los objetos.
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

        # Crear automaticamente la carpeta de registros.
        carpeta_logs = Path(__file__).parent / "logs"
        carpeta_logs.mkdir(exist_ok=True)

        # Configurar el registro de eventos y errores.
        self.logger = logging.getLogger("SoftwareFJ_Antonio")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        if not self.logger.handlers:

            archivo_log = carpeta_logs / "sistema.log"

            manejador = logging.FileHandler(
                archivo_log,
                encoding="utf-8"
            )

            formato = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            manejador.setFormatter(formato)
            self.logger.addHandler(manejador)

        self.logger.info("Sistema Software FJ iniciado.")

    def registrar_cliente(self, cliente):
        """Registra un nuevo cliente."""

        try:
            if cliente is None:
                raise DatosInvalidosError(
                    "No se puede registrar un cliente vacio."
                )

            if any(
                c.identificador == cliente.identificador
                for c in self.__clientes
            ):
                raise DatosInvalidosError(
                    "Ya existe un cliente con esa identificacion."
                )

            self.__clientes.append(cliente)

            self.logger.info(
                "Cliente registrado: %s",
                cliente.identificador
            )

            return True

        except Exception:
            self.logger.exception("Error al registrar cliente.")
            raise

    def registrar_servicio(self, servicio):
        """Registra un nuevo servicio."""

        try:
            if servicio is None:
                raise DatosInvalidosError(
                    "No se puede registrar un servicio vacio."
                )

            if any(
                s.identificador == servicio.identificador
                for s in self.__servicios
            ):
                raise DatosInvalidosError(
                    "Ya existe un servicio con ese codigo."
                )

            self.__servicios.append(servicio)

            self.logger.info(
                "Servicio registrado: %s",
                servicio.identificador
            )

            return True

        except Exception:
            self.logger.exception("Error al registrar servicio.")
            raise

    def buscar_cliente(self, identificador):
        """Busca un cliente por su identificacion."""

        for cliente in self.__clientes:
            if cliente.identificador == identificador:
                return cliente

        raise ClienteNoEncontradoError(
            f"No se encontro el cliente {identificador}."
        )

    def buscar_servicio(self, identificador):
        """Busca un servicio por su codigo."""

        for servicio in self.__servicios:
            if servicio.identificador == identificador:
                return servicio

        raise ServicioNoDisponibleError(
            f"No se encontro el servicio {identificador}."
        )

    def crear_reserva(
        self,
        identificador,
        id_cliente,
        id_servicio,
        duracion
    ):
        """Crea una nueva reserva."""

        try:
            if any(
                r.identificador == identificador
                for r in self.__reservas
            ):
                raise ReservaInvalidaError(
                    "Ya existe una reserva con ese codigo."
                )

            cliente = self.buscar_cliente(id_cliente)
            servicio = self.buscar_servicio(id_servicio)

            nueva_reserva = Reserva(
                identificador,
                cliente,
                servicio,
                duracion
            )

            self.__reservas.append(nueva_reserva)

            self.logger.info(
                "Reserva creada: %s para el cliente %s",
                identificador,
                id_cliente
            )

            return nueva_reserva

        except Exception:
            self.logger.exception("Error al crear reserva.")
            raise

    def buscar_reserva(self, identificador):
        """Busca una reserva por su codigo."""

        for reserva in self.__reservas:
            if reserva.identificador == identificador:
                return reserva

        raise ReservaInvalidaError(
            f"No se encontro la reserva {identificador}."
        )

    def confirmar_reserva(
        self,
        identificador,
        impuesto=0,
        descuento=0
    ):
        """Confirma una reserva y calcula su costo."""

        try:
            reserva = self.buscar_reserva(identificador)

            costo = reserva.confirmar(
                impuesto,
                descuento
            )

            self.logger.info(
                "Reserva %s confirmada. Costo: $%.2f",
                identificador,
                costo
            )

            return costo

        except Exception:
            self.logger.exception("Error al confirmar reserva.")
            raise

    def cancelar_reserva(self, identificador):
        """Cancela una reserva."""

        try:
            reserva = self.buscar_reserva(identificador)

            resultado = reserva.cancelar()

            self.logger.info(
                "Reserva cancelada: %s",
                identificador
            )

            return resultado

        except Exception:
            self.logger.exception("Error al cancelar reserva.")
            raise

    def procesar_reserva(self, identificador):
        """Procesa una reserva confirmada."""

        try:
            reserva = self.buscar_reserva(identificador)

            resultado = reserva.procesar()

            self.logger.info(
                "Reserva procesada: %s",
                identificador
            )

            return resultado

        except Exception:
            self.logger.exception("Error al procesar reserva.")
            raise

    def listar_clientes(self):
        """Devuelve una copia de los clientes registrados."""
        return list(self.__clientes)

    def listar_servicios(self):
        """Devuelve una copia de los servicios registrados."""
        return list(self.__servicios)

    def listar_reservas(self):
        """Devuelve una copia de las reservas registradas."""
        return list(self.__reservas)
