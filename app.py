from flask import Flask, render_template, request
from flask_mobility import Mobility
from locator.locator import Locator

app = Flask(__name__)
port = 4500

Mobility(app)

@app.route('/')
def home():
    ip = request.args.get('ip')

    locator = Locator()
    details = locator.getDetails(ip)

    return render_template(
        'index.html',
        ip=details['ip'],
        country=details['country'],
        region=details['region'],
        loc=details['loc']
    )

if __name__ == '__main__':
    app.run(debug=True, port=port)