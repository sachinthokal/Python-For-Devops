# Tests for the log function - no Ollama, no Docker needed.  python -m pytest .

from pathlib import Path

from devops_tools import count_log_levels, list_containers, read_log_file

SAMPLE = """2025-01-10 09:00:01 INFO started
2025-01-10 09:05:12 WARNING high memory
2025-01-10 09:10:22 ERROR failed
2025-01-10 09:10:25 ERROR timeout"""


def test_counts_basic():
    assert count_log_levels(SAMPLE) == {"INFO": 1, "WARNING": 1, "ERROR": 2}


def test_no_substring_false_positive():
    assert count_log_levels("2025 INFO no errors here")["ERROR"] == 0


def test_bundled_app_log():
    app_log = Path(__file__).parent / "app.log"
    counts = count_log_levels(read_log_file(str(app_log)))
    assert counts == {"INFO": 10, "WARNING": 2, "ERROR": 3}


def test_list_containers_returns_text():
    # Works whether or not Docker is installed - always returns a friendly string.
    assert isinstance(list_containers(), str)
