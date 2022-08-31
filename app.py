from flask import Flask, send_from_directory, url_for, render_template
from controller.voice import voice_controller

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dZwwMGShspJPSCjuwty4nbGOQPlzhXcA#^b03h&y%S|2>vGyVr=e*@Z_b1<{'

app.register_blueprint(voice_controller, url_prefix='/api/v1/voice')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/voice")
def aaaaaaa():
    return render_template("voice_to_text.html")


#@app.errorhandler(404)
#def page_not_found(e):
#    return "404 Error (Page not found)"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
