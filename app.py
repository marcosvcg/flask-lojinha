from flask import Flask, jsonify
from util.database import db, init_db
from controllers import product_bp, order_bp, order_item_bp, category_bp, address_bp
from flasgger import Swagger

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
init_db(app)

blueprints = [product_bp, order_bp, order_item_bp, category_bp, address_bp]

for bp in blueprints:
    app.register_blueprint(bp)

# https://localhost:5000/apidocs/  --> link do swagger-ui
swagger = Swagger(app, template_file='util/swagger.yaml')

@app.route('/')
def home():
    txt = [{'flask': 'primeiro app'}]
    return jsonify(txt)

if __name__ == '__main__':
    app.run(debug=True)