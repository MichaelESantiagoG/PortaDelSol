import sqlite3 as sql
import pandas as pd
import random
import string
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
# Database.Empleados(50)  # number of records (int)
# Database.Credenciales()
# Database.Servicios()
# Database.Clientes(50)  # number of records (int)
# Database.Difuntos(50)  # number of records (int)
# Database.Documentos(50)  # number of records (int)
# Database.Contratos(50)  # number of records (int)
# Database.Servicios_Elegidos(120)  # number of records (int)
# Commit changes and close connection
conn.commit()
conn.close()


class Connection:
    def query1(query):
        conn = sql.connect("Database/portadelsol.db")
        # Execute the SQL query
        cursor = conn.execute(query)
        # Fetch the column names from the cursor description
        columns = [description[0] for description in cursor.description]
        # Fetch all rows from the cursor
        data = cursor.fetchall()
        # Convert the fetched data and column names to a DataFrame
        data_df = pd.DataFrame(data, columns=columns)
        # Return the DataFrame
        return data_df

    def query2(query):
        conn = sql.connect("Database/portadelsol.db")
        conn.execute(query)
        conn.commit()
        conn.close()

    def query3(query):
        conn = sql.connect("Database/portadelsol.db")
        cursor = conn.execute(query)
        data = cursor.fetchone()
        column_names = [description[0] for description in cursor.description]
        result_dict = dict(zip(column_names, data))
        return result_dict

    def query4(query):
        conn = sql.connect("Database/portadelsol.db")
        cursor = conn.execute(query)
        data = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        result_dict = dict(zip(column_names, data))
        return result_dict


class Select_All(Connection):

    def Credenciales():
        return Connection.query1(
            """
                SELECT
                    Usuario_ID,
                    Empleado_ID,
                    Usuario,
                    Contraseña,
                    Rol 
                FROM Credenciales"""
        )

    def Empleados():
        return Connection.query1(
            """
                SELECT
                    Empleado_ID,
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
                    Estado_Empleo
                FROM Empleados;"""
        )

    def Servicios():
        return Connection.query1(
            """
            SELECT Servicio_ID, Servicio_Nombre, Servicio_Precio FROM Servicios"""
        )

    def Servicios_Elegidos():
        return Connection.query1(
            """SELECT Servicios_Elegidos_ID, Contrato_ID, Servicio_ID
                FROM Servicios_Elegidos;"""
        )

    def CLientes():
        return Connection.query1(
            """
                SELECT Cliente_ID,
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
                    Descripcion
                FROM Clientes;"""
        )

    def Difuntos():
        return Connection.query1(
            """SELECT 
                    Difunto_ID,
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
                    Fecha_Defuncion    
                FROM Difuntos;      """
        )

    def Documentos():
        return Connection.query1(
            """
            SELECT 
                Documentos_ID,
                Certificado_Defuncion,
                Autorizacion_Cremacion,
                Permiso_Cremacion
            FROM Documentos"""
        )

    def Contratos():
        return Connection.query1(
            """
                SELECT
                    Contrato_ID,
                    Documentos_ID,
                    Cliente_ID,
                    Servicios_Elegido_ID,
                    Difunto_ID,
                    Empleado_ID,
                    Parentesco_Difunto,
                    Fecha_Contrato,
                    Fecha_Servicio,
                    Metodo_Pago,
                    Servicio_Detalles,
                    Monto_Total
                FROM Contratos;
                """
        )


# SELECT_ALL
print(
    # Select_All.Credenciales(),
    # Select_All.Empleados(),
    # Select_All.Servicios(),
    # Select_All.CLientes(),
    # Select_All.Difuntos(),
    # Select_All.Documentos(),
    # Select_All.Contratos(),
    # Select_All.Servicios_Elegidos(),
    end="\n",
)
# __________________________________
# print(Select_All.Servicios_Elegidos())


