import sys, os, hashlib, json, traceback, fnmatch, datetime, pathlib, collections
import numpy as np



def enum(sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


def find_files(directory, pattern):
    import os, fnmatch
    flist = []
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                filename = filename.replace('\\', '/')
                flist.append(filename)
    return flist



def find_directories(directory, pattern=None, maxdepth=None):
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            if pattern is None:
                retname = os.path.join(root, d, '')
                yield retname
            elif fnmatch.fnmatch(d, pattern):
                retname = os.path.join(root, d, '')
                retname = retname.replace('\\\\', os.sep)
                if maxdepth is None:
                    yield retname
                else:
                    if retname.count(os.sep)-directory.count(os.sep) <= maxdepth:
                        yield retname



def DoesPathExistAndIsDirectory(pathStr):
    if os.path.exists(pathStr) and os.path.isdir(pathStr):
        return True
    else:
        return False


def DoesPathExistAndIsFile(pathStr):
    if os.path.exists(pathStr) and os.path.isfile(pathStr):
        return True
    else:
        return False
