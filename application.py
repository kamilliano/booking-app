#!/usr/bin/env python

from Bookings import create_app, db
import os
import click
from flask_migrate import Migrate, MigrateCommand
from Bookings.config import Config
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
app = create_app(os.getenv('BOOKINGS_ENV') or 'dev')

from models import User
migrate = Migrate(app, db)



@app.cli.command()
@click.option('--env_db', required=True)
def create_databases(env_db):
    """Create databases for the application based on environment

        Args: 
            ["dev_db", "test_db", "prod_db"]
    """

    try:
        conn = Config.MYSQL_CONN
        db_name = Config.dbs[env_db]
        db = SQLAlchemy()
        engine = db.create_engine(conn) # connect to server
        engine.execute("CREATE DATABASE " + db_name) #create db
        engine.execute("USE " + db_name ) # select new db
        print("DB created {}".format(db_name))
    except exc.SQLAlchemyError as e:
        click.echo("error has occured loading data to sql storage: " + str(e))
    except:
        print('Usage: Flask --env_db [env_db]')
        print('Possible "env_db" types: ["dev_db", "test_db", "prod_db"]')

    


   


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

