import re

from email.utils import parseaddr

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

USERNAME_REGEX = r'^[^\W_](?:[^\W_]|-(?=[^\W_])){0,38}$'

project_slug = "{{ cookiecutter.project_slug }}"
email = "{{ cookiecutter.email }}"
github_username = "{{ cookiecutter.github_username }}"

if hasattr(project_slug, "isidentifier"):
    assert (
        project_slug.isidentifier()
    ), f"'{project_slug}' project slug is not a valid Python identifier"

assert (
    project_slug == project_slug.lower()
), f"'{project_slug}' project slug should be all lowercase"

assert (
    '@' in parseaddr(email)[1]
), f"'{email}' is not a vaild email"

assert (
    re.match(USERNAME_REGEX, github_username)
), f"'{github_username}' is not a valid username"
