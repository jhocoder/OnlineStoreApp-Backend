from flask import Blueprint, request, render_template, redirect, url_for
from db import queries



admin_blueprint = Blueprint("admin", __name__)


@admin_blueprint.route("/products", methods=["GET","POST"])
def products():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        categoria = request.form["categoria"]
        stock = request.form["stock"]
        print(stock)
        agregado = queries.addProduct(nombre, descripcion, precio, categoria, stock)
        print(agregado)
        return redirect(url_for("admin.products"))
    if request.method == "GET":
        vertodos = queries.getProducts()
        print(vertodos)
        
    return render_template("admin/products.html", products=vertodos)


@admin_blueprint.route("/edit/<string:id>", methods=["GET","POST"])
def edit(id):
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        categoria = request.form["categoria"]
        stock = request.form["stock"]
        updateproduct = queries.updateProduct(id, nombre, descripcion, precio, categoria, stock)
        print(updateproduct)
        return redirect(url_for("admin.products"))
    if request.method == "GET":
        queryId = queries.getProduct(id)
        print(queryId)
        return render_template("admin/edit.html", producto = queryId)
    
@admin_blueprint.route("/delete/<string:id>", methods=["POST"])
def delete(id):
    if request.method == "POST":
        deleteItem = queries.deleteProduct(id)
        if deleteItem:
            return redirect(url_for("admin.products"))
        



