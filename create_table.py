import sqlite3

conn = sqlite3.connect('DB.db')
print("connect successfully")

#可以在這裡建立table 和 data (要在commit()之前完成 )
conn.execute(
    'CREATE TABLE IF NOT EXISTS product(product_id INTEGER , name TEXT , type_id INTEGER , amount INTEGER , price INTEGER , origin TEXT , rating REAL ) ')
conn.execute(
    "INSERT INTO product(product_id , name , type_id , amount , price , origin , rating )VALUES(?,?,?,?,?,?,?)", (1, 'iphone', 3, 10, 23900, 'taipei', 3.9))
conn.commit()
print("add seccessfully")

conn.close()
