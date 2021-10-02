#!/usr/bin/env python3

import logging
import os
import sys

if __name__ == '__main__':
  # Get a logger.
  logger = logging.getLogger('config.py')

  # Work out build dir path.
  repo = git.Repo(os.getcwd(), search_parent_directories=True)
  project_dir = git_repo.git.rev_parse("--show-toplevel")
  build_dir = os.path.abspath(os.path.join(project_dir, 'build'))

  # Create build dir.
  os.makedirs(build_dir, exist_ok=True)
  # Set current directory to build dir.
  os.chdir(build_dir)

  # Configure using cmake.
  logger.info(f"Configuring...")
  exit_code = os.system(f"cmake .. -DCMAKE_INSTALL_PREFIX={os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'install'))}")

  # Done.
  sys.exit(exit_code)
