from flask import Flask
from flask import render_template
import grupos

app = Flask(__name__)


#templates de direcionamento
@app.route ("/home", methods=["GET"])
def home():
    return render_template("index.html")

@app.route ("/projetos", methods=["GET"])
def projetos():
    return render_template("projetos.html")

@app.route ("/contato", methods=["GET"])
def contato():
    return render_template("contato.html")

@app.route ("/sobre", methods=["GET"])
def sobre():
    return render_template("sobre.html")

#templates de funcoes
@app.route ("/", methods=["GET"])
@app.route ("/home", methods=["GET"])
def index():
    grupos.gravaAlunos()
    nomesAlunos = grupos.listaAlunos()
    return render_template("index.html", nomes=nomesAlunos)





if __name__ == "__main__":
    app.run(port=80)