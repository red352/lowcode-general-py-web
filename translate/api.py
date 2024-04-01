from flask import Blueprint
from flask import request
import translate.translate as translate

api = Blueprint("translateapi", __name__, url_prefix="/translate")


# 定义蓝图的路由和功能
@api.route("/", methods=["GET"])
def service1():
    """使用翻译"""
    args = request.args
    return translate.translate(**args)
