from flask import Flask, request, render_template

import pandas as pd
from matplotlib import pyplot as Mplt
import seaborn as sb
import xlrd

Dados = pd.read_excel('static\PesquisaAuto.xlsx', 'Pesquisa')

'''histograma com densidade'''

sb.distplot(Dados["Imagem"], bins=10, kde=True)

Mplt.savefig('static\histogramaComDensidade.jpg');

'''dispersão com histograma'''

sb.jointplot(x="Preco", y="Imagem", data=Dados)

Mplt.savefig('static\dispersao.jpg')

'''box-plot'''

sb.boxplot(y="Imagem", data=Dados)

Mplt.savefig('static\_boxplot.jpg')

'''box-plot-categorizado'''

sb.boxplot(x="Idade", y="Imagem", data=Dados)

Mplt.savefig('static\_boxplotCategorizado.jpg')

'''barra com médias'''

sb.barplot(x="Genero", y="Imagem", data=Dados)

Mplt.savefig('static\_barraComMedias.jpg')


app = Flask(__name__)

@app.route ("/histograma", methods=["GET"])
def histograma():
    boxplot=request.a["boxplot"]
    return render_template("histograma.html")

@app.route ("/dispersao", methods=["GET"])
def dispersao():
    return render_template("dispersao.html")

if __name__ == "__main__":
    app.run(port=80)
