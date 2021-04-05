import psycopg2

conexion1 = psycopg2.connect("dbname=postgres user=postgres password=admin1234")
cursor1=conexion1.cursor()
cursor1.execute("delete from inventario where idproducto=1")
cursor1.execute("delete from inventario where idproducto=2")
cursor1.execute("delete from inventario where idproducto=3")
cursor1.execute("update inventario set precio=20 where idproducto=4")
conexion1.commit()
cursor1.execute("select idproducto, producto, precio, cantidad from inventario")
for fila in cursor1:
    print(fila)
conexion1.close()    