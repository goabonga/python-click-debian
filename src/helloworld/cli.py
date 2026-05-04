# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

"""Tiny click hello-world CLI.

Entry point exposed via the `helloworld` console script (declared in
``pyproject.toml``'s ``[project.scripts]``). The Debian package installs
this script under ``/usr/bin/helloworld`` thanks to ``dh-python`` +
``pybuild``.

Internationalised via gettext: the greeting is translated based on the
runtime ``$LANGUAGE`` / ``$LC_ALL`` / ``$LANG`` environment, with
catalogues shipped under ``helloworld/locale/<lang>/LC_MESSAGES/`` (so
both ``pip install`` and ``apt install`` find them transparently).
"""

import gettext
from pathlib import Path

import click

DOMAIN = "helloworld"
_LOCALE_DIR = Path(__file__).parent / "locale"


def _translate(msgid: str) -> str:
    """Resolve `msgid` in the current locale.

    Looked up at call time (not module load) so a process can react to
    runtime locale changes — and so tests can monkey-patch
    ``$LANGUAGE`` between invocations.
    """
    return gettext.translation(
        DOMAIN, localedir=str(_LOCALE_DIR), fallback=True
    ).gettext(msgid)


@click.command()
@click.option(
    "--name",
    default="world",
    show_default=True,
    help="Who to greet.",
)
def main(name: str) -> None:
    """Print a friendly greeting (translated based on $LANG)."""
    click.echo(_translate("Hello, %(name)s!") % {"name": name})


if __name__ == "__main__":
    main()
