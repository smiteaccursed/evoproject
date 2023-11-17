from subprocess import run
import os

def run_all():
    e2e_policy_path = os.path.abspath("files/e2e_policy.py")
    e2e_forum_path = os.path.abspath("files/e2e_forum.py")

    run(["python", "-m", "unittest", e2e_policy_path])
    run(["python", "-m", "unittest", e2e_forum_path])
if __name__ == "__main__":
    
    run_all()