import os
from app.config import LOG_LEVEL
from dotenv import load_dotenv

def test_log_level_env_var(monkeypatch):
    """Test that LOG_LEVEL is correctly loaded from the environment variable."""
    monkeypatch.setenv("LOG_LEVEL", "INFO")
    load_dotenv()  # Reload environment variables
    from app.config import LOG_LEVEL  # Re-import to pick up changes
    assert LOG_LEVEL == "INFO"

def test_default_log_level(monkeypatch):
    """Test that LOG_LEVEL defaults to INFO if the environment variable is not set."""
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    load_dotenv()  # Reload environment variables
    from app.config import LOG_LEVEL  # Re-import to pick up changes
    assert LOG_LEVEL == "INFO"
