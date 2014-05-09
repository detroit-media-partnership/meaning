from sqlalchemy import create_engine, exc, event
from sqlalchemy.pool import Pool
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import db_uri

engine = create_engine(db_uri.DB_URI, pool_recycle=3600, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
					autoflush=True,
					bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	import models
	Base.metadata.create_all(bind=engine)

@event.listens_for(Pool, "checkout")
def ping_connection(dbapi_connection, connection_record, connection_proxy):
	cursor = dbapi_connection.cursor()
	try:
		cursor.execute("SELECT 1")
	except:
		raise exc.DisconnectionError()
	cursor.close()
