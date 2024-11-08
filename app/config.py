from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get log level from environment
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = os.getenv(
    "LOG_FORMAT", "%(asctime)s - %(levelname)s - %(message)s"
)