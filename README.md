
# SOFTWARE FJ
## Sistema Integral de Gestion de Clientes, Servicios y Reservas

### Autor
Antonio Jose Diaztagle Pacheco

### Descripcion del proyecto

Este proyecto consiste en el desarrollo de un sistema integral para la empresa ficticia Software FJ, cuyo objetivo es administrar clientes, servicios y reservas mediante la programacion orientada a objetos en Python.

El sistema permite registrar clientes, gestionar diferentes tipos de servicios y crear, confirmar, cancelar y procesar reservas. Ademas, incorpora validaciones y excepciones personalizadas para controlar los errores que puedan presentarse durante la ejecucion.

### Objetivo general

Desarrollar una aplicacion en Python que permita gestionar clientes, servicios y reservas, aplicando los principios de la programacion orientada a objetos y mecanismos de manejo de excepciones.

### Tecnologias utilizadas

- Python 3.
- Visual Studio Code.
- Programacion orientada a objetos.
- Manejo de excepciones.
- Modulo logging para el registro de eventos.
- Git y GitHub para el control de versiones.

### Funcionalidades principales

1. Registro y consulta de clientes.
2. Registro de servicios especializados.
3. Gestion de reservas.
4. Confirmacion y cancelacion de reservas.
5. Calculo del costo de los servicios.
6. Validacion de datos.
7. Manejo de excepciones personalizadas.
8. Registro de eventos y errores en archivos de log.
9. Simulaciones de operaciones correctas e incorrectas.

### Estructura del proyecto

```text
Software_FJ_Antonio/
│
├── main.py
├── entidades.py
├── excepciones.py
├── clientes.py
├── servicios.py
├── reservas.py
├── gestor.py
├── README.md
│
└── logs/
    └── sistema.log
```

### Ejecucion del programa

1. Instalar Python 3.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir la terminal.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

El programa ejecutara diferentes simulaciones para verificar el funcionamiento del sistema.

### Registro de eventos

El sistema utiliza el modulo `logging` de Python para registrar las operaciones realizadas y los errores detectados.

Los registros se almacenan automaticamente en el archivo:

`logs/sistema.log`

### Aplicacion de programacion orientada a objetos

El proyecto aplica los siguientes conceptos:

- **Abstraccion:** mediante clases abstractas para definir estructuras generales.
- **Encapsulamiento:** utilizando atributos privados y propiedades.
- **Herencia:** mediante clases especializadas que heredan de clases base.
- **Polimorfismo:** mediante la implementacion de metodos sobrescritos en diferentes clases.

### Manejo de excepciones

Se implementan excepciones personalizadas, bloques `try`, `except`, `else` y `finally`, ademas del encadenamiento de excepciones para controlar situaciones inesperadas.

### Autor

Antonio Jose Diaztagle Pacheco
