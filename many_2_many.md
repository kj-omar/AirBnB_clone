We want to create a many to many relationship
EG channels and users
   a user can subscribe to many channels and a channel can have many users

class User(Base):
    id, name

class Channel(Base):
    id, name
