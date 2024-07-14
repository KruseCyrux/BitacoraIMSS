from sqlite3.dbapi2 import Cursor
from .conexion import ConexionDB
from tkinter import messagebox

def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f'SELECT h.idHistorialMedico, p.apellidoPaterno || " " || p.apellidoMaterno AS Apellidos, h.fechaHistorial, h.motivo, h.examenAuxiliar, h.tratamiento, h.detalle FROM historialMedico h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'
    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'LISTAR HISTORIA'
        mensaje = 'Error al listar historial medico'
        messagebox.showerror(title, mensaje)
    return listaHistoria

def guardarHistoria(idPersona, fechaHistorial, motivo, examenAuxiliar, tratamiento, detalle):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historialMedico (idPersona, fechaHistorial, motivo, examenAuxiliar, tratamiento, detalle) VALUES ({idPersona},'{fechaHistorial}','{motivo}','{examenAuxiliar}','{tratamiento}','{detalle}')"""

    try:
        conexion.cursor.execute(sql) 
        conexion.cerrarConexion()
        title = 'Registro Historial Medico'
        mensaje = 'Historial Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registro Historial Medico'
        mensaje = 'Error al registrar historial'
        messagebox.showerror(title, mensaje)

def eliminarHistoria(idHistorialMedico):
    conexion = ConexionDB()
    sql = f'DELETE FROM historialMedico WHERE idHistorialMedico = {idHistorialMedico}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Historia'
        mensaje = 'Historia medica eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Historia'
        mensaje = 'Error al eliminar historia medica'
        messagebox.showerror(title, mensaje)

def editarHistoria(fechaHistorial, motivo, examenAuxiliar, tratamiento, detalle, idHistorialMedico):
    conexion = ConexionDB()
    sql = f"""UPDATE historialMedico SET fechaHistorial = '{fechaHistorial}', motivo = '{motivo}', examenAuxiliar = '{examenAuxiliar}', tratamiento = '{tratamiento}', detalle = '{detalle}' WHERE idHistorialMedico = {idHistorialMedico}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Historia'
        mensaje = 'Historia medica editada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Historia'
        mensaje = 'Error al editar historia medica'
        messagebox.showerror(title, mensaje)

class historialMedico:
    def __init__(self, idPersona, fechaHistorial, motivo, examenAuxiliar, tratamiento, detalle):
        self.idHistorialMedico = None
        self.idPersona = idPersona
        self.fechaHistorial = fechaHistorial
        self.motivo = motivo
        self.examenAuxiliar = examenAuxiliar
        self.tratamiento = tratamiento
        self.detalle = detalle

    def __str__ (self):
        return f'historialMedico[{self.idPersona}, {self.fechaHistorial}, {self.motivo}, {self.examenAuxiliar}, {self.tratamiento}, {self.detalle}]'    