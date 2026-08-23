create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_product TEXT NOT NULL,
        price INTEGER,
        product_id INTEGER NOT NULL, 
        photo_id TEXT
    )
"""

insert_product = "INSERT INTO products (name_product, price, product_id, photo_id) VALUES (?, ?, ?, ?)"
insert_product = 'SEKECT name_product, price, product_id, photo_id FROM products'