class Select(Connection):

    def Credenciales(id):
        return Connection.query3(
            f"""
                SELECT
                    Usuario_ID,
                    Empleado_ID,
                    Usuario,
                    Contraseña,
                    Rol 
                FROM Credenciales
                WHERE Usuario_ID = {id};"""
        )

    def Empleados(id):
        return Connection.query3(
            f"""
                SELECT
                    Empleado_ID,
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
                    Estado_Empleo
                FROM Empleados
                WHERE Empleado_ID = {id};"""
        )

    def Servicios(id):
        return Connection.query3(
            f"""
            SELECT Servicio_ID, Servicio_Nombre, Servicio_Precio 
            FROM Servicios
            WHERE Servicio_ID = {id};"""
        )

    def Servicios_Elegidos(id):
        return Connection.query1(
            f"""SELECT Servicios_Elegidos_ID, Contrato_ID, Servicio_ID
                FROM Servicios_Elegidos
                WHERE Contrato_ID = {id}"""
        )

    def CLientes(id):
        return Connection.query3(
            f"""
                SELECT Cliente_ID,
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
                    Descripcion
                FROM Clientes
                WHERE Cliente_ID = {id};"""
        )

    def Difuntos(id):
        return Connection.query3(
            f"""SELECT 
                    Difunto_ID,
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
                    Fecha_Defuncion    
                FROM Difuntos
                WHERE Difunto_ID = {id};      """
        )

    def Documentos(id):
        return Connection.query3(
            f"""
            SELECT 
                Documentos_ID,
                Certificado_Defuncion,
                Autorizacion_Cremacion,
                Permiso_Cremacion
            FROM Documentos
            WHERE Documentos_ID= {id};"""
        )

    def Contratos(id):
        return Connection.query3(
            f"""
                SELECT
                    Contrato_ID,
                    Documentos_ID,
                    Cliente_ID,
                    Servicios_Elegido_ID,
                    Difunto_ID,
                    Empleado_ID,
                    Parentesco_Difunto,
                    Fecha_Contrato,
                    Fecha_Servicio,
                    Metodo_Pago,
                    Servicio_Detalles,
                    Monto_Total
                FROM Contratos
                WHERE Contrato_ID = {id};
           """
        )


# SELECT
print(
    # Select.Credenciales(1),  # id
    # Select.Empleados(1),  # id
    # Select.Servicios(1),  # id
    # Select.CLientes(1),  # id
    # Select.Difuntos(1),  # id
    # Select.Documentos(1),  # id
    # Select.Contratos(1),  # id
    # Select.Servicios_Elegidos(1),
    end="\n",
    sep="\n\n",
)
# __________________________________
# print(Select.Servicios_Elegidos(1))  # Contrato_ID


