#!/usr/bin/env python3

import os
import sys

def config(logger, project_dir):
  # Work out build dir path.
  build_dir = os.path.abspath(os.path.join(project_dir, 'build'))
  install_dir = os.path.abspath(os.path.join(project_dir, 'install'))

  # Create build dir.
  os.makedirs(build_dir, exist_ok=True)
  # Set current directory to build dir.
  os.chdir(build_dir)

  # Configure using cmake.
  logger.info(f":: Configuring :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
  exit_code = os.system(f"cmake .. -DCMAKE_INSTALL_PREFIX={install_dir}")

  # Done.
  return exit_code

__all__ = [config]
