"""Tests for scripts/gen_models/gen_sqla.py CLI behavior."""

from __future__ import annotations

import sys

from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / 'scripts' / 'gen_models'
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import gen_sqla


def test_dry_run_prints_output_and_writes_no_file(
    monkeypatch, capsys, tmp_path
) -> None:
    """Ensure --dry-run prints code and skips writes/ruff."""
    default_output = tmp_path / 'default' / 'fhirx.py'
    monkeypatch.setattr(gen_sqla, 'OUTPUT_PATH', default_output)
    monkeypatch.setattr(gen_sqla, 'iter_pydantic_models', lambda: {})
    monkeypatch.setattr(
        gen_sqla, 'build_orm_file', lambda _models: 'GEN_CODE\n'
    )

    called = {'ruff': False}

    def fake_ruff(_path, *, fix: bool = True) -> None:
        called['ruff'] = True

    monkeypatch.setattr(gen_sqla, 'run_ruff', fake_ruff)

    exit_code = gen_sqla.main(['--dry-run'])

    out = capsys.readouterr()
    assert exit_code == 0
    assert out.out == 'GEN_CODE\n'
    assert out.err == ''
    assert not default_output.exists()
    assert called['ruff'] is False


def test_output_writes_to_custom_path(monkeypatch, tmp_path, capsys) -> None:
    """Ensure --output writes file to custom destination and runs Ruff."""
    custom_output = tmp_path / 'custom' / 'models.py'
    monkeypatch.setattr(gen_sqla, 'iter_pydantic_models', lambda: {})
    monkeypatch.setattr(gen_sqla, 'build_orm_file', lambda _models: 'CUSTOM\n')

    calls: list[Path] = []

    def fake_ruff(path: Path, *, fix: bool = True) -> None:
        calls.append(path)

    monkeypatch.setattr(gen_sqla, 'run_ruff', fake_ruff)

    exit_code = gen_sqla.main(['--output', str(custom_output)])

    out = capsys.readouterr()
    assert exit_code == 0
    assert custom_output.exists()
    assert custom_output.read_text(encoding='utf-8') == 'CUSTOM\n'
    assert calls == [custom_output]
    assert '[✓] ORM models written to' in out.out


def test_default_behavior_uses_output_path(
    monkeypatch, tmp_path, capsys
) -> None:
    """Ensure default behavior still writes to OUTPUT_PATH and runs Ruff."""
    default_output = tmp_path / 'default' / 'fhirx.py'
    monkeypatch.setattr(gen_sqla, 'OUTPUT_PATH', default_output)
    monkeypatch.setattr(gen_sqla, 'iter_pydantic_models', lambda: {})
    monkeypatch.setattr(
        gen_sqla, 'build_orm_file', lambda _models: 'DEFAULT\n'
    )

    calls: list[Path] = []

    def fake_ruff(path: Path, *, fix: bool = True) -> None:
        calls.append(path)

    monkeypatch.setattr(gen_sqla, 'run_ruff', fake_ruff)

    exit_code = gen_sqla.main([])

    out = capsys.readouterr()
    assert exit_code == 0
    assert default_output.exists()
    assert default_output.read_text(encoding='utf-8') == 'DEFAULT\n'
    assert calls == [default_output]
    assert '[✓] ORM models written to' in out.out


def test_output_directory_path_fails_gracefully(
    monkeypatch, tmp_path, capsys
) -> None:
    """Ensure invalid output path (directory) returns a non-zero exit code."""
    monkeypatch.setattr(gen_sqla, 'iter_pydantic_models', lambda: {})
    monkeypatch.setattr(
        gen_sqla, 'build_orm_file', lambda _models: 'IGNORED\n'
    )

    target_dir = tmp_path / 'outdir'
    target_dir.mkdir(parents=True, exist_ok=True)

    exit_code = gen_sqla.main(['--output', str(target_dir)])

    out = capsys.readouterr()
    assert exit_code == 1
    assert out.out == ''
    assert '[x] Failed to write ORM models:' in out.err
