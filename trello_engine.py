# trello_engine.py

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TRELLO_KEY = os.environ['TRELLO_API_KEY']
TRELLO_TOKEN = os.environ['TRELLO_TOKEN']
BOARD_ID = os.environ['TRELLO_BOARD_ID']

def create_card(name, description, list_id):
    url = f"https://api.trello.com/1/cards"
    params = {
        'key': TRELLO_KEY,
        'token': TRELLO_TOKEN,
        'idList': list_id,
        'name': name,
        'desc': description
    }
    r = requests.post(url, params=params)
    return r.json()

@app.route('/create_job', methods=['POST'])
def create_job():
    data = request.json
    job_name = data.get('job_name')
    job_desc = data.get('job_desc')
    list_id = data.get('list_id')

    result = create_card(job_name, job_desc, list_id)
    return jsonify(result), 200

@app.route('/')
def hello():
    return "Trello Engine is online."

if __name__ == '__main__':
    app.run()
