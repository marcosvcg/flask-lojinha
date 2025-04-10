from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    
    from models import Product, Order, OrderItem, Category, Address

    with app.app_context():
        db.drop_all()
        db.create_all()
        create_dummy_data()

def create_dummy_data():
    # Inserção das categorias diretamente via SQL
    db.session.execute(
        text("INSERT INTO categories (name) VALUES ('Eletrônicos'), ('Roupas')")
    )
    db.session.commit()  # Commit após a execução das inserções

    # Inserção dos produtos diretamente via SQL
    db.session.execute(
        text(
            "INSERT INTO products (name, description, price, stock, category_id) "
            "VALUES ('iPhone 15 Pro', 'iPhone da mais nova geração', 9499.99, 10, 1), "
            "('Camiseta Estilosa', 'Camiseta unissex, confortável e estilosa', 50.00, 100, 2)"
        )
    )
    db.session.commit()

    # Inserção dos endereços diretamente via SQL
    db.session.execute(
        text(
            "INSERT INTO addresses (postcode, state, city, street, number) "
            "VALUES ('12345-678', 'São Paulo', 'São Paulo', 'Rua dos Três Irmãos', '123'), "
            "('98765-432', 'Rio de Janeiro', 'Rio de Janeiro', 'Avenida Brasil', '456')"
        )
    )
    db.session.commit()

    # Inserção dos pedidos diretamente via SQL
    db.session.execute(
        text(
            "INSERT INTO orders (order_date, status, total_price, completed_at, address_id) "
            "VALUES (CURRENT_TIMESTAMP, 'pending', 1200.00, NULL, 1), "
            "(CURRENT_TIMESTAMP, 'delivered', 50.00, CURRENT_TIMESTAMP, 2)"
        )
    )
    db.session.commit()

    # Inserção dos itens de pedido diretamente via SQL
    db.session.execute(
        text(
            "INSERT INTO order_items (order_id, product_id, product_quantity, price_at_time_of_order) "
            "VALUES (1, 1, 1, 1200.00), "
            "(2, 2, 2, 50.00)"
        )
    )
    db.session.commit()

    print("✅ Dummy data created successfully!")