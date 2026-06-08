from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/photo")
def photo():
    return "这里是摄影页面（后面再做）"

@app.route("/video")
def video():
    return "这里是视频页面"

@app.route("/media")
def media():
    return "这里是运营页面"

@app.route("/writing")
def writing():
    return "这里是文案页面"