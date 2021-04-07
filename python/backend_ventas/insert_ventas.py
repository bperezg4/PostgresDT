import psycopg2

conexion1 = psycopg2.connect("dbname=postgres user=postgres password=admin1234")
cursor1=conexion1.cursor()
sql="insert into ventas(descripcion, precio, cantidad) values (%s,%s,%s)"
datos=("Caja te de manzanilla", 30, 5)
cursor1.execute(sql, datos)
datos=("mascarillas", 2, 5)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close() 