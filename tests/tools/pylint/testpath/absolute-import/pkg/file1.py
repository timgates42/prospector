"""Module with absolute import"""
from __future__ import absolute_import, print_function

from tzlocal import unix

print(unix.get_localzone())
