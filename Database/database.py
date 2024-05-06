import sqlite3 as sql
import random
import string
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta


# Initialize Faker to generate fake data
fake = Faker()

# Connect to SQLite database
conn = sql.connect("Database/portadelsol.db")
cursor = conn.cursor()


class Database:

    def Empleados(n: int):
        # Create Empleados Table
        cursor.execute(
            """
    -- Empleados
        CREATE TABLE IF NOT EXISTS Empleados (
            Empleado_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Posicion TEXT NOT NULL,
            Nombre TEXT NOT NULL,
            Apellido_Paterno TEXT NOT NULL,
            Apellido_Materno TEXT NOT NULL,
            Genero TEXT NOT NULL,
            Correo_Electronico VARCHAR(255) NOT NULL,
            Celular VARCHAR(10) NOT NULL,
            Celular_2 TEXT,
            Direccion TEXT NOT NULL,
            Fecha_Nacimiento DATE NOT NULL,
            Lugar_Nacimiento TEXT NOT NULL,
            Seguro_Social VARCHAR(9) NOT NULL,
            Licencia VARCHAR(20),
            Servicio_Militar VARCHAR(11),
            Estado_Civil TEXT,
            Estado_Empleo TEXT NOT NULL DEFAULT 'Activo');"""
        )

        # # Generate 50 records for Empleados table
        for _ in range(n):
            Posicion = random.choice(
                [
                    "Embalsamador",
                    "Gerente",
                    "Supervisor",
                    "Cafeteria",
                    "Mantenimiento",
                    "Tecnico",
                ]
            )
            Nombre = fake.first_name()
            Apellido_Paterno = fake.last_name()
            Apellido_Materno = fake.last_name()
            Genero = random.choice(["Masculino", "Femenino"])
            Correo_Electronico = fake.email()
            Celular = fake.phone_number()[:10]  # Ensure max length of 10
            Celular_2 = (
                fake.phone_number()[:10] if random.choice([True, False]) else None
            )
            Direccion = fake.address()
            Fecha_Nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=65)
            Lugar_Nacimiento = fake.city()
            Seguro_Social = "".join(random.choices("0123456789", k=9))
            Licencia = (
                "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=7))
                if random.choice([True, False])
                else None
            )
            Servicio_Militar = (
                fake.random_number(digits=8) if random.choice([True, False]) else None
            )
            Estado_Civil = random.choice(["Soltero", "Casado", "Divorciado", "Viudo"])
            Estado_Empleo = random.choice(["Activo", "Inactivo"])

            cursor.execute(
                """
            INSERT INTO Empleados (
                Posicion,
                Nombre,
                Apellido_Paterno,
                Apellido_Materno,
                Genero,
                Correo_Electronico,
                Celular,
                Celular_2,
                Direccion,
                Fecha_Nacimiento,
                Lugar_Nacimiento,
                Seguro_Social,
                Licencia,
                Servicio_Militar,
                Estado_Civil,
                Estado_Empleo)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
                (
                    Posicion,
                    Nombre,
                    Apellido_Paterno,
                    Apellido_Materno,
                    Genero,
                    Correo_Electronico,
                    Celular,
                    Celular_2,
                    Direccion,
                    Fecha_Nacimiento,
                    Lugar_Nacimiento,
                    Seguro_Social,
                    Licencia,
                    Servicio_Militar,
                    Estado_Civil,
                    Estado_Empleo,
                ),
            )

    def Credenciales():
        # Create Credenciales Table
        cursor.execute(
            """
    -- Credenciales
        CREATE TABLE IF NOT EXISTS Credenciales (
            Usuario_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Empleado_ID INTEGER NOT NULL,
            Usuario TEXT NOT NULL,
            Contraseña TEXT NOT NULL,
            Rol INTEGER NOT NULL DEFAULT 1,
            FOREIGN KEY (Empleado_ID) REFERENCES Empleados (Empleado_ID));"""
        )

        # Generate credentials for each employee
        cursor.execute("SELECT Empleado_ID, Nombre FROM Empleados")
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=["Empleado_ID", "Nombre"])
        for index, row in df.iterrows():
            empleado_id = row["Empleado_ID"]
            nombre = row["Nombre"]
            usuario = nombre.lower().replace(" ", "") + str(empleado_id)
            contraseña = "".join(
                random.choices(string.ascii_letters + string.digits, k=8)
            )  # Generate random password

            cursor.execute(
                """
            INSERT INTO Credenciales (Empleado_ID, Usuario, Contraseña)
            VALUES (?, ?, ?)
            """,
                (empleado_id, usuario, contraseña),
            )

    def Servicios():
        # Create Servicios Table
        cursor.execute(
            """
    -- Servicios
        CREATE TABLE IF NOT EXISTS Servicios (
            Servicio_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Servicio_Nombre TEXT NOT NULL,
            Servicio_Precio DECIMAL(6,2) NOT NULL);"""
        )

        # Generate 50 records for Servicios table
        services = [
            "Servicio de Embalsamamiento",
            "Diseño de programa para Servicio Funebres",
            "Servicio de Transportación," "Arreglo Floral",
            "Producción de Video",
            "Servicio de Velatorio",
            "Servicio de cremación",
            "Urna de Madera",
            "Urna de Marmol",
            "Urna de Cobre",
            "Urnna de Ceramica",
            "Urna Biodegradable",
            "Servicio de Entierro",
            "Ataúd de Madera",
            "Ataúd de Hierro",
            "Ataúd de Mimbre",
            "Ataúd de Pino",
            "Ataúd de Caoba",
            "Ataúd Biodegradable",
        ]
        for service in services:
            servicio_nombre = service
            servicio_precio = round(
                random.uniform(100, 500), 2
            )  # Generate a random price between 100 and 2000

            cursor.execute(
                """
            INSERT INTO Servicios (Servicio_Nombre, Servicio_Precio)
            VALUES (?, ?)
            """,
                (servicio_nombre, servicio_precio),
            )

    def Servicios_Elegidos(n: int):
        cursor.execute(
            """
-- Servicios_Elegidos
CREATE TABLE IF NOT EXISTS Servicios_Elegidos (
    Servicios_Elegidos_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Contrato_ID INTEGER NOT NULL,
    Servicio_ID INTEGER NOT NULL,
    FOREIGN KEY (Contrato_ID) REFERENCES Contratos (Contrato_ID),
    FOREIGN KEY (Servicio_ID) REFERENCES Servicios (Servicio_ID)

);"""
        )
        for id in range(n):
            Servicio_ID = random.randint(1, 18)
            cursor.execute(
                """
                INSERT INTO Servicios_Elegidos (Contrato_ID, Servicio_ID)
                VALUES(?, ?)
            """,
                (id + 1, Servicio_ID),
            )

    def Clientes(n: int):
        # Create Clientes Table
        cursor.execute(
            """
        -- Clientes
        CREATE TABLE IF NOT EXISTS Clientes (
            Cliente_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Ocupacion TEXT NOT NULL,
            Nombre TEXT NOT NULL,
            Apellido_Paterno TEXT NOT NULL,
            Apellido_Materno TEXT NOT NULL,
            Genero TEXT NOT NULL,
            Correo_Electronico VARCHAR(255) NOT NULL,
            Celular VARCHAR(10) NOT NULL,
            Celular_2 TEXT,
            Direccion TEXT NOT NULL,
            Fecha_Nacimiento DATE NOT NULL,
            Lugar_Nacimiento TEXT NOT NULL,
            Seguro_Social VARCHAR(9) NOT NULL,
            Licencia VARCHAR(20),
            Servicio_Militar VARCHAR(11),
            Estado_Civil TEXT,
            Descripcion TEXT);"""
        )
        # Generate 50 records for Clientes table
        for _ in range(n):
            Ocupacion = fake.job()
            Nombre = fake.first_name()
            Apellido_Paterno = fake.last_name()
            Apellido_Materno = fake.last_name()
            Genero = random.choice(["Masculino", "Femenino", "Otro"])
            Correo_Electronico = fake.email()
            Celular = fake.phone_number()[:10]  # Ensure max length of 10
            Celular_2 = (
                fake.phone_number()[:10] if random.choice([True, False]) else None
            )
            Direccion = fake.address()
            Fecha_Nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=65)
            Lugar_Nacimiento = fake.city()
            Seguro_Social = "".join(random.choices("0123456789", k=9))
            Licencia = (
                "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=7))
                if random.choice([True, False])
                else None
            )
            Servicio_Militar = (
                fake.random_number(digits=8) if random.choice([True, False]) else None
            )
            Estado_Civil = random.choice(["Soltero", "Casado", "Divorciado", "Viudo"])
            Descripcion = random.choice(
                [
                    "Familias en duelo",
                    "Clientes previsores",
                    "Instituciones religiosas",
                    "Compañías de seguros",
                    "Hospitales y hogares de ancianos",
                    "Servicios sociales y organizaciones benéficas",
                    "Personas que han perdido a sus mascotas",
                ]
            )
            cursor.execute(
                """
            INSERT INTO Clientes (
            Ocupacion,
            Nombre,
            Apellido_Paterno,
            Apellido_Materno,
            Genero,
            Correo_Electronico,
            Celular,
            Celular_2,
            Direccion,
            Fecha_Nacimiento,
            Lugar_Nacimiento,
            Seguro_Social,
            Licencia,
            Servicio_Militar,
            Estado_Civil,
            Descripcion)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
                (
                    Ocupacion,
                    Nombre,
                    Apellido_Paterno,
                    Apellido_Materno,
                    Genero,
                    Correo_Electronico,
                    Celular,
                    Celular_2,
                    Direccion,
                    Fecha_Nacimiento,
                    Lugar_Nacimiento,
                    Seguro_Social,
                    Licencia,
                    Servicio_Militar,
                    Estado_Civil,
                    Descripcion,
                ),
            )

    def Difuntos(n: int):
        cursor.execute(
            """
        -- Difuntos
        CREATE TABLE IF NOT EXISTS Difuntos (
            Difunto_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Apellido_Paterno TEXT NOT NULL,
            Apellidp_Materno TEXT NOT NULL,
            Genero TEXT NOT NULL,
            Estado_Civil TEXT NOT NULL,
            Nombre_Padre TEXT NOT NULL,
            Nombre_Madre TEXT NOT NULL,
            Seguro_Social VARCHAR(11) NOT NULL,
            Servicio_Militar TEXT NULL,
            Edad INTEGER NOT NULL,
            Lugar_Nacimiento NOT NULL,
            Fecha_Nacimiento DATE NOT NULL,
            Fecha_Defuncion DATE NOT NULL
        );
    """
        )
        for _ in range(n):
            Nombre = fake.first_name()
            Apellido_Paterno = fake.last_name()
            Apellidp_Materno = fake.last_name()
            Genero = random.choice(["Masculino", "Femenino", "Otro"])
            Estado_Civil = random.choice(["Soltero", "Casado", "Divorciado", "Viudo"])
            Nombre_Padre = (
                fake.first_name_male() + " " + fake.last_name() + " " + fake.last_name()
            )
            Nombre_Madre = (
                fake.first_name_female()
                + " "
                + fake.last_name()
                + " "
                + fake.last_name()
            )
            Seguro_Social = "".join(random.choices("0123456789", k=9))
            Servicio_Militar = (
                fake.random_number(digits=8) if random.choice([True, False]) else None
            )

            Edad = random.randint(1, 115)
            Lugar_Nacimiento = fake.city()
            Fecha_Nacimiento = fake.date_of_birth(minimum_age=0, maximum_age=115)
            Fecha_Defuncion = fake.date_between_dates(
                date_start=Fecha_Nacimiento, date_end=datetime.today()
            )

            cursor.execute(
                """
                INSERT INTO Difuntos (
                    Nombre,
                    Apellido_Paterno,
                    Apellidp_Materno,
                    Genero,
                    Estado_Civil,
                    Nombre_Padre,
                    Nombre_Madre,
                    Seguro_Social,
                    Servicio_Militar,
                    Edad,
                    Lugar_Nacimiento,
                    Fecha_Nacimiento,
                    Fecha_Defuncion)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (
                    Nombre,
                    Apellido_Paterno,
                    Apellidp_Materno,
                    Genero,
                    Estado_Civil,
                    Nombre_Padre,
                    Nombre_Madre,
                    Seguro_Social,
                    Servicio_Militar,
                    Edad,
                    Lugar_Nacimiento,
                    Fecha_Nacimiento,
                    Fecha_Defuncion,
                ),
            )

    def Documentos(n: int):
        cursor.execute(
            """
        --Documentos
        CREATE TABLE IF NOT EXISTS Documentos (
            Documentos_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Certificado_Defuncion VARCHAR(255) NULL,
            Autorizacion_Cremacion BOOLEAN NOT NULL DEFAULT FALSE,
            Permiso_Cremacion BOOLEAN NOT NULL DEFAULT FALSE
    )
    """
        )
        for _ in range(n):
            Certificado_Defuncion = random.choice(
                ["Certificado Estándar de Muerte", "Certificado Coroner's de Muerte"]
            )
            Autorizacion_Cremacion = random.choice([True, False])
            Permiso_Cremacion = random.choice([True, False])
            cursor.execute(
                """
                    INSERT INTO Documentos(
                        Certificado_Defuncion,
                        Autorizacion_Cremacion,
                        Permiso_Cremacion)
                    VALUES(?,?,?)""",
                (Certificado_Defuncion, Autorizacion_Cremacion, Permiso_Cremacion),
            )

    def Contratos(n: int):
        Detalles_Servicios = [
            "Embalming service for preservation of the deceased",
            "Viewing service for family and friends to pay respects",
            "Design and printing of personalized funeral programs",
            "Arrangement of floral displays for the funeral service",
            "Production of a memorial video to honor the deceased",
            "Handcrafted wooden urn with floral engravings",
            "Marble urn with intricate designs",
            "Brass urn with personalized inscription",
            "Ceramic urn with hand-painted motif",
            "Biodegradable urn made from eco-friendly materials",
            "Traditional coffin made from solid wood",
            "Casket with plush interior lining",
            "Steel coffin with reinforced structure",
            "Cardboard coffin with biodegradable lining",
            "Wicker coffin with natural finish",
            "Fiberglass coffin with sleek modern design",
            "Eco-friendly coffin made from sustainable materials",
            "Glass coffin for a unique display",
            "Customized coffin tailored to specific preferences",
            "Vintage-style coffin with ornate details",
            "Metallic coffin with polished finish",
            "Wooden coffin crafted from high-quality timber",
            "Pine coffin with minimalist design",
            "Mahogany coffin with rich, dark finish",
            "Bamboo coffin with eco-conscious construction",
        ]
        Parentesco = [
            "Madre",
            "Padre",
            "Hijo/a",
            "Abuelo/a",
            "Bisabuelo/a",
            "Tatarabuelo/a",
            "Sobrino/a",
            "Primo/a",
            "Tio/a",
            "Orto",
        ]
        Pago_Metodos = ["Efectivo", "Cheque", "Tarjeta - Credito", "Tarjeta - Debito"]
        # Create Contratos Table
        cursor.execute(
            """
        -- Contratos
        CREATE TABLE IF NOT EXISTS Contratos (
            Contrato_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Empleado_ID INTEGER NOT NULL,
            Cliente_ID INTEGER NOT NULL,
            Servicios_Elegido_ID INTEGER NOT NULL,
            Difunto_ID INTEGER NOT NULL,
            Documentos_ID INTEGER NOT NULL,
            Parentesco_Difunto TEXT NOT NULL,
            Fecha_Contrato DATE NOT NULL,
            Fecha_Servicio DATE NOT NULL,
            Metodo_Pago TEXT NOT NULL,
            Servicio_Detalles TEXT,
            Monto_Total DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (Documentos_ID) REFERENCES Documentos (Documentos_ID),
            FOREIGN KEY (Cliente_ID) REFERENCES Clientes (Cliente_ID),
            FOREIGN KEY (Servicios_Elegido_ID) REFERENCES Servicios_Elegidos (Contrato_ID),
            FOREIGN KEY (Difunto_ID) REFERENCES Difuntos (Difunto_ID),
            FOREIGN KEY (Empleado_ID) REFERENCES Empleados (Empleado_ID)
        )
        """
        )

        # Generate 50 records
        for _ in range(n):
            Documentos_ID = random.randint(1, 50)
            Cliente_ID = random.randint(1, 50)
            Servicios_Elegido_ID = random.randint(1, 50)
            Difunto_ID = random.randint(1, 50)
            Empleado_ID = random.randint(1, 50)
            Parentesco_Difunto = random.choice(Parentesco)
            Fecha_Contrato = fake.date_between(start_date="-1y", end_date="today")
            Fecha_Servicio = Fecha_Contrato + timedelta(days=random.randint(1, 30))
            Metodo_Pago = random.choice(Pago_Metodos)
            Servicio_Detalles = random.choice(Detalles_Servicios)
            Monto_Total = round(random.uniform(100, 10000), 2)

            # Insert the record into the Contratos table
            cursor.execute(
                """
                INSERT INTO Contratos (
                    Empleado_ID,
                    Cliente_ID,
                    Servicios_Elegido_ID,
                    Difunto_ID,
                    Documentos_ID,
                    Parentesco_Difunto,
                    Fecha_Contrato,
                    Fecha_Servicio,
                    Metodo_Pago,
                    Servicio_Detalles,
                    Monto_Total)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    Empleado_ID,
                    Cliente_ID,
                    Servicios_Elegido_ID,
                    Difunto_ID,
                    Documentos_ID,
                    Parentesco_Difunto,
                    Fecha_Contrato,
                    Fecha_Servicio,
                    Metodo_Pago,
                    Servicio_Detalles,
                    Monto_Total,
                ),
            )


# ____________________________________
# CREATE Tables
Database.Empleados(50)  # int
Database.Credenciales()
Database.Servicios()
Database.Clientes(50)  # int
Database.Difuntos(50)  # int
Database.Documentos(50)  # int
Database.Contratos(50)  # int
Database.Servicios_Elegidos(50)  # int

# Commit changes and close connection
conn.commit()
conn.close()
