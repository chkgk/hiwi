#!/usr/bin/python3 
# coding=utf-8

"""Hiwi.

Usage:
  hiwi [--sfile=settings.py] integrate [--local] <package_name>
  hiwi [--sfile=settings.py] package <app_name>
  hiwi [--sfile=settings.py] publish <app_name>

Options:
  --sfile=settings.py     Use different settings file [default: settings.py]
  --web                   Integrate from web repository
  -h --help               Show this screen.
  --version               Show version.

"""
from . import hiwi
from docopt import docopt


def main():
  arguments = docopt(__doc__, version='Hiwi 0.1')
  # print(arguments)
  h = hiwi.Hiwi(arguments["--sfile"])
  if arguments["integrate"]:
    if arguments["--local"]: 
      h.integrate(arguments["<package_name>"])
    else:
      h.integrate_from_web(arguments["<package_name>"])

  if arguments["package"]:
    h.package(arguments["<app_name>"])

  if arguments["publish"]:
    h.publish(arguments["<app_name>"])