#!/usr/bin/python3
"""Script that prints all City objects from database"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    import sys

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    cities_result = session.query(City).order_by(City.id).all()
    for row in cities_result:
        state = session.query(State).filter(
            State.id == row.state_id
                ).one()
        print(state.name + ": " + "(" + str(row.id) + ") " + row.name)
