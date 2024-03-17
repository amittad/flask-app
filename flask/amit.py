from  flask import Flask, render_template
app =Flask(__name__)

@app.route("/")
def amit():
    return render_template('index.html')
@app.route("/boss")
def boss():
    return "hello welcome two the boss website"
@app.route("/king")
def king():
    return "hello welcome two the king website"
@app.route("/coder")
def coder():
    return "hello welcome two flake"
if __name__=="__main__":
 app.run(debug=True, port=8000)
