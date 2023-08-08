import os
from supabase import create_client, Client


class Database():
    def __init__(self):
        # url = os.environ.get("SUPABASE_URL")
        # key = os.environ.get("SUPABASE_KEY")
        self.url = 'https://rbwjjqmomnzcvdygfcgo.supabase.co'

        self.key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJid2pqcW1vbW56Y3ZkeWdmY2dvIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTE0MjM3MjUsImV4cCI6MjAwNjk5OTcyNX0.Q_cnirVEDXDn75m9SPvJIuCw7wdbL5NrGiDf9lhX0nI'
        self.supabase: Client = create_client(self.url, self.key)

    def get_user(self, email):
        response = self.supabase.table('users').select("*").eq('email', email).execute()
        # why is it empty
        return response.data[0]

    def add_user(self, email, fly_from, fly_to, date_from, date_to, return_from, return_to, price_to):
        self.supabase.table('users').insert(
            {'email': email, "fly_from": fly_from, "fly_to": fly_to, "date_from": date_from, "date_to": date_to,
             "return_from": return_from, "return_to": return_to, "price_to": price_to}).execute()
        # TODO: ADD USER DOES NOT WORK
