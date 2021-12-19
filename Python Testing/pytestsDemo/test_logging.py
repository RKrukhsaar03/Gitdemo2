import logging

def test_loggingDemo():
    logger = logging.getLogger(_name_)

    fileHandler = logging.fileHandler('logfile.log')
    formatter = logging.formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # to create a connection between the logger and filehandler

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")