import pymysql as db
import csv

connection = db.connect(host='localhost', user='root', password='12345678', db='clothingShop')
print("connect succssful!")

try:
    with connection.cursor() as cursor:

        sql = "SELECT * FROM Suggest"
        result_count = cursor.execute(sql)
        rows = cursor.fetchall()
        for j in rows:
            print(j)
        column_names = [i[1] for i in cursor.description]
        print(column_names)

        c = csv.writer(open("/Users/admin/Desktop/Java/Hoc/SpringMVC/CollaborativeFiltering/DB/CF.csv", "w"), lineterminator='\n')
        # c.writerow(column_names)
        c.writerows(rows)
finally:
    connection.close()
