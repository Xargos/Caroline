import os
import importlib

def getPlugins():
    # get this folder's content
    contents = os.listdir(os.curdir + '/plugins')

    # import all .py files except for __init__.py
    for i in contents:
        if i.endswith('.py') == True and i != '__init__.py':
            imported = importlib.import_module('plugins.'+ i[:-3])
            imported.main()
            del imported
    del i