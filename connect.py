import sqlite3


def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS CONVERSES_SHOES (NAME TEXT ,SUBTITLE TEXT ,PRICE TEXT , SHIPPING TEXT)")
    print("Table created successfully")
    conn.close()


def insert_in_table(dbname, values):
    conn = sqlite3.connect(dbname)
    print("Inserted into table " + str(values))
    insert_sql = "INSERT INTO CONVERSES_SHOES (NAME , SUBTITLE , PRICE , SHIPPING) VALUES (?, ?, ?, ?)"
    conn.execute(insert_sql, values)
    conn.close()


def get_info(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM CONVERSES_SHOES ")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()





