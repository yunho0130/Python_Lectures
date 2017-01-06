# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 17:09:47 2017

@author: Yunho
"""

import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print "Logging to", logging_file

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

