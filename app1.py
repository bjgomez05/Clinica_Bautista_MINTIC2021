import abc
from flask import Flask
from flask import make_response
from flask import render_template as render
from flask import redirect
from flask import request
from formas import FormaListaCitas, FormaLoginMedico, FormaLoginPaciente, FormaLoginSuperadmin, FormaMedico, FormaProducto
import db
import os
import bcrypt

app = Flask(__name__)
app.secret_key= os.urandom(32)
# VARIABLES
sesion_iniciada = False
sesion_paciente_iniciada = False
sesion_medico_iniciada = False
sesion_super_iniciada = False
regis_paciente = False
regis_medico = False

# RUTAS

#semilla
semilla = bcrypt.gensalt()


# Home
@app.route("/", methods=["GET", "POST"])
def inicio():
    return render("inicio/inicio.html")

# Login
@app.route("/enviarabd", methods=["GET", "POST"])
def enviaradb():
    forma = FormaProducto()
    if request.method =="POST":
        Nombres = forma.nombres.data
        Apellidos = forma.apellidos.data
        Email = forma.email.data
        Contrasena = forma.contrasena.data
        Tipo_identificacion = forma.tipo_identificacion.data
        Numero_identificacion = forma.numero_identificacion.data
        Telefono = forma.telefono.data
        Telefono_fijo = forma.telefono_fijo.data
        password_encode = Contrasena.encode("utf-8")
        password_encriptado = bcrypt.hashpw(password_encode, semilla)
        if bcrypt.checkpw(password_encode, password_encriptado):
            boolOK = db.insertProducto(Nombres, Apellidos, Email, Contrasena, Tipo_identificacion, Numero_identificacion, Telefono, Telefono_fijo)
            if boolOK:
                return redirect("/login_paciente")
            else:
                return redirect("/registro_paciente")
    else:
        return redirect ("/registro_paciente")

@app.route("/enviarabdm", methods=["GET", "POST"])
def enviaradbm():
    forma = FormaMedico()
    if request.method =="POST":
        Nombres = forma.nombres.data
        Apellidos = forma.apellidos.data
        Email = forma.email.data
        Contrasena = forma.contrasena.data
        Telefono = forma.telefono.data
        Telefono_fijo = forma.telefono_fijo.data
        Tipo_identificacion = forma.tipo_identificacion.data
        Numero_identificacion = forma.numero_identificacion.data
        Profesion = forma.profesion.data
        Posgrado = forma.posgrado.data
        Matricula_profesional = forma.matricula_profesional.data
        password_encode = Contrasena.encode("utf-8")
        password_encriptado = bcrypt.hashpw(password_encode, semilla)
        if bcrypt.checkpw(password_encode, password_encriptado):
            boolOK = db.insertMedico(Nombres, Apellidos, Email, Contrasena, Telefono, Telefono_fijo, Tipo_identificacion, Numero_identificacion, Profesion, Posgrado, Matricula_profesional)
            if boolOK:
                return redirect("/login_medico")
            else:
                return redirect("/registro_medico")
    else:
        return redirect("/registro_medico")


@app.route("/enviarabdlista", methods=["GET", "POST"])
def enviaradblista():
    forma = FormaListaCitas()
    if request.method =="POST":
        Nombre_medico = forma.select.data
        Horario = forma.selectdos.data
        tipo_cita = forma.selecttres.data
        if tipo_cita == "Cardiologia":
            boolOK = db.insertcita(Nombre_medico, Horario, tipo_cita)
            if boolOK:
                return redirect("/listado_citas")
        if tipo_cita == "Cuidado del bebe":
            boolOK = db.insertcita(Nombre_medico, Horario, tipo_cita)
            if boolOK:
                return redirect("/listado_citas")
        if tipo_cita == "Medico general":
            boolOK = db.insertcita(Nombre_medico, Horario, tipo_cita)
            if boolOK:
                return redirect("/listado_citas")
        if tipo_cita == "Neurologia":
            boolOK = db.insertcita(Nombre_medico, Horario, tipo_cita)
            if boolOK:
                return redirect("/listado_citas")
        if tipo_cita == "Pediatria":
            boolOK = db.insertcita(Nombre_medico, Horario, tipo_cita)
            if boolOK:
                return redirect("/listado_citas")
        if tipo_cita == "Psicologia":
            boolOK = db.insertcita(Nombre_medico, Horario, tipo_cita)
            if boolOK:
                return redirect("/listado_citas")
        



