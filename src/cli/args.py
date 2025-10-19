import sys
from src.repl import repl_run
from src.runtime.runtime import execute_file

def run_repl():
    print('Zox REPL (type `exit` to quit)')
    repl_run()

def run_file(path):
    if not path.endswith('.zox'):
        print('Zox source files should have .zox extension')
        return
    execute_file(path)
