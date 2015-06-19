#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author(s)
---------
John M. Howard

Date
----
06-18-15
"""

import os
import imp
import inspect

PROJECT_PATHS_MODULES = ""


def test_paths_existence():
    for dir_name, subdir_list, filename_list in os.walk(PROJECT_PATHS_MODULES):

        for full_filename in filename_list:
            filename, file_ext = os.path.splitext(full_filename)

            if file_ext == ".py":
                _file, _path, _description = imp.find_module(filename, [dir_name])

                try:
                    mod = imp.load_module(filename, _file, _path, _description)

                    for path_module_var, path_module_val in inspect.getmembers(mod):

                        if path_module_var.isupper():

                            if isinstance(path_module_val, str):
                                yield _check_path_exists, path_module_val

                            elif isinstance(path_module_val, list):

                                for path in path_module_val:
                                    yield _check_path_exists, path

                except:
                    pass


def _check_path_exists(obj):
    print obj
    assert os.path.exists(obj)


if __name__ == "__main__":
    test_paths_existence()
