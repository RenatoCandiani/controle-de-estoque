from flask import Flask

app = Flask(__name__)
class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def to_dict(self):
        return {
            name: self.name,
            age: self.age
        }
renato = User("Jorge", 19)
@app.route("/")
def hello_world():
    user = renato
    informacao = "eu sou viado"
    return f"Oi: {user.name} informação: {informacao}"
@app.route("/compras")
def compras():
    return "compras"

app.run(debug=True)