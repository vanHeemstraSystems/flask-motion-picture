from prefect import flow, task
from models import Producer

@task
def secure_distribution_deals(producer: Producer):
    print(f"{producer.name} is securing distribution deals.")

@task
def schedule_release_dates(producer: Producer):
    print(f"{producer.name} is scheduling release dates.")

@flow
def distribution_flow(producer: Producer):
    secure_distribution_deals(producer)
    schedule_release_dates(producer)
