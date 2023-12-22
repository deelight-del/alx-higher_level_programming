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
    state_objects = session.query(State).join(City).order_by(
        asc(State.id)
            ).order_by(asc(City.id)).all()
    for eachState in state_objects:
        print(str(eachState.id) + ": " + eachState.name)
        cities = eachState.cities
        for eachCity in cities:
            print("\t{}".format(eachCity.id) + ": " + eachCity.name)
