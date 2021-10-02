
import logging
import os
import argparse
import sys

import git

from .build import build
from .config import config
from .install import install

def main():

  # Get a logger.
  logging.basicConfig(level=logging.DEBUG)
  logger = logging.getLogger('mxkb')

  # Work out build dir path.
  repo = git.Repo(os.getcwd(), search_parent_directories=True)
  project_dir = repo.git.rev_parse("--show-toplevel")

  # Arguments.
  parser = argparse.ArgumentParser(description='Manage C++ dependencies.')
  subparsers = parser.add_subparsers(dest='command')

  parser_build = subparsers.add_parser('build', aliases=['bld', 'b'])
  parser_configure = subparsers.add_parser('config', aliases=['cfg', 'c'])
  parser_install = subparsers.add_parser('install', aliases=['i'])

  args = parser.parse_args()
  if args.command is None:
    exit_code = config(logger, project_dir)
    exit_code = exit_code | build(logger, project_dir)
    exit_code = exit_code | install(logger, project_dir)
    sys.exit(exit_code)
  if args.command in ['config', 'cfg', 'c']:
    exit_code = config(logger, project_dir)
    sys.exit(exit_code)
  elif args.command in ['build', 'bld', 'b']:
    exit_code = build(logger, project_dir)
    sys.exit(exit_code)
  elif args.command in ['install', 'i']:
    exit_code = install(logger, project_dir)
    sys.exit(exit_code)
  else:
    parser.print_help()
    sys.exit(1)

__all__ = []