class Insert(Connection):
    def Credenciales(data: dict):
        Connection.query2(
            f"""
            INSERT INTO Credenciales (Empleado_ID, Usuario, Contraseña, Rol)
            VALUES ({data['Empleado_ID']},'{data['Usuario']}','{data['Contraseña']}', {data['Rol']})
            """
        )

    def Empleado(data: dict):
        Connection.query2(
            f"""INSERT INTO Empleados (
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
                    Estado_Empleo
            )
            VALUES (
                '{data["Posicion"]}',
                '{data["Nombre"]}',
                '{data["Apellido_Paterno"]}',
                '{data["Apellido_Materno"]}',
                '{data["Genero"]}',
                '{data["Correo_Electronico"]}',
                '{data["Celular"]}',
                '{data["Celular_2"]}',
                '{data["Direccion"]}',
                '{data["Fecha_Nacimiento"]}',
                '{data["Lugar_Nacimiento"]}',
                '{data["Seguro_Social"]}',
                '{data["Licencia"]}',
                '{data["Servicio_Militar"]}',
                '{data["Estado_Civil"]}',
                '{data["Estado_Empleo"]}')""",
        )

    def Servicio(data: dict):
        Connection.query2(
            f"""
            INSERT INTO Servicios (Servicio_Nombre, Servicio_Precio)
            VALUES ('{data['Servicio_Nombre']}', {data['Servicio_Precio']})
            """
        )

    def Servicios_Elegidos(data: list):
        for service_id in data["Servicio_ID"]:
            Connection.query2(
                f"""INSERT INTO Servicios_Elegidos(Contrato_ID, Servicio_ID)
                    VALUES({data["Contrato_ID"]}, {service_id})"""
            )

    def Cliente(data: dict):
        Connection.query2(
            f"""INSERT INTO Clientes (
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
                    Descripcion
            )
            VALUES (
                '{data["Ocupacion"]}',
                '{data["Nombre"]}',
                '{data["Apellido_Paterno"]}',
                '{data["Apellido_Materno"]}',
                '{data["Genero"]}',
                '{data["Correo_Electronico"]}',
                '{data["Celular"]}',
                '{data["Celular_2"]}',
                '{data["Direccion"]}',
                '{data["Fecha_Nacimiento"]}',
                '{data["Lugar_Nacimiento"]}',
                '{data["Seguro_Social"]}',
                '{data["Licencia"]}',
                '{data["Servicio_Militar"]}',
                '{data["Estado_Civil"]}',
                '{data["Descripcion"]}'
            )"""
        )

    def Difunto(data: dict):
        Connection.query2(
            f"""INSERT INTO Difuntos (
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
                    Fecha_Defuncion
            )
            VALUES (
                '{data["Nombre"]}',
                '{data["Apellido_Paterno"]}',
                '{data["Apellidp_Materno"]}',
                '{data["Genero"]}',
                '{data["Estado_Civil"]}',
                '{data["Nombre_Padre"]}',
                '{data["Nombre_Madre"]}',
                '{data["Seguro_Social"]}',
                '{data["Servicio_Militar"]}',
                {data["Edad"]},
                '{data["Lugar_Nacimiento"]}',
                '{data["Fecha_Nacimiento"]}',
                '{data["Fecha_Defuncion"]}'
            )"""
        )

    def Documentos(data: dict):
        Connection.query2(
            f"""
            INSERT INTO Documentos (
                Certificado_Defuncion,
                Autorizacion_Cremacion,
                Permiso_Cremacion
            )
            VALUES (
                '{data['Certificado_Defuncion']}',
                '{data['Autorizacion_Cremacion']}',
                '{data['Permiso_Cremacion']}'
            )
            """
        )

    def Contrato(data: dict):
        Connection.query2(
            f"""
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
                Monto_Total
            )
            VALUES (
                {data['Empleado_ID']},
                {data['Cliente_ID']},
                {data['Servicios_Elegido_ID']},
                {data['Difunto_ID']},
                {data['Documentos_ID']},
                '{data['Parentesco_Difunto']}',
                '{data['Fecha_Contrato']}',
                '{data['Fecha_Servicio']}',
                '{data['Metodo_Pago']}',
                '{data['Servicio_Detalles']}',
                {data['Monto_Total']}
            )
            """
        )


# INSERT
Employee = {
    "Posicion": "None",
    "Nombre": "None",
    "Apellido_Paterno": "None",
    "Apellido_Materno": "None",
    "Genero": "None",
    "Correo_Electronico": "None",
    "Celular": "None",
    "Celular_2": "None",
    "Direccion": "None",
    "Fecha_Nacimiento": "None",
    "Lugar_Nacimiento": "None",
    "Seguro_Social": "None",
    "Licencia": "None",
    "Servicio_Militar": "None",
    "Estado_Civil": "None",
    "Estado_Empleo": "None",
}
Client = {
    "Ocupacion": "None",
    "Nombre": "None",
    "Apellido_Paterno": "None",
    "Apellido_Materno": "None",
    "Genero": "None",
    "Correo_Electronico": "None",
    "Celular": "None",
    "Celular_2": "None",
    "Direccion": "None",
    "Fecha_Nacimiento": "None",
    "Lugar_Nacimiento": "None",
    "Seguro_Social": "None",
    "Licencia": "None",
    "Servicio_Militar": "None",
    "Estado_Civil": "None",
    "Descripcion": "None",
}
Servicio = {
    "Servicio_Nombre": "None",
    "Servicio_Precio": 0,
}
Difunto = {
    "Nombre": "None",
    "Apellido_Paterno": "None",
    "Apellidp_Materno": "None",
    "Genero": "None",
    "Estado_Civil": "None",
    "Nombre_Padre": "None",
    "Nombre_Madre": "None",
    "Seguro_Social": "None",
    "Servicio_Militar": "None",
    "Edad": 1,
    "Lugar_Nacimiento": "None",
    "Fecha_Nacimiento": "",
    "Fecha_Defuncion": "",
}

