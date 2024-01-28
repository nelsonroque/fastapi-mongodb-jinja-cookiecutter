from .utils import get_utc_timestamp
from .storage import init_db
import logging

# Configure the logger as needed
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)