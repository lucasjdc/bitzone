from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)

@app.route('/inicio')

def ola():
    jogo1 = Jogo('Tomb Raider: Atlantean Scion','Ação-aventura','Sega Saturn')
    jogo2 = Jogo('The Legend of Zelda','Ação-aventura','Nintendo')
    jogo3 = Jogo('Mortal Kombat','Luta','PS2')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()