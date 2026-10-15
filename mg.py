import json, time, hashlib
from flask import Flask, jsonify

app = Flask(__name__)

MG_COIN = {
  "address": "0xfb516632419c252d70aa0c22f0962b2c0bf22865",
  "name": "MG-COIN",
  "symbol": "MGC",
  "isNative": True,
  "chain": "MG-CHAIN",
  "chainId": 7777,
  "decimals": 18
}

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/')
def home():
    return jsonify({
        "network": "MG-CHAIN is INSIDE MG-COIN",
        "coin": MG_COIN,
        "status": "Live",
        "rpc": "Use /chain for RPC",
        "message": "MG-CHAIN Network - Native coin is MG-COIN"
    })

@app.route('/chain')
def chain_info():
    return jsonify(MG_COIN)

@app.route('/token')
def token():
    return jsonify(MG_COIN)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
