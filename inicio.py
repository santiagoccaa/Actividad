import tkinter as tk
from constantes import style
from frames import *

class App(tk.Tk):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.config(bg="#FFFFFF")
		self.geometry("900x480")
		self.resizable(0,0)
		self.title("Inicio")
	
		container=tk.Frame(self)

		container.pack(
			side = tk.TOP,
			fill = tk.BOTH,
			expand = True
		)

		container.configure(background = style.BACKGROUND)
		container.grid_columnconfigure(0, weight=1)
		container.grid_rowconfigure(0, weight=1)

		self.frames = {}

		for F in (Inicio, Registro):

			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky= tk.NSEW)
		self.show_frame(Inicio)


	def show_frame(self, container):

		frame=self.frames[container]
		frame.tkraise()