Documento = {
    "Certificado_Defuncion": "None",
    "Autorizacion_Cremacion": True,
    "Permiso_Cremacion": True,
}
Credenciales = {
    "Empleado_ID": 1,
    "Usuario": "None",
    "Contraseña": "None",
    "Rol": 0,
}
Contrato = {
    "Empleado_ID": 1,
    "Cliente_ID": 1,
    "Servicios_Elegido_ID": 1,
    "Difunto_ID": 1,
    "Documentos_ID": 1,
    "Parentesco_Difunto": "None",
    "Fecha_Contrato": "None",
    "Fecha_Servicio": "None",
    "Metodo_Pago": "None",
    "Servicio_Detalles": "None",
    "Monto_Total": 0,
}
Servicios_Elegidos = {
    "Contrato_ID": 5,
    "Servicio_ID": [4, 3],
}

# Insert.Empleado(Employee)
# Insert.Cliente(Client)
# Insert.Servicio(Servicio)
# Insert.Difunto(Difunto)
# Insert.Documentos(Documento)
# Insert.Credenciales(Credenciales)
# Insert.Contrato(Contrato)
# Insert.Servicios_Elegidos(Servicios_Elegidos)


# __________________________________


class Delete(Connection):
    def Empleado(id):
        Connection.query2(f"DELETE FROM Empleados WHERE Empleado_ID = {id};")

    def Credenciales(id):
        Connection.query2(f"DELETE FROM Credenciales WHERE Usuario_ID = {id};")

    def Servicio(id):
        Connection.query2(f"DELETE FROM Servicios WHERE Servicio_ID = {id};")

    def Cliente(id):
        Connection.query2(f"DELETE FROM Clientes WHERE Cliente_ID = {id};")

    def Difunto(id):
        Connection.query2(f"DELETE FROM Difuntos WHERE Difunto_ID = {id};")

    def Documentos(id):
        Connection.query2(f"DELETE FROM Documentos WHERE Documentos_ID = {id};")

    def Contrato(id):
        Connection.query2(f"DELETE FROM Contratos WHERE Contrato_ID = {id};")

    def Servicios_Elegidos(id):
        Connection.query2(f"DELETE FROM Servicios_Elegidos WHERE Contrato_ID = {id};")


id = 1
# Delete.Empleado(id)
# Delete.Credenciales(id)
# Delete.Servicio(id)
# Delete.Cliente(id)
# Delete.Difunto(id)
# Delete.Documentos(id)
# Delete.Contrato(id)


