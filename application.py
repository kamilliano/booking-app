#!/usr/bin/env python

from Bookings import create_app
import os

app = create_app(os.getenv('BOOKINGS_ENV') or 'dev')

if __name__ == '__main__':
    app.run()

