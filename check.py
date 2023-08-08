import os
import smtplib
from database import Database
from flight_checker import FlightChecker

# # -----------------SUPABASE DATABASE-----------------#
db = Database()
all_users = db.get_all_users()

# # -----------------FLIGHT CHECK----------------- #

fc = FlightChecker()
all_flights = []
for user in all_users:
    user_account = db.get_user(user['email'])
    flights = fc.check_flight(user=user_account)
    all_flights.append(flights)

#
# # ------------SENDING EMAIL----------------#

EMAIL = 'searchflightsearch@gmail.com'
PASSWORD = os.environ.get('EMAIL_PASSWORD')
# connecting to email
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)

    for i in range(len(all_users)):
        # if the person has flights create and send message
        if all_flights[i]:
            email_message = 'Subject:FLIGHT DEAL\n\n '
            for j in range(len(all_flights[i])):
                email_message += all_flights[i][j]['cityFrom'] + ' -> ' + all_flights[i][j]['cityTo'] + ' for $' + str(all_flights[i][j]['price']) + '\n'
            connection.sendmail(from_addr=EMAIL, to_addrs=all_users[i]['email'], msg=email_message)





