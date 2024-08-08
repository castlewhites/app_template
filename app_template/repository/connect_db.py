from sqlmodel import create_engine

def connect():
    engine = create_engine()
    return engine