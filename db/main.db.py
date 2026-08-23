import sqlite3
from db import queries 

path_db = 'db/sqlite3.db'


async def init_db():
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_products_table)
    cursor.execute(queries.create_table_products_detail)
    print('DB подключена!')
    conn.commit()
    conn.close()


async def add_product_db(name_product, price, product_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_product, (name_product, price, product_id))
    conn.commit()
    conn.close()


async def get_product_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.select_product)
    products = cursor.fetchall()
    conn.close()
    return products