from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker


dbpath = "test.db"
engine = create_engine('sqlite:///%s' %dbpath)
metadata = MetaData(bind=engine)

people = Table('people', metadata, Column('id', Integer, primary_key=True),\
         Column('name', String), Column('count', Integer))

Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

people_ins = people.insert().values(name="umar", count=1)
print(people_ins)
session.execute(people_ins)
session.commit()

result = session.execute(select([people]).where(people.c.name =="umar"))
for row in result:
    print(row)


