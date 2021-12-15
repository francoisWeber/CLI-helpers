#! /opt/homebrew/bin/python3
import click
import os
from subprocess import run


@click.command()
@click.argument(
    "path", type=click.Path(resolve_path=True), required=False, default=None
)
def cli(path):
    path_or_dir = os.getcwd()
    if path is not None:
        path_or_dir = os.path.join(path_or_dir, path)
    run("pbcopy", universal_newlines=True, input=path_or_dir)


if __name__ == "__main__":
    cli()
