import MySQLdb


def mostrar():

	miConexion = MySQLdb.connect( 
		host='localhost',
		 user= 'root', 
		 passwd='cuaderno23', 
		 db='Lista_Omar_Blanco' )

	cursor = miConexion.cursor()

	cursor.execute( "SELECT codigo, nombre, apellido, cedula, telefono FROM Comando1" )

	for codigo, nombre, apellido, cedula, telefono in cursor.fetchall() :

		print(codigo, nombre, apellido, cedula, telefono)

	miConexion.close()
