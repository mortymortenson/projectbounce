#!/usr/bin/env python3

import importlib
import sys
import traceback

modules = [
        'autolist',
        'bounce',
        'bounce_app',
        'bounce_main',
        'name',
        'sample',
        'sliding_total',
        'vwap',
        ]

for module_name in modules:
    print("====== Running Tests: %s ======" % module_name)
    module = importlib.import_module(module_name)
    good = module.runTests()
    print("")

print("ALL TESTS PASSED")

