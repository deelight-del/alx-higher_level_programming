#!/usr/bin/python3
""" This module will be used to print the first instance
of an ORM object"""

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
    result = session.query(State).first()
    if result is not None:
        print(str(result.id) + ":", result.name)
    else:
        print()
