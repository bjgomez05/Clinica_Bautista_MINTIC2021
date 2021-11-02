import sqlite3 
from sqlite3 import Error

def conectar():
    dbname= 'mydatabase1.db'
    conn = sqlite3.connect(dbname)
    return conn

#def insertProducto(code, nom, qty):
#    conn = conectar()
#    conn.execute("insert into productos (codigo, nombre, cantidad) values (?,?,?)", (code, nom, qty))
#    conn.commit()
#    conn.close()

#Para capturar posibles errores:
def insertProducto(Nombres, Apellidos, Email, Contrasena, Tipo_identificacion, Numero_identificacion, Telefono, Telefono_fijo):
    try:
        conn = conectar()
        conn.execute("insert into registro_pacientes (nombres, apellidos, email, contrasena, tipo_identificacion, numero_identificacion, telefono, telefono_fijo) values (?,?,?,?,?,?,?,?)", (Nombres, Apellidos, Email, Contrasena, Tipo_identificacion, Numero_identificacion, Telefono, Telefono_fijo))
        conn.commit()
        conn.close()
        return True
    except Error as error: 
        print(error)
        return False

def insertMedico(Nombres, Apellidos, Email, Contrasena, Telefono, Telefono_fijo, Tipo_identificacion, Numero_identificacion, Profesion, Posgrado, Matricula_profesional):
    try:
        conn = conectar()
        conn.execute("insert into registro_medicos (nombres, apellidos, email, contrasena, telefono, telefono_fijo, tipo_identificacion, numero_identificacion, profesion, posgrado, matricula_profesional) values (?,?,?,?,?,?,?,?,?,?,?)", (Nombres, Apellidos, Email, Contrasena, Telefono, Telefono_fijo, Tipo_identificacion, Numero_identificacion, Profesion, Posgrado, Matricula_profesional))
        conn.commit()
        conn.close()
        return True
    except Error as error: 
        print(error)
        return False

def insertcita(Nombre_medico, Horario, Tipo_cita):
    try:
        conn = conectar()
        conn.execute("insert into lista_citas (nombre_medico, horario, tipo_cita) values (?,?,?)", (Nombre_medico, Horario, Tipo_cita))
        conn.commit()
        conn.close()
        return True
    except Error as error: 
        print(error)
        return False

def loginMedico(Email):
    conn = conectar()
    cursor = conn.execute(f"select email, contrasena from registro_medicos where email='{Email}'")
    resultados = cursor.fetchall()
    return resultados

def loginPaciente(Email):
    conn = conectar()
    cursor = conn.execute(f"select email, contrasena from registro_pacientes where email='{Email}'")
    resultados = cursor.fetchall()
    return resultados

def loginSuperadmin(Email):
    conn = conectar()
    cursor = conn.execute(f"select email, contrasena from superadministrador where email='{Email}'")
    resultados = cursor.fetchall()
    return resultados


if __name__ == '__main__':
    insertProducto()
    insertMedico()
    loginMedico()
    loginPaciente()
    loginSuperadmin()