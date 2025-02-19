from flask import Blueprint, render_template, request, redirect, url_for
from db import queries

client_blueprint = Blueprint("client", __name__)


@client_blueprint.route("/clienthome")
def clienthome():
    productos = queries.getProducts()
    print(productos)
    return render_template("clients/clientProducts.html", productos = productos)


@client_blueprint.route("/productos", methods=["GET", "POST"])
def ascDesc():
    orden = request.args.get("orden", "asc")
    if orden == "desc":
       productosOrdenados = queries.descProducts()
       return render_template("clients/clientProducts.html", productos = productosOrdenados)
    else:
        productosOrdenados = queries.ascProducts()
        return render_template("clients/clientProducts.html", productos = productosOrdenados)
    
@client_blueprint.route("/filtrar", methods=["GET", "POST"])
def filtrar():
    min_precio = request.args.get("min_precio")
    max_precio = request.args.get("max_precio")
    categoria = request.args.get("categoria")
    print(min_precio, max_precio, categoria)
    return render_template("clients/clientProducts.html")