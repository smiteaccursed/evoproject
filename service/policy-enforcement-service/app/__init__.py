import sys

# skip, if import provoke from test runners
if 'test' not in sys.argv[0]:
    from app.app import app

    __all__= [app]