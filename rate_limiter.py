from flask import make_response, jsonify


def on_breach(req_limit):
    print("Breached")
    # print((req_limit))
    return make_response(jsonify(status="Failure", message="Rate Limit Exceeded"), 429)