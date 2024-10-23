from flask import Flask

# from flows import (
#     iterative_cgi_flow,
#     iterative_sound_design_flow,
#     collaborative_pre_production_flow,
#     iterative_production_flow,
#     feedback_post_production_flow,
#     marketing_flow,
#     distribution_flow,
#     screening_flow,
# )
from models import (
    Writer,
    Director,
    Producer,
    Actor,
    Cinematographer,
    Editor,
    SoundDesigner,
    Animator,
    Location,
    Scene,
    Storyboarder,
    FirstAssistantDirector,
    SecondAssistantDirector,
    SecondSecondAssistantDirector,
    Gaffer,
    ExecutiveProducer,
    CastingDirector,
    PrincipalCast,
    AboveTheLineCrew,
    AssistantDirectorsDepartment,
    SetDresser,
    PropMaster,
    ArtPersonalAssistant,
    ArtDepartment,
    ProductionDesigner,
)

app = Flask(__name__)


@app.route("/")
def main():
    return "Main Page"


@app.route("/run_flows", methods=["GET", "POST"])  # Should be POST only
def run_flows():
    # Create participant instances using actual names
    writer = Writer(name="Truman Capote", experience_years=10)
    # sound_designer = SoundDesigner(name="Morris D. Duss", projects_completed=30)
    # reviewer_sound = SoundDesigner(name="John Smith", projects_completed=10)  # Example reviewer for sound
    # animator = Animator(name="Alice Johnson")  # Example animator
    # reviewer_cgi = Animator(name="Bob Brown")  # Example reviewer for CGI
    # director = Director(name="Blake Edwards", awards_won=2)
    # producer = Producer(name="Richard Shepherd", projects_managed=5, funding_secured=500000, project_guidelines="Ensure high-quality production.")
    # executive_producer = ExecutiveProducer(name="Sarah Connor", experience_years=15, role_description="Oversees production and funding.")
    # casting_director = CastingDirector(name="Emily Davis")  # Example casting director
    # principal_cast = PrincipalCast(name="Main Cast")  # Example principal cast
    # art_personal_assistant = ArtPersonalAssistant(name="Chris Blue", experience_years=3)  # Example Art Personal Assistant
    art_department = ArtDepartment(name="Art Department")  # New Art Department
    production_designer = ProductionDesigner(
        name="Tom Hanks",
        experience_years=20,
        design_philosophy="Create immersive environments that enhance storytelling.",
    )  # Example Production Designer
    # storyboarder = Storyboarder(name="John Doe")  # Example storyboarder
    # ad = FirstAssistantDirector(name="Tom Brown", experience_years=5)  # Example 1st Assistant Director
    # second_ad = SecondAssistantDirector(name="Lisa White", experience_years=3)  # Example 2nd Assistant Director
    # second_second_ad = SecondSecondAssistantDirector(name="Mike Green", experience_years=2)  # Example 2nd 2nd Assistant Director
    # gaffer = Gaffer(name="Mark Lee")  # Example gaffer
    # crew = ["Cinematographer", "Sound Designer", "Production Assistant"]
    # actors = [
    #     Actor(name="Audrey Hepburn", role="Holly Golightly", experience_years=20),
    #     Actor(name="George Peppard", role="Paul Varjak", experience_years=15)
    # ]
    # cinematographer = Cinematographer(name="Charles Lang", style="Classic")
    # editor = Editor(name="Samuel E. Beetley", software_proficient="Film Editing")

    # Create location instances
    # locations = [
    #     Location(name="Tiffany & Co.", description="Iconic jewelry store on Fifth Avenue."),
    #     Location(name="Upper East Side Apartment", description="Holly Golightly's apartment."),
    #     Location(name="Central Park", description="Various scenes filmed in this famous park."),
    #     Location(name="The 21 Club", description="A famous restaurant where key scenes take place."),
    # ]

    # Create scene instances
    # scenes = [
    #     Scene(description="Holly arrives at Tiffany's", location=locations[0], time_of_day="DAY", scene_type="EXT", scene_number=1, has_cgi=True),
    #     Scene(description="Holly's apartment", location=locations[1], time_of_day="NIGHT", scene_type="INT", scene_number=2, has_cgi=False),
    #     Scene(description="Central Park meeting", location=locations[2], time_of_day="DAY", scene_type="EXT", scene_number=3, has_cgi=True),
    #     Scene(description="Dinner at The 21 Club", location=locations[3], time_of_day="NIGHT", scene_type="INT", scene_number=4, has_cgi=False),
    # ]

    # Trigger each flow
    # iterative_cgi_flow(animator, reviewer_cgi, "Initial CGI Design", "Added new visual effects.")
    # iterative_sound_design_flow(sound_designer, reviewer_sound, "Initial Sound Design", "Added new sound effects and ambiance.")
    # collaborative_pre_production_flow(director, producer, casting_director, principal_cast, art_personal_assistant, actors, locations, storyboarder, scenes)
    # iterative_production_flow(director, cinematographer, gaffer, scenes, actors, ad, crew)
    # feedback_post_production_flow(editor, director, scenes)
    # marketing_flow(producer, director, actors)
    # distribution_flow(producer)
    # screening_flow(producer, director, actors)

    return "Flows executed successfully!"


if __name__ == "__main__":
    app.run(debug=True)
