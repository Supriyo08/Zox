# Runtime: evaluates parsed statements in a simple environment
import os, sys
from src.parser.parser import parse_lines

def eval_expr(expr, env):
    # Very naive evaluator: handle numbers, strings, + operator, names
    expr = expr.strip()
    if expr.isdigit():
        return int(expr)
    if expr.startswith('"') and expr.endswith('"'):
        return expr[1:-1]
    if '+' in expr:
        parts = expr.split('+',1)
        return str(eval_expr(parts[0], env)) + str(eval_expr(parts[1], env))
    # variable
    return env.get(expr, expr)

def execute_stmts(stmts, env):
    for s in stmts:
        if s[0] == 'say':
            val = eval_expr(s[1], env)
            print(val)
        elif s[0] == 'let':
            env[s[1]] = eval_expr(s[2], env)
        elif s[0] == 'func_def':
            # stub: store header for later (not fully parsed)
            name = s[1]
            env.setdefault('_funcs', []).append(name)
        elif s[0] == 'expr':
            # attempt to call function without args
            call = s[1]
            if call in env.get('_funcs', []):
                print(f"(call) {call} - function calling not implemented fully yet")
            else:
                print(f"Unrecognized expression: {call}")
        else:
            print('Unknown stmt', s)

def execute_file(path):
    with open(path, 'r') as f:
        content = f.read()
    lines = content.splitlines()
    stmts = parse_lines(lines)
    env = {}
    execute_stmts(stmts, env)
