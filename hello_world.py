# Good to have a skeleton of the code before starting actual coding

#   1 - write out the comments of expected functions
#   2 - create those functions with proper docstrings, logging, and pass ONLY
#       NOTE:  pass is a null operation (nothing happens) and is therefore
#              only used as a placeholder when no code needs to be executed
#              such as when a function doesn't do anything yet or have logging
#   3 - tie the functions together in your __main__
#   4 - test the logic with print or logging statements
# =============================================================================
# More information on logging can be found here:
#   www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging
#   www.digitalocean.com/community/tutorials/how-to-use-logging-in-python3
#   www.loggly.com/ultimate-guide/python-logging-basics
# =============================================================================

import logging

logging.basicConfig(
    filename='Output.log',       # consider using formatting instead
    filemode='w',                       # overwrites the file every time
    level=logging.DEBUG,                # lowest logging level
    format="%(asctime)s|%(levelname)s: %(name)s @ %(lineno)d|%(message)s"
    )

# setup logging buffer for console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG) # all DEBUG or higher will show on console

# set format easy for console to use
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger(__name__).addHandler(console)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    """
    This function is the main function
    """

    logger.debug('Starting {}()...'.format(__name__))
    print("Hello World")
    # pass
    logger.debug('Ending {}()...'.format(__name__))
