from flask import Flask
from flask import request
import trans
import waitress

app = Flask(__name__)

app.json.ensure_ascii = False  # 确保不转为ascii


@app.route("/translate", methods=["GET"])
def service1():
    """使用翻译"""
    args = request.args
    return trans.translate(**args)


@app.errorhandler(404)
def not_found(error):
    return "Not Found", 404


if __name__ == "__main__":
    waitress.serve(app=app, host="0.0.0.0", port=8000)
