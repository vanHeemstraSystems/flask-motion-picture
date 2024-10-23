from prefect import flow, task
from models import Director, Producer, Actor, Location, Storyboarder, Scene, CastingDirector, PrincipalCast, AboveTheLineCrew, AssistantDirectorsDepartment

@task
def casting(casting_director: CastingDirector, principal_cast: PrincipalCast, actors: list):
    for actor in actors:
        print(f"{casting_director.name} is casting {actor.name} for the role of {actor.role}.")
        principal_cast.actors.append(actor)  # Associate actor with principal cast

@task
def crew_assembly(director: Director, producer: Producer, ad_department: AssistantDirectorsDepartment):
    print(f"{director.name} and {producer.name} are assembling the crew.")
    print(f"Assistant Directors Department includes: {', '.join([ad.name for ad in ad_department.first_assistant_directors])}, {', '.join([ad.name for ad in ad_department.second_assistant_directors])}, {', '.join([ad.name for ad in ad_department.second_second_assistants])}, {', '.join([ad.name for ad in ad_department.set_personal_assistants])}")

@task
def location_scouting(director: Director, producer: Producer, locations: list):
    for location in locations:
        print(f"{director.name} and {producer.name} are scouting {location.name}: {location.description}.")

@task
def storyboarding(storyboarder: Storyboarder, scenes: list):
    for scene in scenes:
        print(f"{storyboarder.name} is storyboarding scene: {scene.description}.")

@flow
def collaborative_pre_production_flow(director: Director, producer: Producer, casting_director: CastingDirector, principal_cast: PrincipalCast, ad_department: AssistantDirectorsDepartment, actors: list, locations: list, storyboarder: Storyboarder, scenes: list):
    casting(casting_director, principal_cast, actors)
    crew_assembly(director, producer, ad_department)
    location_scouting(director, producer, locations)
    storyboarding(storyboarder, scenes)
