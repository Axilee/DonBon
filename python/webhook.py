from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_webhook():
    print("e")
    # data = request.get_json()
    code = request.args.get('code') #pobiera ten jebany kod
    scope = request.args.getlist('scope') #pobiera scope permisji //lista
    
    
    print (f"Scope={scope}\n\nKod = {code}\n\n")
    # process the data received from the webhook
    return f'<h1><b>scope = {scope}<br>kod = {code}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)