import datetime
import logging
import os
import sys
import tarfile
import yaml
from logcleaner import del_older_files,arc_older_files

#Tool setup variables here
archive_name="test.tar"

#Test2 using logging module --May 19 2022
logging.basicConfig(filename="testfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Process the directories using YAML as config file
with open('testconfig.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    for key,value in (config[0]).items():
        listing = list(value.values())
        for directory in listing:
            directory = directory.strip()
            del_older_files(directory)

with open('testconfig.yaml') as f2:
    config = yaml.load(f2, Loader=yaml.FullLoader)
    for key,value in (config[1]).items():
        listing = list(value.values())
        for directory in listing:
            directory = directory.strip()
            arc_older_files(directory)