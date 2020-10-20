import sqlite3

db = sqlite3.connect("university.db")
cursor=db.cursor() #相当于一个指针

# cursor.execute("""CREATE TABLE IF NOT EXISTS students 
# (id integer PRIMARY KEY, name text NOT NULL, gender text NOT NULL, age ineger NOT NULL);""") #新建一个表，里面是SQL的伪代码

# cursor.execute("""INSERT INTO students(id, name, gender, age) 
# VALUES(4, 'wang_shaoping', 'male', 18)""")
# cursor.execute("""INSERT INTO students(id, name, gender, age) 
# VALUES(5, 'shi_haixu', 'male', 19)""")
# cursor.execute("""INSERT INTO students(id, name, gender, age) 
# VALUES(6, 'zhou_zhiyong', 'male', 17)""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS class
# (class_number integer PRIMARY KEY, class_name text NOT NULL, teacher_name text NOT NULL);""") # ineger 是整数 real 是小数 
# cursor.execute("""INSERT INTO class(class_number, class_name, teacher_name) 
# VALUES(10001, 'water_class_1', 'Guolin_Li')""")
# cursor.execute("""INSERT INTO class(class_number, class_name, teacher_name) 
# VALUES(10002, 'water_class_2', 'Milin_Zhang')""")
# cursor.execute("""INSERT INTO class(class_number, class_name, teacher_name) 
# VALUES(10003, 'water_class_3', 'Hao_Zhang')""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS enrolled
# (student_id integer NOT NULL, class_number_chosen integer NOT NULL, grade integer NOT NULL);""")

# cursor.execute("""INSERT INTO enrolled(student_id, class_number_chosen, grade) 
# VALUES(1, 10001, 80)""")

# cursor.execute("""INSERT INTO enrolled(student_id, class_number_chosen, grade) 
# VALUES(1, 10002, 80)""")

# cursor.execute("""INSERT INTO enrolled(student_id, class_number_chosen, grade) 
# VALUES(1, 10003, 80)""")

db.commit() #保存数据库

# cursor.execute("""SELECT students.id, students.name, students.gender, students.age, enrolled.class_number_chosen, enrolled.grade FROM students JOIN 
# enrolled on students.id = enrolled.student_id""")
 
cursor.execute("""SELECT students.id, students.name, students.gender, students.age, enrolled.class_number_chosen, 
enrolled.grade,class.class_name ,class.teacher_name
FROM students JOIN enrolled ON students.id = enrolled.student_id JOIN class ON enrolled.class_number_chosen = class.class_number """)

print(cursor.fetchall())
db.close() #不要忘记关闭连接

# class.class_name class.teacher.name JOIN class ON enrolled.class_number_chosen = class.class_number)