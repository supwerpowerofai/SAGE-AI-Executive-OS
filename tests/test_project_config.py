from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[1]


def test_project_metadata_is_configured():
    """Keep the package metadata and supported Python version explicit."""
    with (ROOT / "pyproject.toml").open("rb") as config_file:
        config = tomllib.load(config_file)

    project = config["project"]
    assert project["name"] == "sage-ai-executive-os"
    assert project["requires-python"] == ">=3.10"
    assert project["dependencies"] == []


def test_pytest_is_configured_for_the_tests_directory():
    """Ensure local and CI test runs discover the same test directory."""
    with (ROOT / "pyproject.toml").open("rb") as config_file:
        config = tomllib.load(config_file)

    pytest_config = config["tool"]["pytest"]["ini_options"]
    assert pytest_config["testpaths"] == ["tests"]
    assert pytest_config["pythonpath"] == ["src"]
