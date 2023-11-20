from subprocess import run
import os
from threading import Timer
from logging import getLogger

logger = getLogger(__name__)
def run_all():
    e2e_policy_path = os.path.abspath("files/e2e_policy.py")
    e2e_forum_path = os.path.abspath("files/e2e_forum.py")

    run(["python", "-m", "unittest", e2e_policy_path])
    run(["python", "-m", "unittest", e2e_forum_path])
if __name__ == "__main__":
    logger.info("Tests will run after 10 seconds")
    tim = Timer(15, run_all) #wait 15 seconds to start after all services
    tim.start()