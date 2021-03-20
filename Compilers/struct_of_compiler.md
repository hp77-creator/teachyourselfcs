## Structure of Compiler

Recall that a compiler has 5 major phases(Lexical Analysis, Parsing, Semantic Analysis, Optimization and Code Generation), Let's try to understand these with analogy with how humans understand English.

- First Step: Recognize words
  *This is a sentence*
  - Smallest unit above letters
  The goal of lexical analysis to divide program text into "words" or "tokens"
  
  ex: *if x==y then z=1; else z=2*

  In above line, there are some keywords(if, then, else), then some variables(x, y, z), there are constants(1, 2), there are also separators and also operators, we will see how we computer learns it differently.

- Once words are understood, the next step is to understand sentence structure
  
  Parsing = Diagramming Sentences

  - The diagram is a tree
