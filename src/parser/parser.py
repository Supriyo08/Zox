# Extremely small parser that converts a token list into statements.
# For the starter, we only parse lines using simple heuristics.
def parse_lines(lines):
    stmts = []
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith('#'):
            continue
        if s.startswith('say '):
            expr = s[4:].strip()
            stmts.append(('say', expr))
        elif s.startswith('let '):
            rest = s[4:].strip()
            if '=' in rest:
                name, expr = rest.split('=',1)
                stmts.append(('let', name.strip(), expr.strip()))
        elif s.startswith('func '):
            # very simple: func name(args) { ... }
            header = s
            stmts.append(('func_def', header))
        else:
            stmts.append(('expr', s))
    return stmts
