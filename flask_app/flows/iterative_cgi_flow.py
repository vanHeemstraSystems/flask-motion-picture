from prefect import flow, task
from models import Animator, CGIAnimationBranch, CGIPullRequest


@task
def test(animator: Animator, branch_name: str):
    print("Iterative CGI: Test.")
    # return CGIAnimationBranch(
    #     branch_name=branch_name, content="Test", animator_id=animator.id
    # )

# @task
# def create_cgi_branch(animator: Animator, branch_name: str):
#     print(f"{animator.name} created a new CGI branch: {branch_name}.")
#     return CGIAnimationBranch(
#         branch_name=branch_name, content="Initial CGI content", animator_id=animator.id
#     )


# @task
# def make_cgi_changes(branch: CGIAnimationBranch, new_content: str):
#     branch.content += f"\n{new_content}"
#     print(f"Changes made to CGI branch {branch.branch_name}: {new_content}")


# @task
# def submit_cgi_pull_request(branch: CGIAnimationBranch, reviewer: Animator):
#     print(
#         f"Pull request submitted for CGI branch {branch.branch_name} to {reviewer.name}."
#     )
#     return CGIPullRequest(
#         branch_id=branch.id, reviewer_id=reviewer.id, status="Pending"
#     )


# @task
# def review_cgi_pull_request(pull_request: CGIPullRequest):
#     pull_request.status = "Approved"
#     print(f"Pull request {pull_request.id} has been approved.")


# @task
# def merge_cgi_to_main(branch: CGIAnimationBranch):
#     print(f"CGI branch {branch.branch_name} has been merged into the main branch.")


@flow
def iterative_cgi_flow(
    animator: Animator, reviewer: Animator, branch_name: str, new_content: str
):
    test(animator, branch_name)
    # branch = create_cgi_branch(animator, branch_name)
    # make_cgi_changes(branch, new_content)
    # pull_request = submit_cgi_pull_request(branch, reviewer)
    # review_cgi_pull_request(pull_request)
    # merge_cgi_to_main(branch)
