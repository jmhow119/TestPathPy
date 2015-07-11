#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author(s)
---------
John M. Howard

Purpose
-------
Tests for the existence of the paths definited
in the specified modules.

Created On
----------
06-18-15

Updated On
----------
07-11-15

Requirements
------------
Nosetests
"""
import os
import imp
import inspect

PATHS_MODULES = "/Users/John/Desktop/NIST/slre/paths/ivec14_paths.py"


def test_paths_existence():
    if os.path.isdir(PATHS_MODULES):

        for dir_name, subdir_list, filename_list in os.walk(PATHS_MODULES):

            for full_filename in filename_list:
                filename, file_ext = os.path.splitext(full_filename)

                if file_ext == ".py":
                    _file, _path, _description = imp.find_module(filename, [dir_name])
                    print _file
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

    elif os.path.exists(PATHS_MODULES):
        dir_name, filename = os.path.split(PATHS_MODULES)
        filename, file_ext = os.path.splitext(filename)

        if file_ext == ".py":
            _file, _path, _description = imp.find_module(filename, [dir_name])
            print _file
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

    else:
        print "not a directory or a file"


def _check_path_exists(obj):
    print obj
    assert os.path.exists(obj)


if __name__ == "__main__":
    test_paths_existence()
