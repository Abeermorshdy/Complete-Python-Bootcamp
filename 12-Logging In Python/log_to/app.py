'''Write a Python script that sets up logging for a multi-module application. 
Each module should have its own logger.'''
from logger import logger1
from logger import logger2

def multiple(a,b):
    logger1.debug("the opration is running")
    return a*b

def divide(a,b):
    try:
        return a/b
    except Exception:
        raise logger2.exception("You cann't divide by zero")

multiple(2,3)
divide(2,1)
