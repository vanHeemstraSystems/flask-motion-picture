from prefect import flow, task
from models import Producer, Director, Actor


@task
def premiere_film(producer: Producer, director: Director, actors: list):
    print(
        f"{producer.name} is organizing the premiere with {director.name} and the actors."
    )


@task
def general_release(producer: Producer):
    print(f"{producer.name} is ensuring the film is released to theaters.")


@flow
def screening_flow(producer: Producer, director: Director, actors: list):
    premiere_film(producer, director, actors)
    general_release(producer)
