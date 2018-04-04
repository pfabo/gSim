#!/usr/bin/env python
'''
B{gsim directory tree, Credit Robin Parmar, Alex Martelli }

You need to examine a directory, or an entire directory tree rooted in a certain directory, and
obtain a list of all the files (and optionally folders) that match a certain pattern.

From::
    Python Cookbook, O'REILLY 2002
'''
import os.path, fnmatch

def listFiles(root, patterns='*', recurse=1,return_folders=0):
    '''
    Skript pre rekurzivne prehladanie adresarov. Vrati zoznam nacitanych suborov 
    s cestami podla zadaneho vzoru.
    '''
    # Expand patterns from semicolon-separated string to list
    pattern_list = patterns.split(';')
    # Collect input and output arguments into one bunch
    class Bunch:
        def __init__(self, **kwds): self.__dict__.update(kwds)
         
    arg = Bunch(recurse=recurse, pattern_list=pattern_list, return_folders=return_folders, results=[])

    def visit(arg, dirname, files):
        # Append to arg.results all relevant files (and perhaps folders)
        for name in files:
            fullname = os.path.normpath(os.path.join(dirname,name))
            
            if arg.return_folders or os.path.isfile(fullname):
                for pattern in arg.pattern_list:
                    if fnmatch.fnmatch(name, pattern):
                        arg.results.append(fullname)
                        break
        # Block recursion if recursion was disallowed
        if not arg.recurse: files[:]=[]

    os.path.walk(root, visit, arg)
    return arg.results


