import click

from {{ cookiecutter.project_slug }}.dynaconf.services.main import settings


@click.group()
@click.option(
    "--config",
    type=click.Choice(["default", "development", "production"], case_sensitive=False),
    default="default",
    show_default=True,
    help="Environment",
)
def main(config: str) -> None:
    """Console script for {{ cookiecutter.project_slug }}"""
    click.echo(f"Environment: {config}")
    settings.setenv(config)


@main.command()
def package_name() -> None:
    click.echo(f"Package Name: {settings.name}")


@main.command()
@click.argument("key", default="")
def database(key: str) -> None:
    if key:
        click.echo(f"{key.title()}: {settings.database[key]}")
    else:
        click.echo(f"Database: {settings.database}")


if __name__ == "__main__":
    main()
