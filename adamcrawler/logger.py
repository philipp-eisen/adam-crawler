import os
import json
import logging.config


class Logger:

    @classmethod
    def setup_logging(cls, configfile_path, default_level=logging.DEBUG, env_key='LOG_CFG'):
        """Setup logging configuration

        """
        if os.path.isfile(configfile_path):
            path = configfile_path
            value = os.getenv(env_key, None)
            if value:
                path = value
            if os.path.isfile(path):

                try:
                    with open(path, 'rt') as f:
                        config = json.load(f)
                    logging.config.dictConfig(config)
                except ValueError as e:
                    print("Unable to configure logging: \n\t{0}".format(e))
                    print("Loading basic configuration")
                    logging.basicConfig(level=default_level)
                else:
                    pass
            else:
                logging.basicConfig(level=default_level)
        else:
            logging.basicConfig(level=default_level)

    @classmethod
    def info(cls, msg, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.info(msg, *args, **kwargs)

    @classmethod
    def debug(cls, msg, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.debug(msg, *args, **kwargs)

    @classmethod
    def warning(cls, msg, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.warning(msg, *args, **kwargs)

    @classmethod
    def error(cls, msg, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.error(msg, *args, **kwargs)

    @classmethod
    def critical(cls, msg, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.critical(msg, *args, **kwargs)
