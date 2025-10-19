<img width="1024" height="1024" alt="zox" src="https://github.com/user-attachments/assets/27dbd95c-c888-4e2f-8e38-33d4ab4ff078" />
# Zox Prog    <img width="1024" height="1024" alt="zox" src="https://github.com/user-attachments/assets/add0fa62-44de-444b-ba24-17385c370e23" />
ramming Language v1 — Official Documentation

## Overview
Zox is a modern, lightweight, and expressive programming language designed for **speed, concurrency, and simplicity**. It features a **shell-style syntax**, asynchronous tasks, and built-in data pipelines, making it ideal for scripting, automation, and scalable applications.

### Philosophy
- Command-like syntax with minimal punctuation
- Curly braces `{}` for blocks instead of indentation
- Async-first design with `task` and `run`
- Native concurrency and data flow operators
- Beginner-friendly and fast

### File Extension
- Zox source files: `.zox`
- Interpreter: `zc_interpreter.zx`

---

## Getting Started

### Running a Zox Program
1. Create a `.zox` file, e.g., `hello.zox`:
```zox
say "Hello Zox"
```
2. Run with the interpreter:
```bash
zox zc_interpreter.zx hello.zox
```
3. Optional (Linux/Mac) make it executable:
```bash
chmod +x zc_interpreter.zx
./zc_interpreter.zx hello.zox
```

---

## Syntax Reference

### Variables
```zox
let x = 10
let name = "Supriyo"
x -> 20  # reassign
```

### Functions
```zox
func greet(name) {
    say "hello " + name
}
greet("Supriyo")
```

### Control Flow
```zox
if x > y {
    say "x is greater"
} else {
    say "y is greater"
}
```
Shorthand:
```zox
if x > y -> say "x > y"
```

### Loops
```zox
for i in range(1,5) {
    say "loop #" + i
}
```
List iteration:
```zox
for n in ["a","b","c"] {
    say "value:" + n
}
```

### Async & Tasks
```zox
task download(url) {
    data = net.get(url)
    say "got " + len(data)
}
run download("https://api.com")
```

### Structs
```zox
type user {
    name
    age
}
u = user("supriyo", 22)
say u.name
```

### Imports
```zox
use net
use math
```

### Comments
```zox
# This is a comment
```

### Data Flow Operators
```zox
get "users.json" -> parse.json -> print
get "data.csv" -> filter(row.age > 18) -> save "adults.csv"
```

---

## Built-in Commands
| Command | Description |
|---------|-------------|
| say | Prints text |
| let | Defines variable |
| -> | Reassigns variable |
| func | Defines function |
| task | Defines async job |
| run | Executes a task |
| get | Fetch HTTP or file |
| pipe/-> | Chains data |
| type | Define struct |
| use | Import module |
| if, for | Control flow |
| exit | Quit program |

---

## Example Program
```zox
use net
urls = ["https://a.com", "https://b.com", "https://c.com"]

task fetch(url) {
    data = net.get(url)
    say "fetched " + url + " (" + len(data) + " bytes)"
}

for u in urls {
    run fetch u
}

say "all downloads started"
```

---

## Internal Design
| Component | Purpose |
|-----------|---------|
| Lexer & Parser | Tokenize and parse shell-style input |
| AST | Abstract Syntax Tree for program logic |
| Runtime | Executes tasks, loops, pipes |
| Compiler Backend | Future native compilation to Go/C++ |
| Standard Library | Built-ins for I/O, HTTP, Math, Concurrency |

---

## Roadmap
| Feature | Status |
|---------|--------|
| Interpreter (Python prototype) | ✅ Built |
| Async runtime | 🔜 Planned |
| Static type checker | 🔜 Planned |
| File I/O + JSON libraries | 🔜 Planned |
| Native compiler (LLVM) | 🔜 Planned |
| Package manager (`zpm`) | 🔜 Planned |

---

## Summary
Zox is a **unique, shell-style language** designed for modern scripting, automation, and concurrent programming. It’s readable, expressive, and scalable — built to feel like a **command-line shell** with programming power.

---

*© Supriyo Maji — Zox Language Project*
