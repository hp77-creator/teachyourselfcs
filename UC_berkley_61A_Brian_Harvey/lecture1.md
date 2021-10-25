# Introduction

Brian Harvey(BH) gave the introduction that this course is based on different paradigms in computing.
He also introduced himself, course and also the book [Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html).

He then went on to give intro about the programming language that we will be using for the course, It is a variant of Scheme called Stk.

To download Scheme, you can use the following link:
[MIT-Scheme](https://www.gnu.org/software/mit-scheme/)

I tried installing Stk, but because of some issues, couldn't.

I am sticking with Scheme for the time being as the concepts taught in the course will be same irrespective of the language, only difference will be in some functions that Stk has over Scheme. I can bear with that.

He went on to demonstrate different syntax of Stk like:

```Scheme
=> (+ 6 8)
14

=> (* 6 8)
48

=> (+)
0

=> (*)
1

=> ('+)
+

=> (word 'hello 'world)
hello world
```

`word` is not found in `Scheme`, and there are some other functions that are in `Stk` like `butfirst`, `butlast` and so on.

Most of them are string functions which are implemented by the berkeley implementation of the `Scheme`.

I tried some commands from the video, default ones, everything is function in `Scheme` .

You can use `define` to define new variables and also new functions like following:

```Scheme

=> (define square (x)
            (x * x))
square

=> (square 5)
25

```

We can also define variables like above method:
```Scheme
=> (define PI 3.141)
PI
=> PI
3.141
```

Professor was talking about recursion using a `pigl` method but class got over and discussion is continued onto the second lecture.

[Lecture-2](./lecture2.md)

[Table of Content](./Readme.md)
