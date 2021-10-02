#!/usr/bin/env python3

import os
import sys

def install(logger, project_dir):
  # Work out build dir path.
  build_dir = os.path.abspath(os.path.join(project_dir, 'build'))

  try:
    # Set current directory to build dir.
    os.chdir(build_dir)
  except:
    logger.error(f"Build directory '{build_dir}' does not exist; have you ran config.py?")
    sys.exit(1)

  # Build using cmake.
  logger.info(f":: Installing ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
  exit_code = os.system("cmake --install .")

  # Done.
  return exit_code

__all__ = [install]