Say owner has many pets
We will make a relationship for this

Class Owner(Base):
    id, name, address
    -> comes in the relationship
    pets = relationship('Pet', backref='owner')
    -> this basically means Owner makes a dummy connected column in Pet

Class Pet(Base):
    id, name, age
    --> NOW a 4th attribute/column with the foreign key to relate to Owner
    owner_id = ForeignKey(owner.id)

++Now to the cmdline++
anthony = Owner('Anthony', '123-Sunnydrive')
    -->add and commit anthony
    -->now to anthony's pet max
max = Pet('Max', 7, owner=anthony)
    -->the relationship at the end would populate the pet table but it would
        be recorded as owner_id on Pet table
buddy = Pet('Buddy', 8, owner=anthony)

++accurate commands from our table using our relationship would be++
anthony.pets would return an object list for anthony's pets
