# main.py

import core
import logging
import logging.config

log = logging.getLogger(__name__)

logging.config.fileConfig('configuration.ini')
log.info('running core.do_something')
core.do_something()
log.debug('this is where we tried to do something bad')
log.error('the thing we did caused an error')