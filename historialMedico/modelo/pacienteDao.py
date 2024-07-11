from cmath import e
from .conexion import ConexionDB
from tkinter import messagebox

def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET nombre = '{persona.nombre}', apellidoPaterno = '{persona.apellidoPaterno}', apellidoMaterno = '{persona.apellidoMaterno}', curp = '{persona.curp}', fechaNacimiento = '{persona.fechaNacimiento}', seguroSocial = '{persona.seguroSocial}', antecedentes = '{persona.antecedentes}', correo = '{persona.correo}', telefono = '{persona.telefono}', Edad = '{persona.Edad}', activo = 1 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Paciente'
        mensaje = 'Paciente Editado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Paciente'
        mensaje = 'Error al editar paciente'
        messagebox.showerror(title, mensaje)
        
def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno, curp, fechaNacimiento, seguroSocial, antecedentes, correo, telefono, Edad, activo) VALUES ('{persona.nombre}','{persona.apellidoPaterno}','{persona.apellidoMaterno}','{persona.curp}','{persona.fechaNacimiento}','{persona.seguroSocial}','{persona.antecedentes}','{persona.correo}','{persona.telefono}', '{persona.Edad}',1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Paciente'
        mensaje = f'Error al registrar paciente: {str (e)}'
        messagebox.showerror(title, mensaje)

        
def listar():
    conexion = ConexionDB()

    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros No Existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona

def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()

    except:
        title = 'Datos'
        mensaje = 'Registros No Existen'      
        messagebox.showwarning(title, mensaje)
    return listaPersona
    
def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Paciente'
        mensaje = 'Paciente Eliminado Exitosamente'
        messagebox.showwarning(title, mensaje)
    except:
        title = 'Eliminar Paciente'
        mensaje = 'Error al eliminar'
        messagebox.showwarning(title, mensaje)

class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, curp, fechaNacimiento, seguroSocial, antecedentes, correo, telefono, Edad):
        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.curp = curp
        self.fechaNacimiento = fechaNacimiento
        self.seguroSocial = seguroSocial
        self.antecedentes = antecedentes
        self.correo = correo
        self.telefono = telefono
        self.Edad = Edad

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellidoPaterno},{self.apellidoMaterno},{self.curp},{self.fechaNacimiento},{self.seguroSocial},{self.antecedentes},{self.correo},{self.telefono}, {self.Edad}]'    