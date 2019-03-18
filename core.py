# core.py

import logging
log = logging.getLogger(__name__)

def do_something():
  log.debug('debug message')
  log.info('info message')
  log.warning('warning message')
  log.error('error message')
  log.critical('critical message')
  log.exception('exception message')
