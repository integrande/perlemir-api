"""
    Author:     Lane Adair (ladair@unca.edu)
    Date:       March 5, 2020
    Version:    0.0.1
"""
import json
import bot
from perlemir_api import app

bot_list = []   

def name_bot(request):
    return 200

def create_bot(request):
    return 201

def pop_bot(request):
    return 200

def get_bots():
    if bot_list == null:
        return {'message' : 'No bots are found!'}, 404
    else:
        bot_json = json.dumps(bot_list)



        return {'message' : 'Request timed out. Please reload page!'}, 200

def test(request):
    return request.get_json()