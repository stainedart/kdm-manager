#!/usr/bin/env python

#   standard
from ConfigParser import SafeConfigParser
import logging
import os
from pymongo import MongoClient
import sys
from user_agents import parse as ua_parse


# function to get settings. This has to be up top.

def load_settings():
    """ Creates a settings object from settings.cfg in the application root dir.
    This func has to be at the top of this module, since everything below here
    (basically) uses it. """

    config = SafeConfigParser()
    config.readfp(open("settings.cfg"))
    config.file_path = os.path.abspath("settings.cfg")
    return config


#
#   General purpose helpers and references
#

settings = load_settings()
ymd = "%Y-%m-%d"
mdb = MongoClient()[settings.get("application","mdb")]


#
#  application helper functions
#


#  sysadmin helper functions

def get_user_agent():
    """ Returns a user-agents object if we can get a user agent. Otherwise,
    returns None. """

    if "HTTP_USER_AGENT" not in os.environ:
        return None
    else:
        return ua_parse(os.environ["HTTP_USER_AGENT"])


def get_logger(log_level="INFO", log_name=False):
    """ Creates a generic logger at the specified log level."""

    settings = load_settings()

    #   initialize a generic logger
    logger = logging.getLogger(__name__)

    if not len(logger.handlers):    # if it's not already open, open it
        exec 'log_level_obj = logging.%s' % log_level
        logger.setLevel(log_level_obj)

        #   set the logger's name and path
        log_file_name = log_name
        if not log_file_name:
            log_file_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]

        log_root_dir = settings.get("application","log_dir")
        if not os.path.isdir(log_root_dir):
            e = Exception("Logging root dir '%s' does not exist!" % log_root_dir)
            raise e

        log_path = os.path.join(log_root_dir, log_file_name + ".log")
        logger_fh = logging.FileHandler(log_path)

        #   set the formatter and add it via addHandler()
        formatter =  logging.Formatter('[%(asctime)s] %(levelname)s:\t%(message)s',"%Y-%m-%d %H:%M:%S")
        logger_fh.setFormatter(formatter)
        logger.addHandler(logger_fh)

    return logger




if __name__ == "__main__":
    print("Starting unit tests...")
    settings = load_settings()
    if not settings:
        raise Exception("Settings file could not be loaded!")
    else:
        print(" Settings file '%s' loaded!" % settings.file_path)
    logger = get_logger()
    if not logger:
        raise Exception("Logger could not be initialized!")
    else:
        print(" Logger initialized!")

    logger.info("Unit tests passed!")