class Update(Connection):
    def Credenciales(id: int, data: dict):
        Connection.query2(
            f"""
            UPDATE Credenciales 
            SET Usuario = '{data['Usuario']}', 
                Contraseña = '{data['Contraseña']}', 
                Rol = {data['Rol']} 
            WHERE Empleado_ID = {id}
            """
        )

    def Empleado(id: int, data: dict):
        Connection.query2(
            f"""UPDATE Empleados 
                SET Posicion = '{data["Posicion"]}',
                    Nombre = '{data["Nombre"]}',
                    Apellido_Paterno = '{data["Apellido_Paterno"]}',
                    Apellido_Materno = '{data["Apellido_Materno"]}',
                    Genero = '{data["Genero"]}',
                    Correo_Electronico = '{data["Correo_Electronico"]}',
                    Celular = '{data["Celular"]}',
                    Celular_2 = '{data["Celular_2"]}',
                    Direccion = '{data["Direccion"]}',
                    Fecha_Nacimiento = '{data["Fecha_Nacimiento"]}',
                    Lugar_Nacimiento = '{data["Lugar_Nacimiento"]}',
                    Seguro_Social = '{data["Seguro_Social"]}',
                    Licencia = '{data["Licencia"]}',
                    Servicio_Militar = '{data["Servicio_Militar"]}',
                    Estado_Civil = '{data["Estado_Civil"]}',
                    Estado_Empleo = '{data["Estado_Empleo"]}'
                WHERE Empleado_ID = {id}
        """
        )

    def Servicio(id: int, data: dict):
        Connection.query2(
            f"""
UPDATE Servicios SET Servicio_Nombre = '{data['Servicio_Nombre']}', Servicio_Precio = {data['Servicio_Precio']} WHERE Servicio_ID = {id};
"""
        )

    def Cliente(id: int, data: dict):
        Connection.query2(
            f"""
            UPDATE Clientes
            SET Ocupacion = '{data['Ocupacion']}',
                Nombre = '{data['Nombre']}',
                Apellido_Paterno = '{data['Apellido_Paterno']}',
                Apellido_Materno = '{data['Apellido_Materno']}',
                Genero = '{data['Genero']}',
                Correo_Electronico = '{data['Correo_Electronico']}',
                Celular = '{data['Celular']}',
                Celular_2 = '{data['Celular_2']}',
                Direccion = '{data['Direccion']}',
                Fecha_Nacimiento = '{data['Fecha_Nacimiento']}',
                Lugar_Nacimiento = '{data['Lugar_Nacimiento']}',
                Seguro_Social = '{data['Seguro_Social']}',
                Licencia = '{data['Licencia']}',
                Servicio_Militar = '{data['Servicio_Militar']}',
                Estado_Civil = '{data['Estado_Civil']}',
                Descripcion = '{data['Descripcion']}'
            WHERE Cliente_ID = {id};"""
        )

    def Difunto(id: int, data: dict):
        Connection.query2(
            f"""
            UPDATE Difuntos
            SET 
                Nombre = '{data["Nombre"]}',
                Apellido_Paterno = '{data["Apellido_Paterno"]}',
                Apellidp_Materno = '{data["Apellidp_Materno"]}',
                Genero = '{data["Genero"]}',
                Estado_Civil = '{data["Estado_Civil"]}',
                Nombre_Padre = '{data["Nombre_Padre"]}',
                Nombre_Madre = '{data["Nombre_Madre"]}',
                Seguro_Social = '{data["Seguro_Social"]}',
                Servicio_Militar = '{data["Servicio_Militar"]}',
                Edad = {data["Edad"]},
                Lugar_Nacimiento = '{data["Lugar_Nacimiento"]}',
                Fecha_Nacimiento = '{data["Fecha_Nacimiento"]}',
                Fecha_Defuncion = '{data["Fecha_Defuncion"]}'
            WHERE 
                Difunto_ID = {id};
            """
        )

    def Documentos(id: int, data: dict):
        Connection.query2(
            f"""
            UPDATE Documentos
            SET 
                Certificado_Defuncion = '{data['Certificado_Defuncion']}',
                Autorizacion_Cremacion = '{data['Autorizacion_Cremacion']}',
                Permiso_Cremacion = '{data['Permiso_Cremacion']}'
            WHERE 
                Documentos_ID = {id};
            """
        )

    def Servicios_Elegidos(id: int, data: list):
        # Delete>Insert
        Delete.Servicios_Elegidos(id)
        Insert.Servicios_Elegidos(data)

    def Contrato(id: int, data: dict):
        Connection.query2(
            f"""
            UPDATE Contratos
            SET 
                Empleado_ID = {data['Empleado_ID']},
                Cliente_ID = {data['Cliente_ID']},
                Servicios_Elegido_ID = {data['Servicios_Elegido_ID']},
                Difunto_ID = {data['Difunto_ID']},
                Documentos_ID = {data['Documentos_ID']},
                Parentesco_Difunto = '{data['Parentesco_Difunto']}',
                Fecha_Contrato = '{data['Fecha_Contrato']}',
                Fecha_Servicio = '{data['Fecha_Servicio']}',
                Metodo_Pago = '{data['Metodo_Pago']}',
                Servicio_Detalles = '{data['Servicio_Detalles']}',
                Monto_Total = {data['Monto_Total']}
            WHERE 
                Contrato_ID = {id};
            """
        )


