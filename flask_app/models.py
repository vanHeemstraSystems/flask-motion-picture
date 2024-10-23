from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FilmProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)


class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    awards_won = db.Column(db.Integer, nullable=True)


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)


class Producer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)
    funding_secured = db.Column(db.Float, nullable=False)  # Amount of funding secured
    project_guidelines = db.Column(
        db.Text, nullable=True
    )  # High-level guidelines for the project


class ExecutiveProducer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)
    role_description = db.Column(
        db.Text, nullable=True
    )  # Description of responsibilities


class CastingDirector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class FirstAssistantDirector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)


class SecondAssistantDirector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class SecondSecondAssistantDirector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class SetPersonalAssistant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Gaffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Spark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class BestBoyElectric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Cinematographer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    style = db.Column(db.String(100), nullable=True)


class Editor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    software_proficient = db.Column(db.String(100), nullable=False)


class SoundDesigner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    projects_completed = db.Column(db.Integer, nullable=False)


class Animator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class SetDresser(db.Model):  # New model for Set Dresser
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class PropMaster(db.Model):  # New model for Prop Master
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)


class ArtPersonalAssistant(db.Model):  # New model for Art Personal Assistant
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)


class ArtDepartment(db.Model):  # New model for Art Department
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    production_designers = db.relationship(
        "ProductionDesigner", backref="art_department"
    )
    art_directors = db.relationship("ArtDirector", backref="art_department")
    set_dressers = db.relationship("SetDresser", backref="art_department")
    prop_masters = db.relationship("PropMaster", backref="art_department")
    art_personal_assistants = db.relationship(
        "ArtPersonalAssistant", backref="art_department"
    )


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)


class Scene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    time_of_day = db.Column(db.String(10), nullable=False)  # DAY or NIGHT
    scene_type = db.Column(db.String(10), nullable=False)  # INT or EXT
    scene_number = db.Column(db.Integer, nullable=False)  # Scene number
    has_cgi = db.Column(
        db.Boolean, default=False
    )  # Indicates if the scene includes CGI


class Storyboarder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class PrincipalCast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role_description = db.Column(db.Text, nullable=True)  # Description of the role


class SoundDesignBranch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sound_designer_id = db.Column(db.Integer, db.ForeignKey("sound_designer.id"))


class SoundDesignPullRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch_id = db.Column(db.Integer, db.ForeignKey("sound_design_branch.id"))
    reviewer_id = db.Column(db.Integer, db.ForeignKey("sound_designer.id"))
    status = db.Column(
        db.String(20), nullable=False
    )  # e.g., "Pending", "Approved", "Rejected"


class CGIAnimationBranch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch_name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    animator_id = db.Column(db.Integer, db.ForeignKey("animator.id"))


class CGIPullRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch_id = db.Column(db.Integer, db.ForeignKey("cgi_animation_branch.id"))
    reviewer_id = db.Column(db.Integer, db.ForeignKey("animator.id"))
    status = db.Column(
        db.String(20), nullable=False
    )  # e.g., "Pending", "Approved", "Rejected"


class AboveTheLineCrew(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)  # Role description
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    producer_id = db.Column(db.Integer, db.ForeignKey("producer.id"))
    executive_producer_id = db.Column(
        db.Integer, db.ForeignKey("executive_producer.id")
    )
    casting_director_id = db.Column(db.Integer, db.ForeignKey("casting_director.id"))
