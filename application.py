#!/usr/bin/env python

from Bookings import create_app, db
import os
import click
from flask_migrate import Migrate, MigrateCommand
from models import User
from sqlalchemy import exc
from flask_migrate import Migrate, MigrateCommand
app = create_app(os.getenv('BOOKINGS_ENV') or 'dev')


migrate = Migrate(app, db)

@app.cli.command()
def insert_test_users():
    """insert test users 
    
    Args:
        
    Throws:
        
    """
    
    click.echo("Adding users to the tables")
    
    try:
        
        user = User(username='test123', email='test@test123')

        db.session.add(user)
        
        click.echo("Data has been loaded to database")

    except IOError as e:
        click.echo("error has occured reading file: " + str(e))
    except exc.SQLAlchemyError as e:
        click.echo("error has occured loading data to sql storage: " + str(e))
    #only commit if no errors occured - TODO investigate
    db.session.commit()

app.cli.command()
@click.option('--response', prompt=('Are you sure you want '
                                        'to delete all the data? Type "y" for "n" to quit.'))    
def dropdb(response):
    """Drops the App database if admin types 'y'
    """
    try:
        if response.lower() == "n":
            return
        else:
            while True:
                input_value = input('Type "y" for "n" to quit: ').lower()
                if input_value == 'y':
                    db.drop_all()
                    click.echo("Dropped the database")
                elif input_value == 'n':
                    return
                
    except ValueError as e:
        click.echo("Input value error: " + str(e))

#dummy 2 with parameter
@app.cli.command()
def hello_app():
    click.echo('Hello!')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8080)

