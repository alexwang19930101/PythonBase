from distutils.core import setup

setup(name="wxy",version="1.0",desciption="wxy's module",author="wxy",py_modules=['subA.aa','subA.bb'])


#in the cmdline type following 
'''
python setup.py built
python setup.py dist
'''