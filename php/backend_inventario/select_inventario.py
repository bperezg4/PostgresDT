import psycopg2

conexion1 = psycopg2.connect("dbname=postgres user=postgres password=admin1234")

cursor1=conexion1.cursor()
cursor1.execute("select idproducto, producto, precio, cantidad from inventario")
for fila in cursor1:
    print(fila)
conexion1.close()