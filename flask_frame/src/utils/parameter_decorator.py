import functools

from flask import request, g, abort


class Validate:

    @staticmethod
    def check_params(params, params_type="body"):
        def check(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if params_type == "body":
                    data = get_json_data()
                elif params_type == "args":
                    data = request.args
                check_params_or_400(params, data)
                return func(*args, **kwargs)

            return wrapper

        return check


def get_json_data(limits=[]):
    json_data = {}
    if hasattr(g, "request") and g.request.get("json_data"):
        json_data = g.request["json_data"]
    else:
        json_data = request.json or {}

    if limits:
        return {key: json_data[key] for key in limits if json_data.get(key) is not None}

    return json_data


def check_params_or_400(params, data):
    '''检测必要参数'''
    for key in params:
        if key not in data:
            abort(400, description=f"缺少必要參數{key}")
    return True


