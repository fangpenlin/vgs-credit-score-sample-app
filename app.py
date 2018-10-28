import hashlib
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/credit-score')
def index():
    ssn = request.args['ssn']
    hashed = hashlib.sha1(ssn.encode('utf8'))
    credit_score = 100 + int(hashed.hexdigest(), 16) % 750
    return jsonify(
        credit_score=credit_score
    )