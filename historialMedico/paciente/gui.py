import tkinter as tk 
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date

class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=720, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.idPersona = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()
    def camposPaciente(self):

        #LABELS
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblApePaterno = tk.Label(self, text='Apellido Paterno: ')
        self.lblApePaterno.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblApePaterno.grid(column=0, row=1, padx=10, pady=5)

        self.lblApeMaterno = tk.Label(self, text='Apellido Materno: ')
        self.lblApeMaterno.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblApeMaterno.grid(column=0, row=2, padx=10, pady=5)

        self.lblCurp = tk.Label(self, text='CURP: ')
        self.lblCurp.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblCurp.grid(column=0, row=3, padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text='Fecha de Nacimiento: ')
        self.lblFechNacimiento.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblFechNacimiento.grid(column=0, row=4, padx=10, pady=5)

        self.lblSegSocial = tk.Label(self, text='No. Seguro Social: ')
        self.lblSegSocial.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblSegSocial.grid(column=0, row=5, padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblAntecedentes.grid(column=0, row=6, padx=10, pady=5)

        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblCorreo.grid(column=0, row=7, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Telefono: ')
        self.lblTelefono.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0, row=8, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0, row=9, padx=10, pady=5)

        #ENTRYS
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL', 15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApePaterno = tk.StringVar()
        self.entryApePaterno = tk.Entry(self, textvariable=self.svApePaterno)
        self.entryApePaterno.config(width=50, font=('ARIAL', 15))
        self.entryApePaterno.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svApeMaterno = tk.StringVar()
        self.entryApeMaterno = tk.Entry(self, textvariable=self.svApeMaterno)
        self.entryApeMaterno.config(width=50, font=('ARIAL', 15))
        self.entryApeMaterno.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svCurp = tk.StringVar()
        self.entryCurp = tk.Entry(self, textvariable=self.svCurp)
        self.entryCurp.config(width=50, font=('ARIAL', 15))
        self.entryCurp.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svFechNacimiento = tk.StringVar()
        self.entryFechNacimiento = tk.Entry(self, textvariable=self.svFechNacimiento)
        self.entryFechNacimiento.config(width=50, font=('ARIAL', 15))
        self.entryFechNacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svSegSocial = tk.StringVar()
        self.entrySegSocial = tk.Entry(self, textvariable=self.svSegSocial)
        self.entrySegSocial.config(width=50, font=('ARIAL', 15))
        self.entrySegSocial.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svAntecedentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=50, font=('ARIAL', 15))
        self.entryAntecedentes.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('ARIAL', 15))
        self.entryCorreo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL', 15))
        self.entryTelefono.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL', 15))
        self.entryEdad.grid(column=1, row=9, padx=10, pady=5, columnspan=2)

        #BOTONES
        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.btnNuevo.grid(column=0, row=10, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1, row=10, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#B00000', cursor='hand2', activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=10, padx=10, pady=5)

        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarSegSocial = tk.Label(self, text='Buscar NSS: ')
        self.lblBuscarSegSocial.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblBuscarSegSocial.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarApellido = tk.Label(self, text='Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblBuscarApellido.grid(column=3, row=1, padx=10, pady=5)

        #ENTRYS BUSCADOR
        self.svBuscarSegSocial = tk.StringVar()
        self.entryBuscarSegSocial = tk.Entry(self, textvariable=self.svBuscarSegSocial)
        self.entryBuscarSegSocial.config(width=30, font=('ARIAL',15))
        self.entryBuscarSegSocial.grid(column=4, row=0, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=30, font=('ARIAL',15))
        self.entryBuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

        #BUTTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self, text='Buscar', command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#00396F', cursor='hand2', activebackground='#5B8DBD')
        self.btnBuscarCondicion.grid(column=3, row=2, padx=10, pady=5, columnspan=1)

        #BUTTON LIMPIAR BUSCADOR
        self.btnLimpiarBuscador = tk.Button(self, text='Limpiar', command=self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#120061', cursor='hand2', activebackground='#7C6DC1')
        self.btnLimpiarBuscador.grid(column=4, row=2, padx=10, pady=5, columnspan=1)

        #BUTTON CALENDARIO
        self.btnCalendario = tk.Button(self, text='Calendario', command= self.vistaCalendario)
        self.btnCalendario.config(width=12, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#53005B', cursor='hand2',activebackground='#C774CF')
        self.btnCalendario.grid(column=3,row=4, padx=10, pady=5, columnspan=1)

    def vistaCalendario(self):
        self.calendario = Toplevel()
        self.calendario.title("FECHA NACIMIENTO")
        self.calendario.resizable(0,0)
        self.calendario.config(bg='#CDD8FF')

        self.svCalendario = StringVar(value= '01-01-1990')
        self.calendar = tc.Calendar(self.calendario, selectmode='day', year=1990, month=1, day=1, locale = 'es_US', bg='#777777', fg='#FFFFFF', headersbackground='#B6DDFE', textvariable=self.svCalendario, cursor = 'hand2', date_pattern='dd-mm-Y')
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column = 0)

        #TRACE ENVIAR FECHA
        self.svCalendario.trace('w',self.enviarFecha)

    def enviarFecha(self, *args):
        self.svFechNacimiento.set('' + self.svCalendario.get())
        if len(self.calendar.get_date()) > 1:
            self.svCalendario.trace('w', self.calcularEdad)

    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%d-%m-%Y")

        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
        self.svEdad.set(self.resul)

    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarSegSocial.set('')
        self.tablaPaciente()    
        
    def buscarCondicion(self):
        if len(self.svBuscarSegSocial.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarSegSocial.get())) > 0:
                where += " AND seguroSocial = '" + self.svBuscarSegSocial.get() + "'"
            if (len(self.svBuscarApellido.get())) > 0:
                where += " AND apellidoPaterno LIKE '" + self.svBuscarApellido.get()+"%'"
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()

    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApePaterno.get(), self.svApeMaterno.get(), self.svCurp.get(), self.svFechNacimiento.get(), self.svSegSocial.get(), self.svAntecedentes.get(), self.svCorreo.get(), self.svTelefono.get(), self.svEdad.get()
        )

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona) 

        self.deshabilitar()
        self.tablaPaciente()

    def habilitar(self):
        #self.idPersona = None
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svCurp.set('')
        self.svFechNacimiento.set('')
        self.svSegSocial.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')
        self.svEdad.set('')

        self.entryNombre.config(state='normal')
        self.entryApePaterno.config(state='normal')
        self.entryApeMaterno.config(state='normal')
        self.entryCurp.config(state='normal')
        self.entryFechNacimiento.config(state='normal')
        self.entrySegSocial.config(state='normal')
        self.entryAntecedentes.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryTelefono.config(state='normal')
        self.entryEdad.config(state='normal')

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')

    def deshabilitar(self):
        self.idPersona = None
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svCurp.set('')
        self.svFechNacimiento.set('')
        self.svSegSocial.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')
        self.svEdad.set('')

        self.entryNombre.config(state='disabled')
        self.entryApePaterno.config(state='disabled')
        self.entryApeMaterno.config(state='disabled')
        self.entryCurp.config(state='disabled')
        self.entryFechNacimiento.config(state='disabled')
        self.entrySegSocial.config(state='disabled')
        self.entryAntecedentes.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryTelefono.config(state='disabled')
        self.entryEdad.config(state='disabled')

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')

    def tablaPaciente(self, where=""):

        if len(where) > 0 :
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
            self.listaPersona.reverse

        self.tabla = ttk.Treeview(self, column=('Nombre', 'APaterno', 'AMaterno','Curp', 'FNamiento','SegSocial','Antecedentes','Correo','Telefono','Edad'))
        self.tabla.grid(column=0, row=11, columnspan=12, sticky='nsew')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=11, column=11, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Ap. Paterno')
        self.tabla.heading('#3', text='Ap. Materno')
        self.tabla.heading('#4', text='Curp')
        self.tabla.heading('#5', text='F. Nacimiento')
        self.tabla.heading('#6', text='NSS')
        self.tabla.heading('#7', text='Antecedentes')
        self.tabla.heading('#8', text='Correo')
        self.tabla.heading('#9', text='Telefono')
        self.tabla.heading('#10', text='Edad')

        self.tabla.column("#0", anchor=W, width=50)
        self.tabla.column("#1", anchor=W, width=150)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=120)
        self.tabla.column("#4", anchor=W, width=80)
        self.tabla.column("#5", anchor=W, width=100)
        self.tabla.column("#6", anchor=W, width=50)
        self.tabla.column("#7", anchor=W, width=300)
        self.tabla.column("#8", anchor=W, width=250)
        self.tabla.column("#9", anchor=W, width=82)
        self.tabla.column('#10', anchor=W, width=50)


        for p in self.listaPersona:
            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10]), tags=('evenrow'))

        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#1E0075', activebackground='#9379E0', cursor='hand2')
        self.btnEditarPaciente.grid(row=12, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=12, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente')
        self.btnHistorialPaciente.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=12, column=2, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
        self.btnSalir.grid(row=12, column=4, padx=10, pady=5)

    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidoPaternoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellidoMaternoPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.curpPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.fechaNacimientoPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.seguroSocialPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.antecedentesPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.correoPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][8]
            self.EdadPaciente = self.tabla.item(self.tabla.selection())['values'][9]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApePaterno.insert(0, self.apellidoPaternoPaciente)
            self.entryApeMaterno.insert(0, self.apellidoMaternoPaciente)
            self.entryCurp.insert(0, self.curpPaciente)
            self.entryFechNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entrySegSocial.insert(0, self.seguroSocialPaciente)
            self.entryAntecedentes.insert(0, self.antecedentesPaciente)
            self.entryCorreo.insert(0, self.correoPaciente)
            self.entryTelefono.insert(0, self.telefonoPaciente)
            self.entryEdad.insert(0, self.EdadPaciente)
        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title, mensaje)

    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)

            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar el paciente'