#!/usr/bin/env python3

import logging
import os
import sys

if __name__ == '__main__':
  # Get a logger.
  logger = logging.getLogger('build.py')

  # Work out build dir path.
  build_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'build'))

  try:
    # Set current directory to build dir.
    os.chdir(build_dir)
  except:
    logger.error(f"Build directory '{build_dir}' does not exist; have you ran config.py?")
    sys.exit(1)

  # Build using cmake.
  logger.info(f"Installing...")
  exit_code = os.system("cmake --install .")

  # Done.
  sys.exit(exit_code)