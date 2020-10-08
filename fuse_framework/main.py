import os
import subprocess

from cookiecutter.main import cookiecutter


def init():
    path = cookiecutter("gh:sp-fm/fuse-framework")
    os.chdir(path)
    subprocess.run(["git", "init"])
    subprocess.run(["pip", "install", "poetry", "--upgrade", "--pre"])
    subprocess.run(["poetry", "install"])
    subprocess.run(["poetry", "run", "pre-commit", "install"])
