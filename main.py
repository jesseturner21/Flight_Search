from flask import Flask, render_template, request
from database import Database
from flight_checker import FlightChecker

# -------------------Flask------------------#
app = Flask(__name__, static_url_path='/static')

# -------------------CONTROL------------------#
fc = FlightChecker()
db = Database()


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print('in hello')
    if request.method == 'POST':
        print('in request')
        email = request.form.get('email')
        fly_from = request.form.get('fly_from')
        fly_to = request.form.get('fly_to')
        price_to = request.form.get('price')
        date_from = request.form.get('date_from')
        date_to = request.form.get('date_to')
        return_from = request.form.get('return_from')
        return_to = request.form.get('return_to')
        # Add user to database
        code = fc.get_codes([fly_from, fly_to])
        db.add_user(email=email, fly_from=code[0], fly_to=[code[1]], date_from=date_from,
                    date_to=date_to, return_from=return_from, return_to=return_to, price_to=[price_to])

        return render_template("submitted.html")

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