id = 2
Cuenta = {
    "Usuario": "Usuario",
    "Contraseña": "Contraseña",
    "Rol": 0,
}
Empleado = {
    "Posicion": "Posicion",
    "Nombre": "Nombre",
    "Apellido_Paterno": "Apellido_Paterno",
    "Apellido_Materno": "Apellido_Materno",
    "Genero": "Genero",
    "Correo_Electronico": "Correo_Electronico",
    "Celular": "Celular",
    "Celular_2": "Celular_2",
    "Direccion": "Direccion",
    "Fecha_Nacimiento": "Fecha_Nacimiento",
    "Lugar_Nacimiento": "Lugar_Nacimiento",
    "Seguro_Social": "Seguro_Social",
    "Licencia": "Licencia",
    "Servicio_Militar": "Servicio_Militar",
    "Estado_Civil": "Estado_Civil",
    "Estado_Empleo": "Estado_Empleo",
}
Servicio = {"Servicio_Nombre": "Servicio_Nombre", "Servicio_Precio": 0}
Cliente = {
    "Ocupacion": "Ocupacion",
    "Nombre": "Nombre",
    "Apellido_Paterno": "Apellido_Paterno",
    "Apellido_Materno": "Apellido_Materno",
    "Genero": "Genero",
    "Correo_Electronico": "Correo_Electronico",
    "Celular": "Celular",
    "Celular_2": "Celular_2",
    "Direccion": "Direccion",
    "Fecha_Nacimiento": "Fecha_Nacimiento",
    "Lugar_Nacimiento": "Lugar_Nacimiento",
    "Seguro_Social": "Seguro_Social",
    "Licencia": "Licencia",
    "Servicio_Militar": "Servicio_Militar",
    "Estado_Civil": "Estado_Civil",
    "Descripcion": "Descripcion",
}
Difunto = {
    "Nombre": "Nombre",
    "Apellido_Paterno": "Apellido_Paterno",
    "Apellidp_Materno": "Apellidp_Materno",
    "Genero": "Genero",
    "Estado_Civil": "Estado_Civil",
    "Nombre_Padre": "Nombre_Padre",
    "Nombre_Madre": "Nombre_Madre",
    "Seguro_Social": "Seguro_Social",
    "Servicio_Militar": "Servicio_Militar",
    "Edad": 30,
    "Lugar_Nacimiento": "New Lugar_Nacimiento",
    "Fecha_Nacimiento": "2024-01-01",
    "Fecha_Defuncion": "2025-01-01",
}  # Update.Credenciales(id, Cuenta)
Documentos = {
    "Certificado_Defuncion": "New Certificate",
    "Autorizacion_Cremacion": False,
    "Permiso_Cremacion": True,
}
Servicios_Elegidos = {
    "Contrato_ID": id,  # Specify the Contrato_ID for which you want to update Servicios_Elegidos
    "Servicio_ID": [9, 8, 7],  # Specify the list of Servicio_IDs you want to update
}
Contrato = {
    "Empleado_ID": 1,
    "Cliente_ID": 1,
    "Servicios_Elegido_ID": 1,
    "Difunto_ID": 1,
    "Documentos_ID": 1,
    "Parentesco_Difunto": "New Parentesco",
    "Fecha_Contrato": "2024-05-05",
    "Fecha_Servicio": "2024-05-06",
    "Metodo_Pago": "Credit Card",
    "Servicio_Detalles": "New Details",
    "Monto_Total": 1000,
}
# Update.Empleado(id, Empleado)
# Update.Servicio(id, Servicio)
# Update.Cliente(id, Cliente)
# Update.Difunto(id, Difunto)
# Update.Documentos(id, Documentos)
# Update.Servicios_Elegidos(id, Servicios_Elegidos)
# Update.Contrato(id, Contrato)

print("Records inserted successfully.")
