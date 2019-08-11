https://github.com/python/cpython/blob/3.7/Python/ceval.c

Compilation stages:

    1. lexical analysis (keywords, variables, indentation)
    2. syntactical analysis (token stream -> AST)
    3. compilation (AST -> bytecode)
        a. AST -> basic blocks
        b. basic blocks -> abstract instructions + [code object]
        d. peephole optimization: instructions -> instructions
        c. assembler: instructions -> bytecode + [code object]
            1. dfs: unordered basic blocks -> ordered basic blocks
    4. PYC generation: code object -> written to file
        a. generate header [magic number + hash || modified date + size]
        b. marshal code object
