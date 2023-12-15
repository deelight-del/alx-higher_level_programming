#!/usr/bin/python3
""" This module contains the ORM for objects
that contain only a"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import asc, create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(
        State.name == sys.argv[4]).first()
    if (result is None):
        print("Not found")
    else:
        print(result.id)
