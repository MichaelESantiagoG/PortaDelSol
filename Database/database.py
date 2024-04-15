import sqlite3

# Connect to SQLite database (creates a new one if not exists)
conn = sqlite3.connect("Database/portadelsol.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute SQL commands to create tables
# (Use the SQL statements from the previous response)
cursor.execute(
    """
-- Credenciales
CREATE TABLE Credenciales (
    Usuario_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Empleado_ID INTEGER NOT NULL,
    Usuario TEXT NOT NULL,
    Contraseña TEXT NOT NULL,
    Posicion INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (Empleado_ID) REFERENCES Empleados (Empleado_ID)
);"""
)
cursor.execute(
    """
INSERT INTO Credenciales (Empleado_ID, Usuario, Contraseña, Posicion) VALUES
(1, 'user1', 'password1', 0),
(2, 'user2', 'password2', 1),
(3, 'user3', 'password3', 2),
(4, 'user4', 'password4', 0),
(5, 'user5', 'password5', 1),
(6, 'user6', 'password6', 2),
(7, 'user7', 'password7', 0),
(8, 'user8', 'password8', 1),
(9, 'user9', 'password9', 2),
(10, 'user10', 'password10', 0),
(11, 'user11', 'password11', 1),
(12, 'user12', 'password12', 2),
(13, 'user13', 'password13', 0),
(14, 'user14', 'password14', 1),
(15, 'user15', 'password15', 2),
(16, 'user16', 'password16', 0),
(17, 'user17', 'password17', 1),
(18, 'user18', 'password18', 2),
(19, 'user19', 'password19', 0),
(20, 'user20', 'password20', 1),
(21, 'user21', 'password21', 2),
(22, 'user22', 'password22', 0),
(23, 'user23', 'password23', 1),
(24, 'user24', 'password24', 2),
(25, 'user25', 'password25', 0),
(26, 'user26', 'password26', 1),
(27, 'user27', 'password27', 2),
(28, 'user28', 'password28', 0),
(29, 'user29', 'password29', 1),
(30, 'user30', 'password30', 2),
(31, 'user31', 'password31', 0),
(32, 'user32', 'password32', 1),
(33, 'user33', 'password33', 2),
(34, 'user34', 'password34', 0),
(35, 'user35', 'password35', 1),
(36, 'user36', 'password36', 2),
(37, 'user37', 'password37', 0),
(38, 'user38', 'password38', 1),
(39, 'user39', 'password39', 2),
(40, 'user40', 'password40', 0),
(41, 'user41', 'password41', 1),
(42, 'user42', 'password42', 2),
(43, 'user43', 'password43', 0),
(44, 'user44', 'password44', 1),
(45, 'user45', 'password45', 2),
(46, 'user46', 'password46', 0),
(47, 'user47', 'password47', 1),
(48, 'user48', 'password48', 2),
(49, 'user49', 'password49', 0),
(50, 'user50', 'password50', 1);
"""
)

cursor.execute(
    """
-- Empleados
CREATE TABLE Empleados (
    Empleado_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    Apellido_Paterno TEXT NOT NULL,
    Apellido_Materno TEXT NOT NULL,
    Celular TEXT NOT NULL,
    Celular_2 TEXT,
    Direccion TEXT NOT NULL,
    Ocupacion TEXT NOT NULL,
    Seguro_Social TEXT NOT NULL,
    Correo_Electronico TEXT NOT NULL,
    Fecha_De_Nacimiento DATE NOT NULL,
    Licencia TEXT,
    Estado_Civil TEXT,
    EstadoDeEmpleo TEXT NOT NULL DEFAULT 'Activo'
);"""
)
cursor.execute(
    """
INSERT INTO Empleados (Nombre, Apellido_Paterno, Apellido_Materno, Celular, Celular_2, Direccion, Ocupacion, Seguro_Social, Correo_Electronico, Fecha_De_Nacimiento, Licencia, Estado_Civil, EstadoDeEmpleo) VALUES
('John', 'Doe', 'Smith', '1234567890', '0987654321', '123 Main St', 'Engineer', '123-45-6789', 'john@example.com', '1990-01-01', '123ABC', 'Single', 'Activo'),
('Jane', 'Doe', 'Johnson', '9876543210', '0123456789', '456 Elm St', 'Manager', '987-65-4321', 'jane@example.com', '1985-05-10', '456DEF', 'Married', 'Activo'),
('Michael', 'Smith', 'Brown', '5551112222', '3334445555', '789 Oak St', 'Technician', '555-11-2222', 'michael@example.com', '1988-12-15', '789GHI', 'Divorced', 'Activo'),
('Emily', 'Johnson', 'Davis', '7778889999', '4445556666', '321 Pine St', 'Developer', '777-88-9999', 'emily@example.com', '1992-07-20', 'ABC123', 'Single', 'Activo'),
('Christopher', 'Brown', 'Wilson', '9990001111', '6667778888', '654 Maple St', 'Designer', '999-00-1111', 'christopher@example.com', '1983-03-25', 'DEF456', 'Married', 'Activo'),
('Jessica', 'Davis', 'Martinez', '3334445555', '2223334444', '987 Cedar St', 'Analyst', '333-44-5555', 'jessica@example.com', '1995-09-05', 'GHI789', 'Single', 'Activo'),
('Matthew', 'Wilson', 'Anderson', '1112223333', '8889990000', '753 Birch St', 'Engineer', '111-22-3333', 'matthew@example.com', '1990-11-12', 'JKL012', 'Married', 'Activo'),
('Amanda', 'Martinez', 'Taylor', '4445556666', '0001112222', '852 Walnut St', 'Manager', '444-55-6666', 'amanda@example.com', '1987-04-30', 'MNO345', 'Divorced', 'Activo'),
('David', 'Anderson', 'Hernandez', '6667778888', '1112223333', '369 Oak St', 'Technician', '666-77-8888', 'david@example.com', '1982-08-22', 'PQR678', 'Single', 'Activo'),
('Sarah', 'Taylor', 'Garcia', '2223334444', '5556667777', '963 Elm St', 'Developer', '222-33-4444', 'sarah@example.com', '1993-06-17', 'STU901', 'Married', 'Activo'),
('Daniel', 'Hernandez', 'Rodriguez', '8889990000', '3334445555', '147 Pine St', 'Designer', '888-99-0000', 'daniel@example.com', '1986-01-08', 'VWX234', 'Single', 'Activo'),
('Lauren', 'Garcia', 'Lopez', '0001112222', '6667778888', '258 Maple St', 'Analyst', '000-11-2222', 'lauren@example.com', '1991-04-25', 'YZA567', 'Married', 'Activo'),
('Ryan', 'Rodriguez', 'Perez', '5556667777', '9990001111', '369 Cedar St', 'Engineer', '555-66-7777', 'ryan@example.com', '1984-10-03', 'BCD890', 'Divorced', 'Activo'),
('Ashley', 'Lopez', 'Sanchez', '3334445555', '2223334444', '852 Oak St', 'Manager', '333-44-5555', 'ashley@example.com', '1996-12-19', 'EFG123', 'Single', 'Activo'),
('Kevin', 'Perez', 'Torres', '7778889999', '4445556666', '963 Pine St', 'Technician', '777-88-9999', 'kevin@example.com', '1989-07-14', 'HIJ456', 'Married', 'Activo'),
('Rachel', 'Sanchez', 'Gonzalez', '1112223333', '8889990000', '147 Elm St', 'Developer', '111-22-3333', 'rachel@example.com', '1994-03-08', 'KLM789', 'Single', 'Activo'),
('Brandon', 'Torres', 'Rivera', '9990001111', '6667778888', '258 Oak St', 'Designer', '999-00-1111', 'brandon@example.com', '1981-12-27', 'NOP012', 'Married', 'Activo'),
('Megan', 'Gonzalez', 'Vargas', '4445556666', '0001112222', '369 Pine St', 'Analyst', '444-55-6666', 'megan@example.com', '1997-08-10', 'QRS345', 'Single', 'Activo'),
('Kyle', 'Rivera', 'Ortiz', '2223334444', '5556667777', '852 Cedar St', 'Engineer', '222-33-4444', 'kyle@example.com', '1992-01-31', 'TUV678', 'Married', 'Activo'),
('Stephanie', 'Vargas', 'Cruz', '8889990000', '3334445555', '963 Elm St', 'Manager', '888-99-0000', 'stephanie@example.com', '1985-06-24', 'WXY901', 'Divorced', 'Activo'),
('Nicholas', 'Ortiz', 'Reyes', '5556667777', '9990001111', '147 Pine St', 'Technician', '555-66-7777', 'nicholas@example.com', '1988-11-14', 'ZAB234', 'Single', 'Activo'),
('Alexis', 'Cruz', 'Gomez', '3334445555', '2223334444', '258 Maple St', 'Developer', '333-44-5555', 'alexis@example.com', '1993-07-28', 'BCD567', 'Married', 'Activo'),
('Tyler', 'Reyes', 'Diaz', '9990001111', '6667778888', '369 Oak St', 'Designer', '999-00-1111', 'tyler@example.com', '1982-02-18', 'EFG890', 'Single', 'Activo'),
('Kayla', 'Gomez', 'Torres', '7778889999', '4445556666', '852 Elm St', 'Analyst', '777-88-9999', 'kayla@example.com', '1995-09-03', 'HIJ123', 'Married', 'Activo'),
('Zachary', 'Diaz', 'Ortega', '1112223333', '8889990000', '963 Oak St', 'Engineer', '111-22-3333', 'zachary@example.com', '1990-04-22', 'KLM456', 'Divorced', 'Activo'),
('Samantha', 'Torres', 'Santiago', '4445556666', '0001112222', '147 Pine St', 'Manager', '444-55-6666', 'samantha@example.com', '1983-12-15', 'NOP789', 'Single', 'Activo'),
('Joseph', 'Ortega', 'Morales', '2223334444', '5556667777', '258 Cedar St', 'Technician', '222-33-4444', 'joseph@example.com', '1996-11-05', 'QRS012', 'Married', 'Activo'),
('Hannah', 'Santiago', 'Gutierrez', '8889990000', '3334445555', '369 Elm St', 'Developer', '888-99-0000', 'hannah@example.com', '1987-10-27', 'TUV345', 'Single', 'Activo'),
('Andrew', 'Morales', 'Nunez', '5556667777', '9990001111', '852 Pine St', 'Designer', '555-66-7777', 'andrew@example.com', '1991-02-09', 'WXY678', 'Married', 'Activo'),
('Taylor', 'Gutierrez', 'Ruiz', '3334445555', '2223334444', '963 Oak St', 'Analyst', '333-44-5555', 'taylor@example.com', '1984-08-31', 'ZAB901', 'Divorced', 'Activo'),
('Olivia', 'Ruiz', 'Castillo', '9990001111', '6667778888', '147 Elm St', 'Engineer', '999-00-1111', 'olivia@example.com', '1997-05-14', 'CDE234', 'Single', 'Activo'),
('James', 'Castillo', 'Vasquez', '7778889999', '4445556666', '258 Cedar St', 'Manager', '777-88-9999', 'james@example.com', '1989-01-07', 'FGH567', 'Married', 'Activo'),
('Emma', 'Vasquez', 'Santos', '2223334444', '5556667777', '369 Oak St', 'Technician', '222-33-4444', 'emma@example.com', '1992-06-20', 'IJK890', 'Single', 'Activo'),
('Benjamin', 'Santos', 'Flores', '8889990000', '3334445555', '852 Pine St', 'Developer', '888-99-0000', 'benjamin@example.com', '1985-03-12', 'LMN123', 'Married', 'Activo'),
('Madison', 'Flores', 'Marquez', '5556667777', '9990001111', '963 Elm St', 'Designer', '555-66-7777', 'madison@example.com', '1990-12-25', 'OPQ456', 'Divorced', 'Activo'),
('Elijah', 'Marquez', 'Guerrero', '3334445555', '2223334444', '147 Pine St', 'Analyst', '333-44-5555', 'elijah@example.com', '1993-10-08', 'RST789', 'Single', 'Activo'),
('Chloe', 'Guerrero', 'Delgado', '9990001111', '6667778888', '258 Cedar St', 'Manager', '999-00-1111', 'chloe@example.com', '1986-07-21', 'UVW012', 'Married', 'Activo'),
('Carter', 'Delgado', 'Jimenez', '7778889999', '4445556666', '369 Oak St', 'Technician', '777-88-9999', 'carter@example.com', '1991-04-15', 'XYZ345', 'Single', 'Activo'),
('Avery', 'Jimenez', 'Moreno', '2223334444', '5556667777', '852 Elm St', 'Developer', '222-33-4444', 'avery@example.com', '1994-11-28', 'BCD678', 'Married', 'Activo'),
('Jackson', 'Moreno', 'Rojas', '8889990000', '3334445555', '963 Oak St', 'Designer', '888-99-0000', 'jackson@example.com', '1987-02-03', 'EFG901', 'Divorced', 'Activo'),
('Mia', 'Rojas', 'Estrada', '5556667777', '9990001111', '147 Elm St', 'Analyst', '555-66-7777', 'mia@example.com', '1996-09-16', 'HIJ234', 'Single', 'Activo'),
('Ethan', 'Estrada', 'Alvarez', '3334445555', '2223334444', '258 Cedar St', 'Engineer', '333-44-5555', 'ethan@example.com', '1988-06-09', 'KLM567', 'Married', 'Activo'),
('Natalie', 'Alvarez', 'Silva', '9990001111', '6667778888', '369 Oak St', 'Technician', '999-00-1111', 'natalie@example.com', '1993-01-22', 'NOP890', 'Single', 'Activo'),
('Logan', 'Silva', 'Chavez', '7778889999', '4445556666', '852 Pine St', 'Developer', '777-88-9999', 'logan@example.com', '1980-08-05', 'QRS123', 'Married', 'Activo'),
('Lily', 'Chavez', 'Gomez', '2223334444', '5556667777', '963 Elm St', 'Designer', '222-33-4444', 'lily@example.com', '1995-07-18', 'TUV456', 'Divorced', 'Activo');
"""
)

cursor.execute(
    """
-- Servicios
CREATE TABLE Servicios (
    Servicio_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Servicio_Nombre TEXT NOT NULL,
    Servicio_Precio DECIMAL(6,2) NOT NULL
);"""
)

cursor.execute(
    """

INSERT INTO Servicios (Servicio_Nombre, Servicio_Precio) VALUES
('Funeral básico', 1500.00),
('Servicio de cremación', 1000.00),
('Traslado del cuerpo', 500.00),
('Preparación del cuerpo', 700.00),
('Embalaje del cuerpo', 300.00),
('Servicio de velatorio', 800.00),
('Servicio de entierro', 1200.00),
('Floristería', 400.00),
('Honorarios del director de funeraria', 200.00),
('Gastos administrativos', 100.00);
"""
)

cursor.execute(
    """
-- Servicios_Elegidos
CREATE TABLE Servicios_Elegidos (
    Servicios_Elegidos_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Servicio_ID INTEGER NOT NULL,
    Detalles_Servicios TEXT NOT NULL,
    FOREIGN KEY (Servicio_ID) REFERENCES Servicios (Servicio_ID)
);"""
)

cursor.execute(
    """
INSERT INTO Servicios_Elegidos (Servicio_ID, Detalles_Servicios) VALUES
(1, 'Funeral básico para el Sr. Smith'),
(2, 'Servicio de cremación para la Sra. Johnson'),
(3, 'Traslado del cuerpo para el Sr. Brown'),
(4, 'Preparación del cuerpo para el Sr. Wilson'),
(5, 'Embalaje del cuerpo para la Sra. Davis'),
(6, 'Servicio de velatorio para el Sr. Martinez'),
(7, 'Servicio de entierro para el Sr. Anderson'),
(8, 'Floristería para el Sr. Taylor'),
(9, 'Honorarios del director de funeraria para la Sra. Hernandez'),
(10, 'Gastos administrativos para el Sr. Garcia'),
(1, 'Funeral básico para la Sra. Lopez'),
(2, 'Servicio de cremación para el Sr. Perez'),
(3, 'Traslado del cuerpo para la Sra. Gonzalez'),
(4, 'Preparación del cuerpo para el Sr. Torres'),
(5, 'Embalaje del cuerpo para la Sra. Vasquez'),
(6, 'Servicio de velatorio para el Sr. Santos'),
(7, 'Servicio de entierro para el Sr. Moreno'),
(8, 'Floristería para la Sra. Rojas'),
(9, 'Honorarios del director de funeraria para el Sr. Estrada'),
(10, 'Gastos administrativos para la Sra. Alvarez'),
(1, 'Funeral básico para el Sr. Silva'),
(2, 'Servicio de cremación para la Sra. Chavez'),
(3, 'Traslado del cuerpo para el Sr. Gomez'),
(4, 'Preparación del cuerpo para el Sr. Diaz'),
(5, 'Embalaje del cuerpo para la Sra. Guerrero'),
(6, 'Servicio de velatorio para el Sr. Delgado'),
(7, 'Servicio de entierro para el Sr. Flores'),
(8, 'Floristería para el Sr. Marquez'),
(9, 'Honorarios del director de funeraria para el Sr. Rojas'),
(10, 'Gastos administrativos para la Sra. Estrada'),
(1, 'Funeral básico para la Sra. Santos'),
(2, 'Servicio de cremación para el Sr. Vasquez'),
(3, 'Traslado del cuerpo para la Sra. Ruiz'),
(4, 'Preparación del cuerpo para el Sr. Castillo'),
(5, 'Embalaje del cuerpo para la Sra. Vargas'),
(6, 'Servicio de velatorio para el Sr. Nunez'),
(7, 'Servicio de entierro para el Sr. Gutierrez'),
(8, 'Floristería para la Sra. Morales'),
(9, 'Honorarios del director de funeraria para la Sra. Santiago'),
(10, 'Gastos administrativos para el Sr. Guerrero'),
(1, 'Funeral básico para el Sr. Jimenez'),
(2, 'Servicio de cremación para la Sra. Moreno'),
(3, 'Traslado del cuerpo para el Sr. Rojas'),
(4, 'Preparación del cuerpo para la Sra. Estrada'),
(5, 'Embalaje del cuerpo para el Sr. Alvarez'),
(6, 'Servicio de velatorio para la Sra. Silva'),
(7, 'Servicio de entierro para el Sr. Chavez'),
(8, 'Floristería para el Sr. Gomez'),
(9, 'Honorarios del director de funeraria para la Sr. Diaz'),
(10, 'Gastos administrativos para la Sra. Guerrero');
"""
)

cursor.execute(
    """
-- Vinculo_Certificaciones
CREATE TABLE Vinculo_Certificaciones (
    Documento_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Certificado_De_Defuncion TEXT,
    Autorizacion_De_Cremacion TEXT,
    Permiso_De_Cremacion TEXT
);"""
)

cursor.execute(
    """
INSERT INTO Vinculo_Certificaciones (Certificado_De_Defuncion, Autorizacion_De_Cremacion, Permiso_De_Cremacion) VALUES
('Certificado_001', 'Autorizacion_001', 'Permiso_001'),
('Certificado_002', 'Autorizacion_002', 'Permiso_002'),
('Certificado_003', 'Autorizacion_003', 'Permiso_003'),
('Certificado_004', 'Autorizacion_004', 'Permiso_004'),
('Certificado_005', 'Autorizacion_005', 'Permiso_005'),
('Certificado_006', 'Autorizacion_006', 'Permiso_006'),
('Certificado_007', 'Autorizacion_007', 'Permiso_007'),
('Certificado_008', 'Autorizacion_008', 'Permiso_008'),
('Certificado_009', 'Autorizacion_009', 'Permiso_009'),
('Certificado_010', 'Autorizacion_010', 'Permiso_010'),
('Certificado_011', 'Autorizacion_011', 'Permiso_011'),
('Certificado_012', 'Autorizacion_012', 'Permiso_012'),
('Certificado_013', 'Autorizacion_013', 'Permiso_013'),
('Certificado_014', 'Autorizacion_014', 'Permiso_014'),
('Certificado_015', 'Autorizacion_015', 'Permiso_015'),
('Certificado_016', 'Autorizacion_016', 'Permiso_016'),
('Certificado_017', 'Autorizacion_017', 'Permiso_017'),
('Certificado_018', 'Autorizacion_018', 'Permiso_018'),
('Certificado_019', 'Autorizacion_019', 'Permiso_019'),
('Certificado_020', 'Autorizacion_020', 'Permiso_020'),
('Certificado_021', 'Autorizacion_021', 'Permiso_021'),
('Certificado_022', 'Autorizacion_022', 'Permiso_022'),
('Certificado_023', 'Autorizacion_023', 'Permiso_023'),
('Certificado_024', 'Autorizacion_024', 'Permiso_024'),
('Certificado_025', 'Autorizacion_025', 'Permiso_025'),
('Certificado_026', 'Autorizacion_026', 'Permiso_026'),
('Certificado_027', 'Autorizacion_027', 'Permiso_027'),
('Certificado_028', 'Autorizacion_028', 'Permiso_028'),
('Certificado_029', 'Autorizacion_029', 'Permiso_029'),
('Certificado_030', 'Autorizacion_030', 'Permiso_030'),
('Certificado_031', 'Autorizacion_031', 'Permiso_031'),
('Certificado_032', 'Autorizacion_032', 'Permiso_032'),
('Certificado_033', 'Autorizacion_033', 'Permiso_033'),
('Certificado_034', 'Autorizacion_034', 'Permiso_034'),
('Certificado_035', 'Autorizacion_035', 'Permiso_035'),
('Certificado_036', 'Autorizacion_036', 'Permiso_036'),
('Certificado_037', 'Autorizacion_037', 'Permiso_037'),
('Certificado_038', 'Autorizacion_038', 'Permiso_038'),
('Certificado_039', 'Autorizacion_039', 'Permiso_039'),
('Certificado_040', 'Autorizacion_040', 'Permiso_040'),
('Certificado_041', 'Autorizacion_041', 'Permiso_041'),
('Certificado_042', 'Autorizacion_042', 'Permiso_042'),
('Certificado_043', 'Autorizacion_043', 'Permiso_043'),
('Certificado_044', 'Autorizacion_044', 'Permiso_044'),
('Certificado_045', 'Autorizacion_045', 'Permiso_045'),
('Certificado_046', 'Autorizacion_046', 'Permiso_046'),
('Certificado_047', 'Autorizacion_047', 'Permiso_047'),
('Certificado_048', 'Autorizacion_048', 'Permiso_048'),
('Certificado_049', 'Autorizacion_049', 'Permiso_049'),
('Certificado_050', 'Autorizacion_050', 'Permiso_050');
"""
)

cursor.execute(
    """
-- Clientes
CREATE TABLE Clientes (
    Cliente_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    Apellido_Paterno TEXT NOT NULL,
    Apellido_Materno TEXT NOT NULL,
    Fecha_De_Nacimiento DATE NOT NULL,
    Lugar_De_Nacimiento TEXT NOT NULL,
    Genero TEXT,
    Celular TEXT NOT NULL,
    Celular_2 TEXT,
    Direccion TEXT NOT NULL,
    Licencia TEXT,
    Seguro_Social VARCHAR(11) NOT NULL,
    Numero_De_Servicio_Militar TEXT,
    Descripcion TEXT
);"""
)

cursor.execute(
    """
INSERT INTO Clientes (Nombre, Apellido_Paterno, Apellido_Materno, Fecha_De_Nacimiento, Lugar_De_Nacimiento, Genero, Celular, Celular_2, Direccion, Licencia, Seguro_Social, Numero_De_Servicio_Militar, Descripcion) VALUES
('John', 'Doe', 'Smith', '1990-01-15', 'New York', 'Masculino', '1234567890', '0987654321', '123 Main St', 'ABC123', '123456789', 'MIL001', 'Cliente regular'),
('Jane', 'Doe', 'Johnson', '1985-05-25', 'Los Angeles', 'Femenino', '9876543210', '0123456789', '456 Elm St', 'DEF456', '987654321', 'MIL002', 'Cliente VIP'),
('Michael', 'Smith', 'Brown', '1988-12-30', 'Chicago', 'Masculino', '5551112222', '3334445555', '789 Oak St', 'GHI789', '456789012', 'MIL003', 'Cliente ocasional'),
('Emily', 'Johnson', 'Davis', '1992-07-10', 'Houston', 'Femenino', '7778889999', '4445556666', '321 Pine St', 'JKL012', '789012345', 'MIL004', 'Cliente corporativo'),
('Christopher', 'Brown', 'Wilson', '1983-03-18', 'Miami', 'Masculino', '9990001111', '6667778888', '654 Maple St', 'MNO123', '901234567', 'MIL005', 'Cliente preferencial'),
('Jessica', 'Davis', 'Martinez', '1995-09-05', 'Atlanta', 'Femenino', '3334445555', '2223334444', '987 Cedar St', 'PQR234', '345678901', 'MIL006', 'Cliente regular'),
('Matthew', 'Wilson', 'Anderson', '1990-11-20', 'Dallas', 'Masculino', '1112223333', '8889990000', '753 Birch St', 'STU345', '456789012', 'MIL007', 'Cliente VIP'),
('Amanda', 'Martinez', 'Taylor', '1987-04-15', 'Seattle', 'Femenino', '4445556666', '0001112222', '852 Walnut St', 'VWX456', '567890123', 'MIL008', 'Cliente ocasional'),
('David', 'Anderson', 'Hernandez', '1982-08-28', 'San Francisco', 'Masculino', '6667778888', '1112223333', '369 Oak St', 'YZA567', '678901234', 'MIL009', 'Cliente corporativo'),
('Sarah', 'Taylor', 'Garcia', '1993-06-30', 'Phoenix', 'Femenino', '2223334444', '5556667777', '963 Elm St', 'BCD678', '789012345', 'MIL010', 'Cliente preferencial'),
('Daniel', 'Hernandez', 'Rodriguez', '1986-01-05', 'Denver', 'Masculino', '8889990000', '3334445555', '147 Pine St', 'EFG789', '890123456', 'MIL011', 'Cliente regular'),
('Lauren', 'Garcia', 'Lopez', '1991-04-22', 'Boston', 'Femenino', '0001112222', '6667778888', '258 Maple St', 'HIJ890', '901234567', 'MIL012', 'Cliente VIP'),
('Ryan', 'Rodriguez', 'Perez', '1984-10-13', 'Philadelphia', 'Masculino', '5556667777', '9990001111', '369 Cedar St', 'KLM901', '012345678', 'MIL013', 'Cliente ocasional'),
('Ashley', 'Lopez', 'Sanchez', '1996-12-05', 'Washington D.C.', 'Femenino', '3334445555', '2223334444', '852 Oak St', 'NOP012', '123456789', 'MIL014', 'Cliente corporativo'),
('Kevin', 'Perez', 'Torres', '1989-07-01', 'Houston', 'Masculino', '7778889999', '4445556666', '963 Pine St', 'QRS123', '234567890', 'MIL015', 'Cliente preferencial'),
('Rachel', 'Sanchez', 'Gonzalez', '1994-03-28', 'Dallas', 'Femenino', '1112223333', '8889990000', '147 Elm St', 'TUV234', '345678901', 'MIL016', 'Cliente regular'),
('Brandon', 'Torres', 'Rivera', '1981-12-10', 'Miami', 'Masculino', '9990001111', '6667778888', '258 Oak St', 'WXY345', '456789012', 'MIL017', 'Cliente VIP'),
('Megan', 'Gonzalez', 'Vargas', '1997-08-08', 'Los Angeles', 'Femenino', '4445556666', '0001112222', '369 Pine St', 'YZA456', '567890123', 'MIL018', 'Cliente ocasional'),
('Kyle', 'Rivera', 'Ortiz', '1992-01-15', 'San Francisco', 'Masculino', '2223334444', '5556667777', '852 Cedar St', 'BCD567', '678901234', 'MIL019', 'Cliente corporativo'),
('Stephanie', 'Vargas', 'Cruz', '1985-06-18', 'Seattle', 'Femenino', '8889990000', '3334445555', '963 Elm St', 'EFG678', '789012345', 'MIL020', 'Cliente preferencial'),
('Jacob', 'Ortiz', 'Reyes', '1990-09-20', 'Chicago', 'Masculino', '5556667777', '9990001111', '147 Pine St', 'HIJ789', '890123456', 'MIL021', 'Cliente regular'),
('Alexis', 'Cruz', 'Diaz', '1987-02-28', 'New York', 'Femenino', '1112223333', '8889990000', '258 Cedar St', 'KLM890', '901234567', 'MIL022', 'Cliente VIP'),
('Courtney', 'Reyes', 'Martinez', '1993-05-10', 'Los Angeles', 'Femenino', '7778889999', '4445556666', '369 Elm St', 'NOP901', '012345678', 'MIL023', 'Cliente ocasional'),
('Tyler', 'Diaz', 'Lopez', '1984-11-03', 'Houston', 'Masculino', '9990001111', '6667778888', '852 Oak St', 'QRS012', '123456789', 'MIL024', 'Cliente corporativo'),
('Kayla', 'Martinez', 'Gonzalez', '1989-10-27', 'San Francisco', 'Femenino', '3334445555', '2223334444', '963 Pine St', 'TUV123', '234567890', 'MIL025', 'Cliente preferencial'),
('Zachary', 'Lopez', 'Hernandez', '1995-07-15', 'Dallas', 'Masculino', '7778889999', '4445556666', '147 Elm St', 'WXY234', '345678901', 'MIL026', 'Cliente regular'),
('Samantha', 'Gonzalez', 'Garcia', '1982-04-18', 'Miami', 'Femenino', '2223334444', '5556667777', '258 Cedar St', 'YZA345', '456789012', 'MIL027', 'Cliente VIP'),
('Joseph', 'Hernandez', 'Torres', '1996-02-22', 'Los Angeles', 'Masculino', '8889990000', '3334445555', '369 Oak St', 'BCD456', '567890123', 'MIL028', 'Cliente ocasional'),
('Hannah', 'Garcia', 'Sanchez', '1983-09-14', 'New York', 'Femenino', '5556667777', '9990001111', '852 Elm St', 'EFG567', '678901234', 'MIL029', 'Cliente corporativo'),
('Andrew', 'Torres', 'Martinez', '1990-06-25', 'Chicago', 'Masculino', '1112223333', '8889990000', '963 Pine St', 'HIJ678', '789012345', 'MIL030', 'Cliente preferencial'),
('Taylor', 'Sanchez', 'Rivera', '1986-03-05', 'Houston', 'Femenino', '7778889999', '4445556666', '147 Cedar St', 'KLM789', '890123456', 'MIL031', 'Cliente regular'),
('Olivia', 'Martinez', 'Ortiz', '1991-12-18', 'San Francisco', 'Femenino', '9990001111', '6667778888', '258 Elm St', 'NOP890', '901234567', 'MIL032', 'Cliente VIP'),
('James', 'Rivera', 'Cruz', '1980-08-23', 'Seattle', 'Masculino', '3334445555', '2223334444', '369 Oak St', 'QRS901', '012345678', 'MIL033', 'Cliente ocasional'),
('Emma', 'Ortiz', 'Reyes', '1995-05-30', 'Dallas', 'Femenino', '7778889999', '4445556666', '852 Pine St', 'TUV012', '123456789', 'MIL034', 'Cliente corporativo'),
('Benjamin', 'Cruz', 'Diaz', '1988-02-12', 'Miami', 'Masculino', '1112223333', '8889990000', '963 Cedar St', 'WXY123', '234567890', 'MIL035', 'Cliente preferencial'),
('Madison', 'Reyes', 'Lopez', '1993-11-25', 'Los Angeles', 'Femenino', '9990001111', '6667778888', '147 Elm St', 'YZA234', '345678901', 'MIL036', 'Cliente regular'),
('Elijah', 'Diaz', 'Martinez', '1984-07-21', 'New York', 'Masculino', '3334445555', '2223334444', '258 Oak St', 'BCD345', '456789012', 'MIL037', 'Cliente VIP'),
('Chloe', 'Martinez', 'Gonzalez', '1997-04-14', 'Chicago', 'Femenino', '7778889999', '4445556666', '369 Pine St', 'EFG456', '567890123', 'MIL038', 'Cliente ocasional'),
('Carter', 'Gonzalez', 'Hernandez', '1981-01-03', 'Houston', 'Masculino', '1112223333', '8889990000', '852 Elm St', 'HIJ567', '678901234', 'MIL039', 'Cliente corporativo'),
('Avery', 'Hernandez', 'Torres', '1989-08-16', 'San Francisco', 'Femenino', '3334445555', '2223334444', '963 Cedar St', 'KLM678', '789012345', 'MIL040', 'Cliente preferencial'),
('Jackson', 'Torres', 'Sanchez', '1994-06-09', 'Seattle', 'Masculino', '8889990000', '3334445555', '147 Elm St', 'NOP789', '890123456', 'MIL041', 'Cliente regular'),
('Mia', 'Sanchez', 'Martinez', '1983-03-01', 'Dallas', 'Femenino', '5556667777', '9990001111', '258 Oak St', 'QRS890', '901234567', 'MIL042', 'Cliente VIP'),
('Ethan', 'Martinez', 'Rivera', '1988-10-14', 'Miami', 'Masculino', '1112223333', '8889990000', '369 Pine St', 'TUV901', '012345678', 'MIL043', 'Cliente ocasional'),
('Natalie', 'Rivera', 'Cruz', '1996-09-27', 'Los Angeles', 'Femenino', '7778889999', '4445556666', '852 Cedar St', 'WXY012', '123456789', 'MIL044', 'Cliente corporativo'),
('Noah', 'Cruz', 'Diaz', '1980-04-11', 'New York', 'Masculino', '3334445555', '2223334444', '963 Elm St', 'YZA123', '234567890', 'MIL045', 'Cliente preferencial'),
('Addison', 'Diaz', 'Reyes', '1991-01-24', 'Chicago', 'Femenino', '8889990000', '3334445555', '147 Pine St', 'BCD234', '345678901', 'MIL046', 'Cliente regular'),
('Liam', 'Reyes', 'Lopez', '1995-11-07', 'Houston', 'Masculino', '9990001111', '6667778888', '258 Oak St', 'EFG345', '456789012', 'MIL047', 'Cliente VIP'),
('Aubrey', 'Lopez', 'Martinez', '1986-07-17', 'San Francisco', 'Femenino', '1112223333', '8889990000', '369 Elm St', 'HIJ456', '567890123', 'MIL048', 'Cliente ocasional'),
('Logan', 'Martinez', 'Gonzalez', '1993-05-20', 'Seattle', 'Masculino', '7778889999', '4445556666', '852 Pine St', 'KLM567', '678901234', 'MIL049', 'Cliente corporativo'),
('Hailey', 'Gonzalez', 'Hernandez', '1982-02-28', 'Miami', 'Femenino', '3334445555', '2223334444', '963 Cedar St', 'NOP678', '789012345', 'MIL050', 'Cliente preferencial');
"""
)

cursor.execute(
    """
-- Difuntos
CREATE TABLE Difuntos (
    Difunto_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    Apellido_Paterno TEXT NOT NULL,
    Apellidp_Materno TEXT NOT NULL,
    Genero TEXT NOT NULL,
    Estado_Civil TEXT NOT NULL,
    Nombre_Padre TEXT NOT NULL,
    Nombre_Madre TEXT NOT NULL,
    Seguro_Social VARCHAR(11) NOT NULL,
    Numero_De_Servicio_Militar TEXT,
    Edad INTEGER NOT NULL,
    Fecha_De_Nacimiento DATE NOT NULL,
    Fecha_Defuncion DATE NOT NULL
);"""
)

cursor.execute(
    """
INSERT INTO Difuntos (Nombre, Apellido_Paterno, Apellidp_Materno, Genero, Estado_Civil, Nombre_Padre, Nombre_Madre, Seguro_Social, Numero_De_Servicio_Militar, Edad, Fecha_De_Nacimiento, Fecha_Defuncion) VALUES
('John', 'Doe', 'Smith', 'Masculino', 'Casado', 'James Doe', 'Emily Smith', '123456789', 'MIL001', 75, '1948-03-15', '2023-07-20'),
('Jane', 'Doe', 'Johnson', 'Femenino', 'Casado', 'Michael Johnson', 'Jennifer Brown', '987654321', 'MIL002', 70, '1953-05-25', '2022-11-10'),
('Michael', 'Smith', 'Brown', 'Masculino', 'Soltero', 'Robert Smith', 'Mary Davis', '456789012', 'MIL003', 60, '1963-12-30', '2023-09-05'),
('Emily', 'Johnson', 'Davis', 'Femenino', 'Viudo/a', 'John Johnson', 'Linda Martinez', '789012345', 'MIL004', 65, '1958-07-10', '2024-02-18'),
('Christopher', 'Brown', 'Wilson', 'Masculino', 'Casado', 'David Brown', 'Susan Wilson', '234567890', 'MIL005', 80, '1943-03-18', '2023-10-30'),
('Jessica', 'Davis', 'Martinez', 'Femenino', 'Soltero', 'Daniel Davis', 'Karen Garcia', '901234567', 'MIL006', 35, '1989-09-05', '2024-01-12'),
('Matthew', 'Wilson', 'Anderson', 'Masculino', 'Divorciado', 'Richard Wilson', 'Patricia Anderson', '345678901', 'MIL007', 45, '1978-11-20', '2023-05-15'),
('Amanda', 'Martinez', 'Taylor', 'Femenino', 'Viudo/a', 'Thomas Martinez', 'Maria Hernandez', '678901234', 'MIL008', 55, '1969-04-15', '2022-08-22'),
('David', 'Anderson', 'Hernandez', 'Masculino', 'Soltero', 'George Anderson', 'Nancy Taylor', '789012345', 'MIL009', 68, '1956-08-28', '2023-11-28'),
('Sarah', 'Taylor', 'Garcia', 'Femenino', 'Casado', 'Steven Taylor', 'Rebecca Smith', '890123456', 'MIL010', 72, '1951-06-30', '2023-03-03'),
('Daniel', 'Hernandez', 'Rodriguez', 'Masculino', 'Divorciado', 'Jose Hernandez', 'Laura Martinez', '901234567', 'MIL011', 40, '1984-01-05', '2024-04-01'),
('Lauren', 'Garcia', 'Lopez', 'Femenino', 'Viudo/a', 'Richard Garcia', 'Megan Rodriguez', '012345678', 'MIL012', 85, '1939-04-22', '2023-06-12'),
('Ryan', 'Rodriguez', 'Perez', 'Masculino', 'Soltero', 'Christopher Rodriguez', 'Amy Gonzalez', '123456789', 'MIL013', 55, '1968-10-13', '2024-03-28'),
('Ashley', 'Lopez', 'Sanchez', 'Femenino', 'Casado', 'Joseph Lopez', 'Julia Perez', '234567890', 'MIL014', 47, '1976-12-05', '2023-09-17'),
('Kevin', 'Perez', 'Torres', 'Masculino', 'Divorciado', 'John Perez', 'Maria Lopez', '345678901', 'MIL015', 63, '1960-07-01', '2024-02-09'),
('Rachel', 'Sanchez', 'Gonzalez', 'Femenino', 'Viudo/a', 'Andrew Sanchez', 'Cynthia Torres', '456789012', 'MIL016', 78, '1946-03-28', '2023-11-23'),
('Brandon', 'Torres', 'Rivera', 'Masculino', 'Soltero', 'David Torres', 'Michelle Gonzalez', '567890123', 'MIL017', 42, '1981-12-10', '2024-01-31'),
('Megan', 'Gonzalez', 'Vargas', 'Femenino', 'Casado', 'Nicholas Gonzalez', 'Angela Rivera', '678901234', 'MIL018', 53, '1970-08-08', '2023-08-05'),
('Kyle', 'Rivera', 'Ortiz', 'Masculino', 'Viudo/a', 'William Rivera', 'Amanda Vargas', '789012345', 'MIL019', 68, '1955-01-15', '2023-07-10'),
('Stephanie', 'Vargas', 'Cruz', 'Femenino', 'Divorciado', 'Jason Vargas', 'Rachel Ortiz', '890123456', 'MIL020', 39, '1984-06-18', '2024-03-19'),
('Jacob', 'Ortiz', 'Reyes', 'Masculino', 'Casado', 'Ryan Ortiz', 'Christina Cruz', '901234567', 'MIL021', 41, '1982-09-20', '2023-12-27'),
('Alexis', 'Cruz', 'Diaz', 'Femenino', 'Soltero', 'Eric Cruz', 'Stephanie Reyes', '012345678', 'MIL022', 28, '1995-02-28', '2024-02-03'),
('Courtney', 'Reyes', 'Martinez', 'Femenino', 'Viudo/a', 'Brandon Reyes', 'Melissa Diaz', '123456789', 'MIL023', 62, '1962-04-15', '2023-05-29'),
('Tyler', 'Diaz', 'Lopez', 'Masculino', 'Divorciado', 'Justin Diaz', 'Samantha Martinez', '234567890', 'MIL024', 57, '1967-11-03', '2023-09-01'),
('Kayla', 'Martinez', 'Gonzalez', 'Femenino', 'Soltero', 'Aaron Martinez', 'Alyssa Lopez', '345678901', 'MIL025', 32, '1991-10-27', '2024-01-04'),
('Zachary', 'Lopez', 'Hernandez', 'Masculino', 'Casado', 'Nathan Lopez', 'Chelsea Gonzalez', '456789012', 'MIL026', 44, '1979-07-15', '2023-08-14'),
('Samantha', 'Gonzalez', 'Garcia', 'Femenino', 'Viudo/a', 'Dylan Gonzalez', 'Emily Hernandez', '567890123', 'MIL027', 75, '1948-04-18', '2024-03-07'),
('Joseph', 'Hernandez', 'Torres', 'Masculino', 'Soltero', 'Cameron Hernandez', 'Nicole Garcia', '678901234', 'MIL028', 51, '1972-06-25', '2023-07-29'),
('Hannah', 'Garcia', 'Sanchez', 'Femenino', 'Casado', 'Thomas Garcia', 'Kaitlyn Torres', '789012345', 'MIL029', 60, '1963-09-14', '2023-11-02'),
('Andrew', 'Torres', 'Martinez', 'Masculino', 'Viudo/a', 'Ian Torres', 'Madeline Sanchez', '890123456', 'MIL030', 73, '1950-06-05', '2024-02-16'),
('Taylor', 'Sanchez', 'Rivera', 'Femenino', 'Soltero', 'Jordan Sanchez', 'Juliana Martinez', '901234567', 'MIL031', 49, '1974-03-05', '2023-09-21'),
('Olivia', 'Martinez', 'Ortiz', 'Femenino', 'Casado', 'Noah Martinez', 'Gabriella Rivera', '012345678', 'MIL032', 66, '1957-12-18', '2023-07-19'),
('James', 'Rivera', 'Cruz', 'Masculino', 'Divorciado', 'Ian Rivera', 'Sophia Ortiz', '123456789', 'MIL033', 57, '1966-08-23', '2024-04-30'),
('Emma', 'Ortiz', 'Reyes', 'Femenino', 'Viudo/a', 'Charles Ortiz', 'Alexa Cruz', '234567890', 'MIL034', 81, '1942-05-30', '2023-08-09'),
('Benjamin', 'Cruz', 'Diaz', 'Masculino', 'Casado', 'Ethan Cruz', 'Hailey Reyes', '345678901', 'MIL035', 74, '1949-02-12', '2023-11-05'),
('Madison', 'Reyes', 'Lopez', 'Femenino', 'Soltero', 'Samuel Reyes', 'Isabella Diaz', '456789012', 'MIL036', 48, '1975-11-25', '2024-01-22'),
('Elijah', 'Diaz', 'Martinez', 'Masculino', 'Divorciado', 'Mason Diaz', 'Amelia Lopez', '567890123', 'MIL037', 69, '1954-07-21', '2023-10-13'),
('Chloe', 'Martinez', 'Gonzalez', 'Femenino', 'Viudo/a', 'William Martinez', 'Grace Martinez', '678901234', 'MIL038', 64, '1959-04-14', '2023-05-07'),
('Carter', 'Gonzalez', 'Hernandez', 'Masculino', 'Soltero', 'Henry Gonzalez', 'Elizabeth Gonzalez', '789012345', 'MIL039', 50, '1973-01-03', '2024-03-18'),
('Avery', 'Hernandez', 'Torres', 'Femenino', 'Casado', 'Oliver Hernandez', 'Victoria Hernandez', '890123456', 'MIL040', 67, '1956-08-16', '2023-10-26'),
('Jackson', 'Torres', 'Sanchez', 'Masculino', 'Divorciado', 'Leo Torres', 'Natalie Torres', '901234567', 'MIL041', 58, '1965-06-09', '2024-04-04'),
('Mia', 'Sanchez', 'Martinez', 'Femenino', 'Soltero', 'Aiden Sanchez', 'Lydia Sanchez', '012345678', 'MIL042', 30, '1993-03-01', '2023-09-03'),
('Ethan', 'Martinez', 'Rivera', 'Masculino', 'Casado', 'Jack Martinez', 'Charlotte Martinez', '123456789', 'MIL043', 77, '1946-10-14', '2023-07-27'),
('Natalie', 'Rivera', 'Cruz', 'Femenino', 'Divorciado', 'Owen Rivera', 'Bella Rivera', '234567890', 'MIL044', 52, '1971-09-27', '2024-02-14'),
('Noah', 'Cruz', 'Diaz', 'Masculino', 'Casado', 'Matthew Cruz', 'Victoria Cruz', '345678901', 'MIL045', 71, '1952-04-11', '2023-12-01'),
('Addison', 'Diaz', 'Reyes', 'Femenino', 'Soltero', 'Connor Diaz', 'Stella Diaz', '456789012', 'MIL046', 37, '1987-01-24', '2024-01-07'),
('Liam', 'Reyes', 'Lopez', 'Masculino', 'Viudo/a', 'Gavin Reyes', 'Nora Reyes', '567890123', 'MIL047', 84, '1939-11-07', '2023-08-18'),
('Aubrey', 'Lopez', 'Martinez', 'Femenino', 'Casado', 'Sebastian Lopez', 'Leah Lopez', '678901234', 'MIL048', 58, '1965-07-17', '2023-05-25'),
('Logan', 'Martinez', 'Gonzalez', 'Masculino', 'Divorciado', 'Wyatt Martinez', 'Haley Martinez', '789012345', 'MIL049', 59, '1964-05-20', '2024-03-12'),
('Hailey', 'Gonzalez', 'Hernandez', 'Femenino', 'Soltero', 'Nathan Gonzalez', 'Reagan Gonzalez', '890123456', 'MIL050', 36, '1987-02-28', '2023-10-09');
"""
)

cursor.execute(
    """
-- Contratos
CREATE TABLE Contratos (
    Contrato_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Documentos_ID INTEGER NOT NULL,
    Cliente_ID INTEGER NOT NULL,
    Servicios_Elegido_ID INTEGER NOT NULL,
    Difunto_ID INTEGER NOT NULL,
    Empleado_ID INTEGER,
    Parentesco_Difunto TEXT NOT NULL,
    Fecha_De_Contrato DATE NOT NULL,
    Fecha_De_Servicio DATE NOT NULL,
    Metodo_De_Pago TEXT NOT NULL,
    Detalles_De_Servicio TEXT,
    Monto_Total DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (Documentos_ID) REFERENCES Vinculo_Certificaciones (Documento_ID),
    FOREIGN KEY (Cliente_ID) REFERENCES Clientes (Cliente_ID),
    FOREIGN KEY (Servicios_Elegido_ID) REFERENCES Servicios_Elegidos (Servicios_Elegidos_ID),
    FOREIGN KEY (Difunto_ID) REFERENCES Difuntos (Difunto_ID),
    FOREIGN KEY (Empleado_ID) REFERENCES Empleados (Empleado_ID)
);"""
)

cursor.execute(
    """

INSERT INTO Contratos (Documentos_ID, Cliente_ID, Servicios_Elegido_ID, Difunto_ID, Empleado_ID, Parentesco_Difunto, Fecha_De_Contrato, Fecha_De_Servicio, Metodo_De_Pago, Detalles_De_Servicio, Monto_Total) VALUES
(1, 1, 1, 1, 1, 'Esposo/a', '2023-01-05', '2023-01-10', 'Tarjeta de crédito', 'Servicio básico + Traslado del cuerpo', 2000.00),
(2, 2, 2, 2, 2, 'Hijo/a', '2023-01-10', '2023-01-15', 'Transferencia bancaria', 'Servicio de cremación + Servicio de velatorio', 1800.00),
(3, 3, 3, 3, 3, 'Padre', '2023-01-15', '2023-01-20', 'Efectivo', 'Traslado del cuerpo + Servicio de entierro', 1700.00),
(4, 4, 4, 4, 4, 'Hermano/a', '2023-01-20', '2023-01-25', 'Cheque', 'Preparación del cuerpo + Servicio de velatorio', 1900.00),
(5, 5, 5, 5, 5, 'Primo/a', '2023-01-25', '2023-01-30', 'Tarjeta de débito', 'Embalaje del cuerpo + Floristería', 1600.00),
(6, 6, 6, 6, 6, 'Abuelo/a', '2023-02-05', '2023-02-10', 'Transferencia bancaria', 'Servicio de cremación + Traslado del cuerpo', 1750.00),
(7, 7, 7, 7, 7, 'Esposo/a', '2023-02-10', '2023-02-15', 'Efectivo', 'Servicio básico + Servicio de velatorio', 1950.00),
(8, 8, 8, 8, 8, 'Hijo/a', '2023-02-15', '2023-02-20', 'Tarjeta de crédito', 'Preparación del cuerpo + Servicio de entierro', 1850.00),
(9, 9, 9, 9, 9, 'Padre', '2023-02-20', '2023-02-25', 'Cheque', 'Servicio de cremación + Embalaje del cuerpo', 1650.00),
(10, 10, 10, 10, 10, 'Hermano/a', '2023-03-05', '2023-03-10', 'Transferencia bancaria', 'Servicio básico + Floristería', 1550.00),
(11, 11, 11, 11, 11, 'Primo/a', '2023-03-10', '2023-03-15', 'Tarjeta de débito', 'Traslado del cuerpo + Servicio de entierro', 1750.00),
(12, 12, 12, 12, 12, 'Abuelo/a', '2023-03-15', '2023-03-20', 'Efectivo', 'Preparación del cuerpo + Servicio de velatorio', 1850.00),
(13, 13, 13, 13, 13, 'Esposo/a', '2023-03-20', '2023-03-25', 'Cheque', 'Embalaje del cuerpo + Servicio de cremación', 1800.00),
(14, 14, 14, 14, 14, 'Hijo/a', '2023-04-05', '2023-04-10', 'Transferencia bancaria', 'Servicio básico + Traslado del cuerpo', 1700.00),
(15, 15, 15, 15, 15, 'Padre', '2023-04-10', '2023-04-15', 'Tarjeta de crédito', 'Servicio de cremación + Servicio de velatorio', 1950.00),
(16, 16, 16, 16, 16, 'Hermano/a', '2023-04-15', '2023-04-20', 'Efectivo', 'Preparación del cuerpo + Servicio de entierro', 1850.00),
(17, 17, 17, 17, 17, 'Primo/a', '2023-04-20', '2023-04-25', 'Cheque', 'Embalaje del cuerpo + Floristería', 1650.00),
(18, 18, 18, 18, 18, 'Abuelo/a', '2023-05-05', '2023-05-10', 'Transferencia bancaria', 'Servicio de cremación + Traslado del cuerpo', 1800.00),
(19, 19, 19, 19, 19, 'Esposo/a', '2023-05-10', '2023-05-15', 'Tarjeta de crédito', 'Servicio básico + Servicio de velatorio', 1950.00),
(20, 20, 20, 20, 20, 'Hijo/a', '2023-05-15', '2023-05-20', 'Efectivo', 'Preparación del cuerpo + Servicio de entierro', 1850.00),
(21, 21, 21, 21, 21, 'Padre', '2023-05-20', '2023-05-25', 'Cheque', 'Servicio de cremación + Embalaje del cuerpo', 1700.00),
(22, 22, 22, 22, 22, 'Hermano/a', '2023-06-05', '2023-06-10', 'Transferencia bancaria', 'Servicio básico + Floristería', 1600.00),
(23, 23, 23, 23, 23, 'Primo/a', '2023-06-10', '2023-06-15', 'Tarjeta de débito', 'Traslado del cuerpo + Servicio de entierro', 1800.00),
(24, 24, 24, 24, 24, 'Abuelo/a', '2023-06-15', '2023-06-20', 'Efectivo', 'Preparación del cuerpo + Servicio de velatorio', 1850.00),
(25, 25, 25, 25, 25, 'Esposo/a', '2023-06-20', '2023-06-25', 'Cheque', 'Embalaje del cuerpo + Servicio de cremación', 1800.00),
(26, 26, 26, 26, 26, 'Hijo/a', '2023-07-05', '2023-07-10', 'Transferencia bancaria', 'Servicio básico + Traslado del cuerpo', 1700.00),
(27, 27, 27, 27, 27, 'Padre', '2023-07-10', '2023-07-15', 'Tarjeta de crédito', 'Servicio de cremación + Servicio de velatorio', 1950.00),
(28, 28, 28, 28, 28, 'Hermano/a', '2023-07-15', '2023-07-20', 'Efectivo', 'Preparación del cuerpo + Servicio de entierro', 1850.00),
(29, 29, 29, 29, 29, 'Primo/a', '2023-07-20', '2023-07-25', 'Cheque', 'Embalaje del cuerpo + Floristería', 1650.00),
(30, 30, 30, 30, 30, 'Abuelo/a', '2023-08-05', '2023-08-10', 'Transferencia bancaria', 'Servicio de cremación + Traslado del cuerpo', 1800.00),
(31, 31, 31, 31, 31, 'Esposo/a', '2023-08-10', '2023-08-15', 'Tarjeta de crédito', 'Servicio básico + Servicio de velatorio', 1950.00),
(32, 32, 32, 32, 32, 'Hijo/a', '2023-08-15', '2023-08-20', 'Efectivo', 'Preparación del cuerpo + Servicio de entierro', 1850.00),
(33, 33, 33, 33, 33, 'Padre', '2023-08-20', '2023-08-25', 'Cheque', 'Servicio de cremación + Embalaje del cuerpo', 1700.00),
(34, 34, 34, 34, 34, 'Hermano/a', '2023-09-05', '2023-09-10', 'Transferencia bancaria', 'Servicio básico + Floristería', 1600.00),
(35, 35, 35, 35, 35, 'Primo/a', '2023-09-10', '2023-09-15', 'Tarjeta de débito', 'Traslado del cuerpo + Servicio de entierro', 1800.00),
(36, 36, 36, 36, 36, 'Abuelo/a', '2023-09-15', '2023-09-20', 'Efectivo', 'Preparación del cuerpo + Servicio de velatorio', 1850.00),
(37, 37, 37, 37, 37, 'Esposo/a', '2023-09-20', '2023-09-25', 'Cheque', 'Embalaje del cuerpo + Servicio de cremación', 1800.00),
(38, 38, 38, 38, 38, 'Hijo/a', '2023-10-05', '2023-10-10', 'Transferencia bancaria', 'Servicio básico + Traslado del cuerpo', 1700.00),
(39, 39, 39, 39, 39, 'Padre', '2023-10-10', '2023-10-15', 'Tarjeta de crédito', 'Servicio de cremación + Servicio de velatorio', 1950.00),
(40, 40, 40, 40, 40, 'Hermano/a', '2023-10-15', '2023-10-20', 'Efectivo', 'Preparación del cuerpo + Servicio de entierro', 1850.00),
(41, 41, 41, 41, 41, 'Primo/a', '2023-10-20', '2023-10-25', 'Cheque', 'Embalaje del cuerpo + Floristería', 1650.00),
(42, 42, 42, 42, 42, 'Abuelo/a', '2023-11-05', '2023-11-10', 'Transferencia bancaria', 'Servicio de cremación + Traslado del cuerpo', 1800.00),
(43, 43, 43, 43, 43, 'Esposo/a', '2023-11-10', '2023-11-15', 'Tarjeta de crédito', 'Servicio básico + Servicio de velatorio', 1950.00),
(44, 44, 44, 44, 44, 'Hijo/a', '2023-11-15', '2023-11-20', 'Efectivo', 'Preparación del cuerpo + Servicio de entierro', 1850.00),
(45, 45, 45, 45, 45, 'Padre', '2023-11-20', '2023-11-25', 'Cheque', 'Servicio de cremación + Embalaje del cuerpo', 1700.00),
(46, 46, 46, 46, 46, 'Hermano/a', '2023-12-05', '2023-12-10', 'Transferencia bancaria', 'Servicio básico + Floristería', 1600.00),
(47, 47, 47, 47, 47, 'Primo/a', '2023-12-10', '2023-12-15', 'Tarjeta de débito', 'Traslado del cuerpo + Servicio de entierro', 1800.00),
(48, 48, 48, 48, 48, 'Abuelo/a', '2023-12-15', '2023-12-20', 'Efectivo', 'Preparación del cuerpo + Servicio de velatorio', 1850.00),
(49, 49, 49, 49, 49, 'Esposo/a', '2023-12-20', '2023-12-25', 'Cheque', 'Embalaje del cuerpo + Servicio de cremación', 1800.00),
(50, 50, 50, 50, 50, 'Hijo/a', '2023-12-25', '2023-12-30', 'Transferencia bancaria', 'Servicio básico + Traslado del cuerpo', 1700.00);
"""
)
# Continue creating other tables similarly

# Commit the changes
conn.commit()

# Close the connection
conn.close()
