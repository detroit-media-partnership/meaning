How do you mean?
================

http://meaning.detroitmedia.net

Meaning is a web application to illustrate how differently people
define words or phrases. It can be used for workshops, presentations 
and brainstorms as a way to engage participants and generate discussion.

Meaning will present a user with multiple words and phrases. On a scale 
between 0 to 100, the user is asked to input the number 
they think represents the proportion of time or frequency conveyed by 
that word or phrase.

For example, among a group of people the word "most of the time" might 
equate to a range of definitions from 25% of the time to 75% of the time. 
(You'll be surprised.)

You can view the results after everyone has entered numbers for each word. 
Meaning shows the low, the high and the average of all entries 
for each word and phrase.

You can use the results to begin a discussion about how even though 
we use these words daily, the same word might have very different 
meaning to someone else.

HOW TO DEVELOP
--------------

This app was built using:

*  [Python 2.6](https://www.python.org/download/releases/2.6), 
*  [Flask](http://flask.pocoo.org), 
*  [SQLAlchemy](http://www.sqlalchemy.org), and 
*  [MySQL](http://www.mysql.com)

MySQL Dependencies (Debian):

    $ sudo apt-get install mysql-server libmysqlclient-dev

settings.py
-----------

This file needs to be created for database of choice.
settings.py contains the database connection 
string that hooks into SQLAlchemy e.g. for mysql 
(meaning/settings.py):
    
    DB_URI = "mysql+mysqldb://user:pass@localhost/db"
    # DB_URI = "dialect[+driver]://user:password@hostname/dbname"

We are using mysql but any SQL database that 
SQLAlchemy supports should work.

settings.py also contains the Flask configuration settings:

    DEBUG = False
    SECRET_KEY = 'somekey'

In the meaning directory:

    $ pip install -r requirements.txt
    $ python
    >>> from database import init_db
    >>> init_db()
    >>> exit()
