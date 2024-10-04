from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to your database
engine = create_engine('sqlite:///mydatabase.db')
Base = declarative_base() 

# Define your model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Create the table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
new_user = User(name='John', email='john@example.com')
session.add(new_user)
session.commit() 