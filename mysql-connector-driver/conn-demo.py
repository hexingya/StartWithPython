import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", passwd="mariadbroot", database="employeedb"
)

cursor = db.cursor()

# sql = "insert into employees (birth_date, first_name, last_name, gender, hire_date) values (%s, %s, %s, %s, %s)"

# data = [
#     ("2000:02:12", "Anck", "Ame", "M", "2019-03-01"),
#     ("2000:02:12", "Anck", "Ame", "M", "2019-03-01"),
#     ("2000:02:12", "Anck", "Ame", "M", "2019-03-01"),
#     ("2000:02:12", "Anck", "Ame", "M", "2019-03-01"),
#     ("2000:02:12", "Anck", "Ame", "M", "2019-03-01"),
#     ("2000:02:12", "Anck", "Ame", "M", "2019-03-01"),
#     ("2000:02:12", "Anck", "Ame", "M", "2019-03-01"),
# ]

# cursor.executemany(sql, data)

# db.commit()

# print("Rows inserted: ", cursor.rowcount)
# print("Last inserted row's ID: ", cursor.lastrowid)


# cursor.execute("select * from employees where emp_no >= 500 order by first_name desc")

# result = cursor.fetchall()

# cursor.execute("drop table if exists other")


cursor.execute("show tables")

result = cursor.fetchall()

for x in result:
    print(x)
