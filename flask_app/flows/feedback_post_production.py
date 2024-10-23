from prefect import flow, task
from models import Editor, Director, Scene


@task
def editing_scene(editor: Editor, director: Director, scene: Scene):
    print(f"{editor.name} is editing scene: {scene.description}.")


@task
def feedback_session():
    print("Conducting feedback session on the edited scenes.")


@flow
def feedback_post_production_flow(editor: Editor, director: Director, scenes: list):
    for scene in scenes:
        editing_scene(editor, director, scene)
    feedback_session()
