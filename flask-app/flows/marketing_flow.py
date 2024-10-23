from prefect import flow, task
from models import Producer, Director, Actor

@task
def create_promotional_materials(producer: Producer, director: Director):
    print(f"{producer.name} and {director.name} are creating promotional materials.")

@task
def publicity(producer: Producer, director: Director, actors: list):
    print(f"{producer.name} is managing publicity, with {director.name} and the actors attending events.")

@flow
def marketing_flow(producer: Producer, director: Director, actors: list):
    create_promotional_materials(producer, director)
    publicity(producer, director, actors)
