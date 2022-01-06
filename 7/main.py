from sqlalchemy import insert,select,and_,or_

from models import User, Base
from db import engine, Base

Base.metadata.create_all(engine)

def insert_one_user():
    stmt = insert(User).values(
        name = 'Johnny',
        fullname = 'John Carter',
        gender = 'male',
        age = '37'
    )
    with engine.connect() as conn:
        conn.execute(stmt)
# insert_one_user()
def insert_many_users(values):
    stmt = insert(User)
    with engine.connect() as conn:  
        conn.execute(stmt, values)
values =    [
    {'name' : 'Anna', 'fullname' : 'Anna Karelina', 'gender' : 'female', 'age' : '38' },
    {'name' : 'Guido', 'fullname' : 'Guido van Rossu', 'gender' : 'male', 'age' : '35'},
    { 'name' : 'Leonard', 'fullname' : 'Leonard Hofstader', 'gender' : 'male', 'age' : '35'},
    { 'name' : 'Amy', 'fullname' : 'Amy Farafowler', 'gender' : 'female', 'age' : '32'},
    { 'name' : 'Sheldon', 'fullname' : 'Sheldon Cooper', 'gender' : 'male', 'age' : '34'},
    { 'name' : 'Howard', 'fullname' : 'Hovard Volovets', 'gender' : 'male', 'age' : '33'},
    { 'name' : 'Radjesh', 'fullname' : 'Radjesh Cutropalli', 'gender' : 'male', 'age' : '32'},
]
# insert_many_users(values)
def select_users():
    stmt = (
        select(User)
            .where(User.gender == 'male')
            .filter(User.name.like('L%') | User.name.like('H%'))
            .order_by(User.age.desc())
            .limit(3)
    )
    with engine.connect() as conn:
        return list(conn.execute(stmt))

for row in select_users():
    print(f"{row.name} fullname: {row.fullname} age = {row.age} gender = {row.gender}")


