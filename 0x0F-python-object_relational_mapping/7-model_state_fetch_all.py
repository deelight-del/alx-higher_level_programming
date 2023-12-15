#!/usr/bin/python3
""" This module contains the use of session to
lay a handle on our given ORM"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine, asc
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # This creates tables for all Bass subclass
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(asc(State.id))
    for obj in result:
        print(str(obj.id) + ":",  obj.name)
    # query accepts the exact class/table to query upon
