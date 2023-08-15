from flask import Flask, render_template, request
from database import Database
from flight_checker import FlightChecker
from Email import Email

# -------------------Flask------------------#
app = Flask(__name__, static_url_path='/static')

# -------------------CONTROL------------------#
fc = FlightChecker()
db = Database()
em = Email()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    print('in add')
    if request.method == 'POST':
        email = request.form.get('email')
        fly_from = request.form.get('fly_from')
        fly_to = request.form.get('fly_to')
        fly_to = fly_to.split(',')
        price_to = request.form.get('price')
        price_to = [int(x) for x in price_to.split(',')]
        date_from = request.form.get('date_from')
        date_to = request.form.get('date_to')
        return_from = request.form.get('return_from')
        return_to = request.form.get('return_to')
        # Add user to database
        from_code = fc.get_codes([fly_from])
        to_code = fc.get_codes(fly_to)
        db.add_user(email=email, fly_from=from_code[0], fly_to=to_code, date_from=date_from,
                    date_to=date_to, return_from=return_from, return_to=return_to, price_to=price_to)
        # CANT SEND EMAIL THROUGH RENDER
        # body = "User information: \nEmail: " + email + " \nFly from: " + from_code[
        #     0] + " \nFly to: " + request.form.get('fly_to') + \
        #        "\nFor: " + request.form.get('price') + " \nDepart : " + date_from + " - " + date_to + "\nReturn : " + return_from + " - " + return_to
        # em.send_email(receiver=email, subject="FLIGHT CHECKER CONFIRMATION", body=body)
        return render_template("submitted.html")

    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        email = request.form.get('email')
        user = db.get_user(email)
        user['fly_from'] = fc.get_names([user['fly_from']])[0]
        fly_to_names = fc.get_names(user['fly_to'])
        user['fly_to'] = ','.join(fly_to_names)
        print(user['fly_to'])
        user['price_to'] = ','.join(str(x) for x in user['price_to'])
        user['return_from'] = user['return_from ']

        return render_template('edit-add.html', user=user)
    return render_template('edit.html')


@app.route('/edit-add', methods=['GET', 'POST'])
def edit_add():
    if request.method == 'POST':
        email = request.form.get('email')
        fly_from = request.form.get('fly_from')
        fly_to = request.form.get('fly_to')
        fly_to = fly_to.split(',')
        price_to = request.form.get('price')
        price_to = [int(x) for x in price_to.split(',')]
        date_from = request.form.get('date_from')
        date_to = request.form.get('date_to')
        return_from = request.form.get('return_from')
        return_to = request.form.get('return_to')
        from_code = fc.get_codes([fly_from])
        to_code = fc.get_codes(fly_to)
        # to update
        db.update_user(email=email, fly_from=from_code[0], fly_to=to_code, date_from=date_from,
                       date_to=date_to, return_from=return_from, return_to=return_to, price_to=price_to)
        # CANT SEND EMAIL THROUGH RENDER
        # body = "User information: \nEmail: " + email + " \nFly from: " + from_code[
        #     0] + " \nFly to: " + request.form.get('fly_to') + \
        #        "\nFor: " + request.form.get('price') + " \nDepart : " + date_from + " - " + date_to + "\nReturn : " + return_from + " - " + return_to
        # em.send_email(receiver=email, subject="FLIGHT CHECKER CONFIRMATION", body=body)
        return render_template("submitted.html")
    return render_template('edit-add.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        email = request.form.get('email')
        print(email)
        db.delete_user(email=email)
        return render_template('home.html')
    return render_template('delete.html')


if __name__ == '__main__':
    app.run(debug=False)
