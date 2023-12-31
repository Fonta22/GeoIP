from flask import Flask, render_template, request
from flask_mobility import Mobility
from locator.locator import Locator

app = Flask(__name__)
port = 4500

Mobility(app)

@app.route('/')
def home():
    ip = request.args.get('ip')

    locator = Locator(ip)
    details = locator.getDetails()

    try:
        return render_template(
            'index.html',
            ip=details['ip'],
            country=details['country'],
            region=details['region'],
            loc=details['loc']
        )
    except:
        print(details['message'])
        return render_template(
            'error.html',
            status_code=details['status_code'],
            invalid_ip=ip
        )

if __name__ == '__main__':
    app.run(debug=True, port=port)