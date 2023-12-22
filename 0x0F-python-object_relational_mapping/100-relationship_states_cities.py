#!/usr/bin/python3
"""Module to explore the relationship between cities and State"""


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
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
    new_state = State(name="California")
    san_fran = City(name="San Francisco")
    new_state.cities.append(san_fran)
    session.add(new_state)
    session.commit()
