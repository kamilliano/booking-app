#/usr/bin/python

from Bookings import create_app
import os

app = create_app(os.getenv('WEBOOKMARKS_ENV') or 'dev')

if __name__ == '__main__':
    app.run()

