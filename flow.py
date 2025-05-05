import os

from prefect import flow
from prefect.runner.storage import GitRepository

@flow(log_prints=True)
def my_flow():
    print("Hello again, world!")

if __name__ == "__main__":
    my_flow.from_source(
        source=GitRepository(
            repo_url="https://github.com/<your-org>/<your-repo>.git",
            commit_sha=os.environ["GITHUB_SHA"],
        )
    ).deploy(
        name="my-deployment",
        version="0.0.1",
        work_pool_name="my-work-pool",
    )
