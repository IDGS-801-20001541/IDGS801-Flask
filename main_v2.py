from flask import Flask

app=Flask(__name__)

@app.route("/")
def intex():
    return "hola mundo  "

@app.route("/hola")
def hola():
    return "Hola desde hola XD  "
    
@app.route("/nueva")
def nueva():
    return "Hola desde Nueva  "
   

if __name__ == "__main__":
    app.run(debug=True)

