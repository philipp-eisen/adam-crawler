import os.path

import config
import logger


try:
    _logging = config.get("logging")
except config.ConfigurationError:
    _logging = {'logconfig': ''}

logger.Logger.setup_logging(os.path.join(config.PROJECT_BASE, _logging["logconfig"]))