from prefect import flow, task
from models import SoundDesigner, SoundDesignBranch, SoundDesignPullRequest

@task
def create_sound_design_branch(sound_designer: SoundDesigner, branch_name: str):
    print(f"{sound_designer.name} created a new sound design branch: {branch_name}.")
    return SoundDesignBranch(branch_name=branch_name, content="Initial sound design content", sound_designer_id=sound_designer.id)

@task
def make_sound_design_changes(branch: SoundDesignBranch, new_content: str):
    branch.content += f"\n{new_content}"
    print(f"Changes made to sound design branch {branch.branch_name}: {new_content}")

@task
def submit_sound_design_pull_request(branch: SoundDesignBranch, reviewer: SoundDesigner):
    print(f"Pull request submitted for sound design branch {branch.branch_name} to {reviewer.name}.")
    return SoundDesignPullRequest(branch_id=branch.id, reviewer_id=reviewer.id, status="Pending")

@task
def review_sound_design_pull_request(pull_request: SoundDesignPullRequest):
    pull_request.status = "Approved"
    print(f"Pull request {pull_request.id} has been approved.")

@task
def merge_sound_design_to_main(branch: SoundDesignBranch):
    print(f"Sound design branch {branch.branch_name} has been merged into the main branch.")

@flow
def iterative_sound_design_flow(sound_designer: SoundDesigner, reviewer: SoundDesigner, branch_name: str, new_content: str):
    branch = create_sound_design_branch(sound_designer, branch_name)
    make_sound_design_changes(branch, new_content)
    pull_request = submit_sound_design_pull_request(branch, reviewer)
    review_sound_design_pull_request(pull_request)
    merge_sound_design_to_main(branch)
