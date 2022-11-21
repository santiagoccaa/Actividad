import MySQLdb


from tkinter import messagebox

def agregar_persona(cod, nom, apel, cc, tel):

	try:
		miConexion = MySQLdb.connect( 
			host='localhost',
			user= 'root', 
			passwd='cuaderno23', 
			db='Lista_Omar_Blanco' )

		cursor = miConexion.cursor()

		sql= "INSERT INTO Comando1 (codigo, nombre, apellido, cedula, telefono)  Values ('{}','{}','{}','{}','{}')".format(cod, nom, apel, cc, tel)

		cursor.execute(sql)

		messagebox.showinfo('Aviso', 'Persona agregada correctamente')

	except:
		messagebox.showwarning('Erro', 'Erro')
