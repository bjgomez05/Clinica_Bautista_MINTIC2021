from flask import Flask
from flask import make_response
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
    return render("inicio/inicio.html")

# Login
@app.route("/login_paciente", methods=["GET", "POST"])
def login_paciente():
    global sesion_paciente_iniciada
    sesion_paciente_iniciada = True
    return render(
        "login/login_paciente/login_paciente.html" #,
        # sesion_paciente_iniciada=sesion_paciente_iniciada
        )

@app.route("/login_medico", methods=["GET", "POST"])
def login_medico():
    global sesion_medico_iniciada
    sesion_medico_iniciada = True
    return render(
        "login/login_medico/login_medico.html"#,
        # sesion_medico_iniciada=sesion_medico_iniciada
        )

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
@app.route("/perfil_paciente", methods=["GET", "POST"])
def perfil_paciente():
    return render("perfiles/perfil_paciente/perfil_paciente.html")

""" @app.route("/perfil_medico", methods=["GET", "POST"])
def perfil_medico():
    return render("perfiles/perfil_medico/perfil_paciente.html")

@app.route("/perfil_super", methods=["GET", "POST"])
def perfil_super():
    return render("perfiles/perfil_suoeradmin/perfil_paciente.html") """



# Listado de citas medicas
@app.route("/listado_citas", methods=["GET", "POST"])
def citas():
    return render("listado_citas/listado_citas.html")


# Detalle de la cita
@app.route("/detalle_cita", methods=["GET", "POST"])
def detalle_cita():
    return render("detalle_cita/detalle_cita.html")


# Pagina de paciente
@app.route("/pagina_paciente", methods=["GET", "POST"])
def pagina_paciente():
    return render("pagina_paciente/pagina_paciente.html")


@app.route("/salir", methods=["POST"])
def cerrar_sesion():
    global sesion_iniciada
    sesion_iniciada = False
    return redirect('/')





if __name__=='__main__':
    app.run(debug=True)