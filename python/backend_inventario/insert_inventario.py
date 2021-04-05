import psycopg2

conexion1 = psycopg2.connect("dbname=postgres user=postgres password=admin1234")
cursor1=conexion1.cursor()
sql="insert into inventario(producto, precio, cantidad) values (%s,%s,%s)"
datos=("Tapcin", 23.50, 30)
cursor1.execute(sql, datos)
datos=("Ibuprofeno", 34.50, 10)
cursor1.execute(sql, datos)
datos=("Mascarillas", 25.75, 5)
cursor1.execute(sql, datos)
datos=("Caja te de manzanilla", 30, 5)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close() 