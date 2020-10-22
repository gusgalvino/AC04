import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def fibonacci():
    sequencia = [0, 1]
    limite = 48
    for i in range(limite):
        soma = sequencia[i] + sequencia[i+1]
        sequencia.append(soma)
    return str(sequencia).strip('[]')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)
