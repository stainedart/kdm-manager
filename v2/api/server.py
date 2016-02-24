#!/usr/bin/env python

from eve import Eve
from eve.auth import BasicAuth

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == 'admin' and password == 'Fby1XyweBNR6g'

def run():
    app = Eve(auth=MyBasicAuth)
    app.run()

if __name__ == '__main__':
    run()
