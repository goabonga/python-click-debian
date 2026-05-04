# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>

from click.testing import CliRunner

from helloworld.cli import main


def test_default_greeting() -> None:
    result = CliRunner().invoke(main)
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, world!"


def test_named_greeting() -> None:
    result = CliRunner().invoke(main, ["--name", "alice"])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, alice!"


def test_help_includes_option() -> None:
    result = CliRunner().invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "--name" in result.output
    assert "Who to greet" in result.output
