import tkinter as tk
from constantes import style

from funciones.mostrar_personas import mostrar

from funciones.agregar_personas import agregar_persona

class Inicio(tk.Frame):

	def __init__(self, parent, controller):

		super().__init__(parent)

		self.configure(background = style.BACKGROUND)
		self.controller=controller

		self.init_widgets()

	def cambio(self):

		self.controller.show_frame(Registro)

	def init_widgets(self):

		optionsFrame= tk.Frame(self)

		optionsFrame.configure(
			background=style.FRAMEOPCIONES, 
			width=250, height=460,
			relief='groove', bd=5)

		optionsFrame.place(x=10, y=10)

		tk.Label(optionsFrame, text="Opciones de Manejo", **style.STYLE).place(x=2, y=30)

		tk.Button(optionsFrame, text="Validar", **style.STYLE_BOTON, width=18).place(x=25, y=120)

		tk.Button(optionsFrame, text="Registrar", **style.STYLE_BOTON, width=18, command=self.cambio).place(x=25, y=190)

		tk.Button(optionsFrame, text="Eliminar", **style.STYLE_BOTON, width=18).place(x=25, y=260)

		tk.Button(optionsFrame, text="Listado", **style.STYLE_BOTON, width=18, command=mostrar).place(x=25, y=360)

		#--------------VALIDAR-----------------

		registroFrame= tk.Frame(self)

		registroFrame.configure( 
			width=620, height=460,
			relief='groove', bd=5,
			background=style.FRAMEOPCIONES)
		registroFrame.place(x=270, y=10)

		tk.Label(registroFrame, text="Validacion", **style.STYLE).place(x=160, y=50)

		tk.Label(registroFrame, text="Nombre:", **style.STYLE).place(x=50, y=155)
		tk.Entry(registroFrame, **style.STYLE_ENTRY).place(x=30, y=190)

		tk.Label(registroFrame, text="Cedula:", **style.STYLE).place(x=310, y=155)
		tk.Entry(registroFrame,**style.STYLE_ENTRY).place(x=310, y=190)

		tk.Button(registroFrame, text="Comprobar", **style.STYLE_BOTON, width=15).place(x=300, y=300)


class Registro(tk.Frame):

	def __init__(self, parent, controller):
		
		super().__init__(parent)

		self.controller=controller

		self.nom=tk.StringVar()
		self.apel=tk.StringVar()
		self.cc=tk.IntVar()
		self.tel=tk.IntVar()

		self.init_widgets()

	def cambiar(self):
		
		self.controller.show_frame(Inicio)

	def init_widgets(self):
		#---------opciones----------------
		
		RegFrame= tk.Frame(self)

		RegFrame.configure(
			background=style.FRAMEOPCIONES, 
			width=250, height=460,
			relief='groove', bd=5)

		RegFrame.place(x=10, y=10)

		tk.Label(RegFrame, text="Opciones de Manejo", **style.STYLE).place(x=2, y=30)

		tk.Button(RegFrame, text="Validar", **style.STYLE_BOTON, width=18, command=self.cambiar).place(x=25, y=120)

		tk.Button(RegFrame, text="Registrar", **style.STYLE_BOTON, width=18).place(x=25, y=190)

		tk.Button(RegFrame, text="Eliminar", **style.STYLE_BOTON, width=18).place(x=25, y=260)

		tk.Button(RegFrame, text="Listado", **style.STYLE_BOTON, width=18, command=mostrar).place(x=25, y=360)

		#----------REGISTRO------------------

		RegFrame2= tk.Frame(self)

		RegFrame2.configure(
			background=style.FRAMEOPCIONES, 
			width=620, height=460,
			relief='groove', bd=5)

		RegFrame2.place(x=270, y=10)

		#----------VARIABLES ENTRY -------------------
		
		tk.Label(RegFrame2, text="Nombre:",**style.STYLE).place(x=30, y=50)
		tk.Entry(RegFrame2, **style.STYLE_ENTRY, textvariable=self.nom).place(x=30, y=90)

		tk.Label(RegFrame2, text="Apellido:", **style.STYLE).place(x=300, y=50)
		tk.Entry(RegFrame2, **style.STYLE_ENTRY, textvar=self.apel).place(x=300, y=90)

		tk.Label(RegFrame2, text="Cedula:", **style.STYLE).place(x=30, y=150)
		tk.Entry(RegFrame2, **style.STYLE_ENTRY, textvar=self.cc).place(x=30, y=190)

		tk.Label(RegFrame2, text="Telefono:", **style.STYLE).place(x=300, y=150)
		tk.Entry(RegFrame2, **style.STYLE_ENTRY, textvar=self.tel).place(x=300, y=190)

		tk.Button(
			RegFrame2, 
			text="Registrar *",
			 **style.STYLE_BOTON,
			  width=15, 
			  command=lambda:agregar_persona(3, self.nom.get(), self.apel.get(), self.cc.get(), self.tel.get())).place(x=300, y=300)



