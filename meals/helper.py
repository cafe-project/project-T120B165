import json

from django.core.handlers.wsgi import WSGIRequest


def parse_json_from_request(request: WSGIRequest) -> dict:
    if not request.body:
        pass

    try:
        parameters = json.loads(request.body.decode('UTF-8'))  # type: dict
    except Exception as ex:
        raise Exception(ex)

    return parameters