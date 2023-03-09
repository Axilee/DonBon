from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def handle_webhook():
    print("e")
    data = request.get_json()
    print (data)
    # process the data received from the webhook
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)