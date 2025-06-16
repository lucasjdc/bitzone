from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')

def ola():
    lista = ['Duck Tales', 'Super Mario Bros 2', 'Metroid', 'Zelda', 'Mega Man 2' ]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()