from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def intex():
    return render_template("index.html")
    
@app.route("/calcular",methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/resultado",methods=['POST'])
def resultado():
        n1=request.form.get("txtNum1")
        n2=request.form.get("txtNum2")
        res= int(n1)+int(n1)
        return render_template("usuarios.html",res,n1,n2)

if __name__ == "__main__":
    app.run(debug=True)
