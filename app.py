from flask import Flask
import waitress
from translate.api import api as translateapi

app = Flask(__name__)

app.json.ensure_ascii = False  # 确保不转为ascii


@app.errorhandler(404)
def not_found(error):
    return "Not Found", 404

app.register_blueprint(translateapi)

if __name__ == "__main__":
    waitress.serve(app=app, host="0.0.0.0", port=8000)
