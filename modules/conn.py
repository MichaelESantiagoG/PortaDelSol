import sqlite3 as sql
import pandas as pd


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

    def Empleados(_=0):
        if _ == 1:
            return Connection.query1(
                """SELECT Empleado_ID || ': ' || Nombre || ' ' || Apellido_Paterno FROM Empleados;"""
            )
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

    def Servicios(_=0):
        if _ == 1:
            return Connection.query1(
                "SELECT Servicio_ID || ': ' || Servicio_Nombre FROM Servicios"
            )
        return Connection.query1(
            """
            SELECT Servicio_ID, Servicio_Nombre, Servicio_Precio FROM Servicios"""
        )

    def Servicios_Elegidos(_=0):
        return Connection.query1(
            """SELECT Servicios_Elegidos_ID, Contrato_ID, Servicio_ID
                FROM Servicios_Elegidos;"""
        )

    def CLientes(_=0):
        if _ == 1:
            return Connection.query1(
                """SELECT Cliente_ID || ': ' || Nombre || ' ' || Apellido_Paterno FROM Clientes;"""
            )

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

    def Difuntos(_=0):
        if _ == 1:
            return Connection.query1(
                "SELECT Difunto_ID || ': ' || Nombre || ' ' || Apellido_Paterno FROM Difuntos;"
            )
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
                FROM Difuntos;"""
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

    def Contratos(_=0):
        if _ == 2:
            return Connection.query3(
                "SELECT COUNT(*) AS Total_Contratos FROM Contratos;"
            )
        if _ == 1:
            return Connection.query1(
                """
                    SELECT
                        c.Contrato_ID,
                        cl.Cliente_ID || ': ' || cl.Nombre || ' ' || cl.Apellido_Paterno AS Cliente,
                        d.Difunto_ID || ': ' || d.Nombre  || ' ' || d.Apellido_Paterno AS Difunto,
                        e.Empleado_ID || ': ' || e.Nombre  || ' ' || e.Apellido_Paterno AS Empleado,
                        GROUP_CONCAT(se.Servicio_ID || ': ' || s.Servicio_Nombre) AS Servicios_Elegidos,
                        c.Parentesco_Difunto,
                        c.Fecha_Contrato,
                        c.Fecha_Servicio,
                        c.Metodo_Pago,
                        c.Servicio_Detalles,
                        c.Monto_Total
                    FROM Contratos c
                    JOIN Clientes cl ON c.Cliente_ID = cl.Cliente_ID
                    JOIN Difuntos d ON c.Difunto_ID = d.Difunto_ID
                    JOIN Empleados e ON c.Empleado_ID = e.Empleado_ID
                    JOIN Servicios_Elegidos se ON c.Contrato_ID = se.Contrato_ID
                    JOIN Servicios s ON se.Servicio_ID = s.Servicio_ID
                    GROUP BY c.Contrato_ID;
                    """
            )
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

    def Empleado(id):
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

    def Servicio(id):
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

    def CLiente(id):
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

    def Difunto(id):
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
                WHERE Difunto_ID = {id};"""
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

    def Contrato(id):
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
                UPDATE Servicios 
                SET Servicio_Nombre = '{data['Servicio_Nombre']}', Servicio_Precio = {data['Servicio_Precio']} 
                WHERE Servicio_ID = {id};
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
