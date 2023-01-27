from flask import Flask

app=Flask(__name__)

@app.route("/")
def intex():
    return "hola mundo  Flask Cambos nuevos "

    
if __name__ == "__main__":
    app.run(debug=True)

