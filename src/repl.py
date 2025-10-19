def repl_run():
    env = {}
    while True:
        try:
            line = input('zox> ').strip()
            if not line:
                continue
            if line in ('exit','quit'):
                print('bye')
                break
            # very naive handling
            if line.startswith('say '):
                print(line[4:].strip().strip('"'))
            elif line.startswith('let '):
                print('set variable (REPL prototype)')
            else:
                print('not implemented in REPL prototype')
        except EOFError:
            break
