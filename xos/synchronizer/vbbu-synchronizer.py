#!/usr/bin/env python

# This imports and runs ../../xos-observer.py
# Runs the standard XOS observer

import importlib
import os
import sys
observer_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "../../synchronizers/new_base")
sys.path.append(observer_path)
mod = importlib.import_module("xos-synchronizer")
mod.main()
