import logging
logging.basicConfig(level=logging.DEBUG, filename="//Users/jiniab/PycharmProjects/Seleniumlog/demo_logs.txt",
                    datefmt='%m/%d/%Y:%M:%S %p',
                    )
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug('this is DEBUG message')
logging.info("this is the info message")
logging.warning("this is the warning message")
logging.error("this is the error message")
logging.critical("this is the critical message")
