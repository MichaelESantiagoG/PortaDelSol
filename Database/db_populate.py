import sqlite3
import random
import string
import pandas as pd
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Connect to SQLite database
conn = sqlite3.connect("PortaDelSol/Database/portadelsol.db")
cursor = conn.cursor()


def Empleados():
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
        Correo_Electronico VARCHAR(255) NOT NULL,
        Celular VARCHAR(10) NOT NULL,
        Celular_2 TEXT,
        Direccion TEXT NOT NULL,
        Seguro_Social VARCHAR(9) NOT NULL,
        Fecha_De_Nacimiento DATE NOT NULL,
        Licencia VARCHAR(20),
        Numero_De_Servicio_Militar VARCHAR(11),
        Estado_Civil TEXT,
        Estado_De_Empleo TEXT NOT NULL DEFAULT 'Activo');"""
    )

    # # Generate 50 records for Empleados table
    for _ in range(50):
        nombre = fake.first_name()
        apellido_paterno = fake.last_name()
        apellido_materno = fake.last_name()
        posicion = fake.job()
        correo_electronico = fake.email()
        celular = fake.phone_number()[:10]  # Ensure max length of 10
        celular_2 = fake.phone_number()[:10] if random.choice([True, False]) else None
        direccion = fake.address()
        seguro_social = "".join(random.choices("0123456789", k=9))
        fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=65)
        licencia = (
            "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=7))
            if random.choice([True, False])
            else None
        )
        estado_civil = random.choice(["Soltero", "Casado", "Divorciado", "Viudo"])

        cursor.execute(
            """
        INSERT INTO Empleados (Posicion, Nombre, Apellido_Paterno, Apellido_Materno, Correo_Electronico, Celular, Celular_2, Direccion, Seguro_Social, Fecha_De_Nacimiento, Licencia, Estado_Civil)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                posicion,
                nombre,
                apellido_paterno,
                apellido_materno,
                correo_electronico,
                celular,
                celular_2,
                direccion,
                seguro_social,
                fecha_nacimiento,
                licencia,
                estado_civil,
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
        Posicion INTEGER NOT NULL DEFAULT 1,
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
    for _ in range(50):
        servicio_nombre = fake.bs()  # Generate a business service name
        servicio_precio = round(
            random.uniform(100, 2000), 2
        )  # Generate a random price between 100 and 2000

        cursor.execute(
            """
        INSERT INTO Servicios (Servicio_Nombre, Servicio_Precio)
        VALUES (?, ?)
        """,
            (servicio_nombre, servicio_precio),
        )


def Clientes():
    # Create Clientes Table
    cursor.execute(
        """
    -- Clientes
    CREATE TABLE IF NOT EXISTS Clientes (
        Cliente_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT NOT NULL,
        Apellido_Paterno TEXT NOT NULL,
        Apellido_Materno TEXT NOT NULL,
        Fecha_De_Nacimiento DATE NOT NULL,
        Lugar_De_Nacimiento TEXT NOT NULL,
        Genero TEXT,
        Celular VARCHAR(15) NOT NULL,
        Celular_2 VARCHAR(15),
        Direccion TEXT NOT NULL,
        Licencia VARCHAR(10),
        Seguro_Social VARCHAR(11) NOT NULL,
        Numero_De_Servicio_Militar VARCHAR(11),
        Descripcion TEXT
    );"""
    )
    # Generate 50 records for Clientes table
    for _ in range(50):
        nombre = fake.first_name()
        apellido_paterno = fake.last_name()
        apellido_materno = fake.last_name()
        fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=90)
        lugar_nacimiento = fake.city()
        genero = random.choice(["Masculino", "Femenino"])
        celular = fake.phone_number()
        celular_2 = fake.phone_number() if random.choice([True, False]) else None
        direccion = fake.address()
        licencia = (
            fake.random_number(digits=8) if random.choice([True, False]) else None
        )
        seguro_social = fake.random_number(digits=9)
        servicio_militar = (
            fake.random_number(digits=8) if random.choice([True, False]) else None
        )
        descripcion = fake.text(max_nb_chars=200)

        cursor.execute(
            """
        INSERT INTO Clientes (Nombre, Apellido_Paterno, Apellido_Materno, Fecha_De_Nacimiento, Lugar_De_Nacimiento, Genero, Celular, Celular_2, Direccion, Licencia, Seguro_Social, Numero_De_Servicio_Militar, Descripcion)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                nombre,
                apellido_paterno,
                apellido_materno,
                fecha_nacimiento,
                lugar_nacimiento,
                genero,
                celular,
                celular_2,
                direccion,
                licencia,
                seguro_social,
                servicio_militar,
                descripcion,
            ),
        )


Empleados()
Credenciales()
Servicios()
Clientes()

# Commit changes and close connection
conn.commit()
conn.close()

print("Records inserted successfully.")
