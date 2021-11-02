from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FormaProducto(FlaskForm):
    nombres= StringField("Nombres", validators=[DataRequired()])

    apellidos= StringField("Apellidos", validators=[DataRequired()])

    email= StringField("Email", validators=[DataRequired()])

    contrasena= StringField("Contrasena", validators=[DataRequired()])

    selectbox= StringField("Selectbox", validators=[DataRequired()])

    tipo_identificacion= StringField("Tipo_identificacion", validators=[DataRequired()])
    
    numero_identificacion= StringField("Numero_identificacion", validators=[DataRequired()])

    telefono= StringField("Telefono", validators=[DataRequired()])

    telefono_fijo= StringField("Telefono_fijo")

    aceptartyc= StringField("Aceptartyc", validators=[DataRequired()])

    ingresar= SubmitField('Ingresar')

class FormaMedico(FlaskForm):
    nombres= StringField("Nombres", validators=[DataRequired()])

    apellidos= StringField("Apellidos", validators=[DataRequired()])

    email= StringField("Email", validators=[DataRequired()])

    contrasena= StringField("Contrasena", validators=[DataRequired()])

    telefono= StringField("Telefono", validators=[DataRequired()])

    telefono_fijo= StringField("Telefono_fijo", validators=[DataRequired()])
    
    tipo_identificacion= StringField("Tipo_identificacion", validators=[DataRequired()])

    numero_identificacion= StringField("Numero_identificacion", validators=[DataRequired()])

    profesion= StringField("Profesion", validators=[DataRequired()])

    posgrado= StringField("Posgrado")
    
    matricula_profesional= StringField("Matricula_profesional", validators=[DataRequired()])
    
    aceptartyc= StringField("Aceptartyc", validators=[DataRequired()])

    enviar= SubmitField('Enviar')

class FormaLoginMedico(FlaskForm):
    email= StringField("Email", validators=[DataRequired()])
    contrasena= StringField("Contrasena", validators=[DataRequired()])

class FormaLoginPaciente(FlaskForm):
    email= StringField("Email", validators=[DataRequired()])
    contrasena= StringField("Contrasena", validators=[DataRequired()])

class FormaLoginSuperadmin(FlaskForm):
    email= StringField("Email", validators=[DataRequired()])
    contrasena= StringField("Contrasena", validators=[DataRequired()])

class FormaListaCitas(FlaskForm):
    select= StringField("nombre_medico", validators=[DataRequired()])
    selectdos= StringField("horario", validators=[DataRequired()])
    selecttres= StringField("horario", validators=[DataRequired()])


