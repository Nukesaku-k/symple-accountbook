import datetime
from flask import Flask, render_template
from api.api import api_bp
from api.models import t_items
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myspa.db'
app.register_blueprint(api_bp)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        t_items.init_db(app)
        try:
            t_items.get_all()
        except NoResultFound:
            t_items.insert('初期アイテム', 50000, '27', datetime.datetime.today())
    app.run()
