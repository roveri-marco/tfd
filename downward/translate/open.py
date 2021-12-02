#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import pddl

if __name__ == "__main__":
  task = pddl.pddl_open()
  task.dump()
