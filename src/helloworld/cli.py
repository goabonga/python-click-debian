# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

"""Tiny click hello-world CLI.

Entry point exposed via the `helloworld` console script (declared in
``pyproject.toml``'s ``[project.scripts]``). The Debian package installs
this script under ``/usr/bin/helloworld`` thanks to ``dh-python`` +
``pybuild``.
"""

import click


@click.command()
@click.option("--name", default="world", show_default=True, help="Who to greet.")
def main(name: str) -> None:
    """Print a friendly greeting."""
    click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    main()
