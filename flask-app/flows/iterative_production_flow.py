from prefect import flow, task
from models import Director, Cinematographer, Gaffer, Actor, Scene, AssistantDirector, FirstAssistantDirector

@task
def filming_scene(director: Director, cinematographer: Cinematographer, gaffer: Gaffer, scene: Scene, actors: list):
    print(f"{director.name} is filming scene: {scene.description} at {scene.location.name} ({scene.scene_type}, {scene.time_of_day}).")
    print(f"{gaffer.name} is setting up the lighting for this scene.")
    for actor in actors:
        print(f"{actor.name} is performing in this scene.")

@task
def filming(director: Director, cinematographer: Cinematographer, gaffer: Gaffer, scenes: list, actors: list):
    for scene in scenes:
        filming_scene(director, cinematographer, gaffer, scene, actors)

@task
def daily_callsheets(ad: AssistantDirector, scenes: list, crew: list, actors: list):
    for scene in scenes:
        create_callsheet(ad, f"Day {scene.scene_number}", scene, crew, actors)

@flow
def iterative_production_flow(director: Director, cinematographer: Cinematographer, gaffer: Gaffer, scenes: list, actors: list, ad: AssistantDirector, crew: list):
    filming(director, cinematographer, gaffer, scenes, actors)
    daily_callsheets(ad, scenes, crew, actors)
