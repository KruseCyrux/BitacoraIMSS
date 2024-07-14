import tkinter as tk
from paciente.gui import Frame 
def main():
    root = tk.Tk()
    root.title('HISTORIAL MEDICO')
    root.resizable(0,0)
    root.iconbitmap('C:/Users/cracb/OneDrive/Escritorio/MediTrack/historialMedico/img/clinica.ico')
    frame = Frame(root)
    frame.mainloop()

if __name__ == '__main__':    
    main()