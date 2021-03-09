"""
    The app.py file will hold all the active endpoints
    for the application and will pose calls to the proper
    functions for each URL.
"""
from config import config
from user import user_fun
from bot import bot_fun
import json

if config.DEBUG:
    print("DEBUG IS ON")

# create the Flask app
app = config.Flask(__name__)
app.secret_key = 'ACM_PERLEMIR_TEST'


#*********************************************************
#                      USER ENDPOINTS
#*********************************************************


@app.route('/api/v1/user/user_get_nonce', methods=['GET'])
def user_get_nonce():
    return user_fun.nonce(config.request)


@app.route('/api/v1/user/user_login', methods=['POST'])
def user_login():
    return user_fun.login(config.request)

@app.route('/api/v1/user/user_logout', methods=['POST'])
def user_logout():
    config.session.pop('uid', None)
    return redirect(url_for('index'))

@app.route('/api/v1/user/user_get_settings', methods=['POST'])
def user_get_settings():
    return "d"

@app.route('/api/v1/user/user_change_settings', methods=['POST'])
def user_change_settings():
    return "d"

#*********************************************************
#                      BOT ENDPOINTS
#*********************************************************

@app.route('/api/v1/bot/<id>/get_price', methods=['POST'])
def get_price(id):
    return bot_fun.get_price(config.request)

@app.route('/api/v1/bot/<id>/get_settings', methods=['GET'])
def get_settings(id):
    return bot_fun.get_settings(config.request)

@app.route('/api/v1/bot', methods=['GET'])
def get_bots(): 
    return bot_fun.get_bots(config.request)



#*********************************************************
#                      TEST ENDPOINT
#*********************************************************
@app.route('/api/v1/<num>/test', methods=['POST'])
def test(num): 
    return num

#run the program
if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
 
