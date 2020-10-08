import os
import subprocess

from cookiecutter.main import cookiecutter


def init():
    path = cookiecutter(".")
    os.chdir(path)
    subprocess.run(["git", "init"])
    subprocess.run(["poetry", "install"])
    subprocess.run(["poetry", "run", "pre-commit", "install"])