@app.route("/login_paciente", methods=["GET", "POST"])
def login_paciente():
    return render("login/login_paciente/login_paciente.html")

    
    

@app.route("/login_medico", methods=["GET", "POST"])
def login_medico():
    global sesion_medico_iniciada
    sesion_medico_iniciada = True
    return render(
        "login/login_medico/login_medico.html"#,
        # sesion_medico_iniciada=sesion_medico_iniciada
        )

@app.route("/consultbdm", methods=["GET", "POST"])
def consultbdm():
    forma = FormaLoginMedico()
    if request.method =="POST":
        Email = forma.email.data
        Contrasena = forma.contrasena.data
        tabla = db.loginMedico(Email)
        #print(tabla[0][0])
        #print(tabla[0][1])
        #print(Email)
        #print(Contrasena)
        try:
            if tabla != None:
                if tabla[0][0] == Email and tabla[0][1] == Contrasena:
                    return redirect("/pagina_medico")
                else:
                    return redirect("/login_medico")
            else:
                return redirect("/login_medico")
        except IndexError as error:
            print(error)
            return redirect("/login_medico")

@app.route("/consultbdp", methods=["GET", "POST"])
def consultbdp():
    forma = FormaLoginPaciente()
    if request.method =="POST":
        Email = forma.email.data
        Contrasena = forma.contrasena.data
        tablap = db.loginPaciente(Email)
        print(tablap)
        #print(tablap[0][0])
        #print(tablap[0][1])
        #print(Email)
        #print(Contrasena)
        try:
            if tablap != None:
                if tablap[0][0] == Email and tablap[0][1] == Contrasena:
                    return redirect("/pagina_paciente")
                else:
                    return redirect("/login_paciente")
            else:
                return redirect("/login_paciente")
        except IndexError as error:
            print(error)
            return redirect("/login_paciente")

@app.route("/consultbds", methods=["GET", "POST"])
def consultbds():
    forma = FormaLoginSuperadmin()
    if request.method =="POST":
        Email = forma.email.data
        Contrasena = forma.contrasena.data
        tablasuper = db.loginSuperadmin(Email)
        #print(tablap)
        #print(tablap[0][0])
        #print(tablap[0][1])
        #print(Email)
        #print(Contrasena)
        try:
            if tablasuper != None:
                if tablasuper[0][0] == Email and tablasuper[0][1] == Contrasena:
                    return redirect("/perfil_paciente")
                else:
                    return redirect("/login_superadmin")
            else:
                return redirect("/login_superadmin")
        except IndexError as error:
            print(error)
            return redirect("/login_superadmin")

    
    


@app.route("/login_superadmin", methods=["GET", "POST"])
def login_super():
    global sesion_super_iniciada
    sesion_super_iniciada = True
    return render(
        "login/login_superadmin/login_superadmin.html"#,
        # sesion_super_iniciada=sesion_super_iniciada
        )


# Registro
@app.route("/registro_paciente", methods=["GET", "POST"])
def registro_paciente():
    global regis_paciente
    regis_paciente = True
    return render(
        "registro/registro_paciente/registro_paciente.html"#,
        # regis_paciente=regis_paciente
        )

@app.route("/registro_medico", methods=["GET", "POST"])
def registro_medico():
    global regis_medico
    regis_medico = True
    return render(
        "registro/registro_medico/registro_medico.html"#,
        # regis_medico=regis_medico
        )

# @app.route("/registro_super", methods=["GET", "POST"])
# def registro_super():
#     return "Pagina de registro de datos para los superadministradores"



# Pagina de perfil
@app.route("/pagina_paciente", methods=["GET", "POST"])
def perfil_paciente():
    return render("pagina_paciente/pagina_paciente.html")



# Listado de citas medicas
@app.route("/listado_citas", methods=["GET", "POST"])
def citas():
    return render("listado_citas/listado_citas.html")


# Detalle de la cita
@app.route("/detalle_cita", methods=["GET", "POST"])
def detalle_cita():
    return render("detalle_cita/detalle_cita.html")


# Pagina de paciente
@app.route("/pagina_medico", methods=["GET", "POST"])
def pagina_paciente():
    return render("pagina_medico/pagina_medico.html")


@app.route("/salir", methods=["POST"])
def cerrar_sesion():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/')





if __name__=='__main__':
    app.run(debug=True)