How do you mean?
================

http://meaning.detroitmedia.net

Meaning is a web application to illustrate how differently people
define words or phrases.

Meaning will present a user with multiple phrases and on a scale 
between 0 to 100, the user is asked to input the number they think represents 
that phrase.

db\_uri.py contains the database connection string that hooks into SQLAlchemy
e.g. for mysql:
    
    DB_URI = "mysql://user:pass@localhost/db"

In the meaning directory:

    $ pip install -r requirements.txt
    $ python
    >>> from database import init_db
    >>> init_db()
    >>> exit()
