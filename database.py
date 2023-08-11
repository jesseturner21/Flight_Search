import os
from supabase import create_client, Client


class Database:
    def __init__(self):
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.supabase: Client = create_client(self.url, self.key)

    def get_user(self, email):
        response = self.supabase.table('users').select("*").eq('email', email).execute()
        # why is it empty
        return response.data[0]

    def get_all_users(self):
        response = self.supabase.table('users').select("email").execute()
        return response.data

    def add_user(self, email, fly_from, fly_to, date_from, date_to, return_from, return_to, price_to):
        self.supabase.table('users').insert(
            {'email': email, "fly_from": fly_from, "fly_to": fly_to, "date_from": date_from, "date_to": date_to,
             "return_from ": return_from, "return_to": return_to, "price_to": price_to}).execute()

    def update_user(self, email, fly_from, fly_to, date_from, date_to, return_from, return_to, price_to):
        self.supabase.table('users').update(
            {'email': email, "fly_from": fly_from, "fly_to": fly_to, "date_from": date_from, "date_to": date_to,
             "return_from ": return_from, "return_to": return_to, "price_to": price_to}).eq('email', email).execute()

    def delete_user(self, email):
        self.supabase.table('users').delete().eq('email', email).execute()