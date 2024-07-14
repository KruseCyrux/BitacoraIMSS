import sqlite3
import os

class ConexionDB:
    def __init__(self):
        self.baseDatos = 'C:/Users/cracb/OneDrive/Escritorio/MediTrack/historialMedico/database/dbbitacora.db'
        self.conexion = sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()

    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()    