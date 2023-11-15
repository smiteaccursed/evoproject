from subprocess import run

def run_all():
    run(["python", "-m", "unittest", "files/e2e_policy.py"])
    run(["python", "-m", "unittest", "files/e2e_forum.py"])

if __name__ == "__main__":
    run_all()