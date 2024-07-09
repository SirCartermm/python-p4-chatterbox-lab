from flask import Flask, request, make_response, jsonify # type: ignore
from flask_cors import CORS # type: ignore
from flask_migrate import Migrate # type: ignore

from models import db, Message
from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
from models import Message

app = Flask(__name__)
CORS(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages')
def messages():
    return ''

@app.route('/messages/<int:id>')
def messages_by_id(id):
    return ''

if __name__ == '__main__':
    app.run(port=5555)
