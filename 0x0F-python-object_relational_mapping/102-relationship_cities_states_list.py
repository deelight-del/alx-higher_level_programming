#!/usr/bin/python3
"""Module to explore the relationship between cities and State"""


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine, asc
    from relationship_city import Base, City
    from relationship_state import State
    import sys

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    city_objects = session.query(City).join(State).order_by(
        asc(City.id)
            ).all()
    for eachCity in city_objects:
        state = eachCity.state
        print("{}: {} -> {}".format(
            eachCity.id, eachCity.name,
            state.name
            )
        )
