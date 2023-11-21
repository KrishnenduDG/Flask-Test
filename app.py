from flask import Flask,jsonify
from config import limiter
from rate_limiter import on_breach


def create_app():
    app = Flask(__name__)

    # Configuring the Limiter
    limiter.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()

    @app.route("/get-route",methods=["GET"])
    @limiter.limit("2/hour", on_breach=on_breach)
    def getRouteHandler():
        return jsonify(status="success",msg="Hello world")
    
    # app.run(host="0.0.0.0", port=7000, debug=False)
