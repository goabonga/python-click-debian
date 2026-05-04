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


def test_french_translation(monkeypatch) -> None:
    """When LANGUAGE=fr, the greeting comes from the French catalogue."""
    monkeypatch.setenv("LANGUAGE", "fr")
    monkeypatch.setenv("LC_ALL", "fr_FR.UTF-8")
    result = CliRunner().invoke(main, ["--name", "Alice"])
    assert result.exit_code == 0
    assert "Bonjour, Alice !" in result.output


def test_spanish_translation(monkeypatch) -> None:
    """When LANGUAGE=es, the greeting comes from the Spanish catalogue."""
    monkeypatch.setenv("LANGUAGE", "es")
    monkeypatch.setenv("LC_ALL", "es_ES.UTF-8")
    result = CliRunner().invoke(main, ["--name", "Alice"])
    assert result.exit_code == 0
    assert "¡Hola, Alice!" in result.output


def test_fallback_to_english_when_unknown_locale(monkeypatch) -> None:
    """A locale we don't ship (e.g. zz) falls back to the source msgid."""
    monkeypatch.setenv("LANGUAGE", "zz")
    monkeypatch.setenv("LC_ALL", "C")
    result = CliRunner().invoke(main)
    assert result.exit_code == 0
    assert result.output.strip() == "Hello, world!"
