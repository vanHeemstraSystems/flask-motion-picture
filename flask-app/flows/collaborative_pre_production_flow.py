from prefect import flow, task
from models import Director, Producer, Actor, Location, Storyboarder, Scene, CastingDirector, PrincipalCast, PropMaster, ArtPersonalAssistant, ArtDepartment

@task
def casting(casting_director: CastingDirector, principal_cast: PrincipalCast, actors: list):
    for actor in actors:
        print(f"{casting_director.name} is casting {actor.name} for the role of {actor.role}.")
        principal_cast.actors.append(actor)  # Associate actor with principal cast

@task
def crew_assembly(director: Director, producer: Producer):
    print(f"{director.name} and {producer.name} are assembling the crew.")

@task
def location_scouting(director: Director, producer: Producer, locations: list):
    for location in locations:
        print(f"{director.name} and {producer.name} are scouting {location.name}: {location.description}.")

@task
def storyboarding(storyboarder: Storyboarder, scenes: list):
    for scene in scenes:
        print(f"{storyboarder.name} is storyboarding scene: {scene.description}.")

@task
def arrange_art(art_personal_assistant: ArtPersonalAssistant, scenes: list):
    for scene in scenes:
        print(f"{art_personal_assistant.name} is arranging art elements for scene: {scene.description}.")

@flow
def collaborative_pre_production_flow(director: Director, producer: Producer, casting_director: CastingDirector, principal_cast: PrincipalCast, art_personal_assistant: ArtPersonalAssistant, actors: list, locations: list, storyboarder: Storyboarder, scenes: list):
    casting(casting_director, principal_cast, actors)
    crew_assembly(director, producer)
    location_scouting(director, producer, locations)
    storyboarding(storyboarder, scenes)
    arrange_art(art_personal_assistant, scenes)

