from flask import Flask
from flask import render_template as render
from flask import redirect
from flask import request

app = Flask(__name__)

# VARIABLES
sesion_iniciada = False
sesion_paciente_iniciada = False
sesion_medico_iniciada = False
sesion_super_iniciada = False
regis_paciente = False
regis_medico = False

# RUTAS


# Home
@app.route("/", methods=["GET", "POST"])
def inicio():
    return render("inicio1.html")

# Login
@app.route("/login_paciente", methods=["GET", "POST"])
def login_paciente():
    global sesion_paciente_iniciada
    sesion_paciente_iniciada = True
    return render(
        "login.html",
        sesion_paciente_iniciada=sesion_paciente_iniciada
        )

@app.route("/login_medico", methods=["GET", "POST"])
def login_medico():
    global sesion_medico_iniciada
    sesion_medico_iniciada = True
    return render(
        "login.html",
        sesion_medico_iniciada=sesion_medico_iniciada
        )

@app.route("/login_super", methods=["GET", "POST"])
def login_super():
    global sesion_super_iniciada
    sesion_super_iniciada = True
    return render(
        "login.html",
        sesion_super_iniciada=sesion_super_iniciada
        )


# Registro
@app.route("/registro_paciente", methods=["GET", "POST"])
def registro_paciente():
    global regis_paciente
    regis_paciente = True
    return render(
        "registro.html",
        regis_paciente=regis_paciente
        )

@app.route("/registro_medico", methods=["GET", "POST"])
def registro_medico():
    global regis_medico
    regis_medico = True
    return render(
        "registro.html",
        regis_medico=regis_medico
        )

# @app.route("/registro_super", methods=["GET", "POST"])
# def registro_super():
#     return "Pagina de registro de datos para los superadministradores"



# Pagina de perfil
@app.route("/perfil_paciente", methods=["GET", "POST"])
def perfil_paciente():
    return "Muestra el perfil de los pacientes"

@app.route("/perfil_medico", methods=["GET", "POST"])
def perfil_medico():
    return "Muestra el perfil de los médicos"

@app.route("/perfil_super", methods=["GET", "POST"])
def perfil_super():
    return "Muestra el perfil del superadministrador"


# Listado de citas medicas
@app.route("/citas", methods=["GET", "POST"])
def citas():
    return "Muestra la lista de citas"

@app.route("/salir", methods=["POST"])
def cerrar_sesion():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)