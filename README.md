# Papy

Pseudo assembly interpreter made in Python.

## Requirements

Python 3.6+ is required.

## Usage

```
!!!IMPORTANT!!!
NEVER USE REGISTER 0, IT'S RESERVED FOR COMPARISION
ARRAY IS GENERATED WITH RANDOM NUMBERS FROM -99 TO -99 (INCLUDING BOTH)
TO REFER TO N-POSITION IN THE ARRAY USE ARRAY_NAME(N*4)
CLEAR REGISTER BEFORE USING IT

Scheme
<short description>
<command>
<example>

Definition
NAME    DC    INTEGER(SOME_NUMBER)
ONE     DC    INTEGER(1)

Declaring numbers
NAME    DS    INTEGER
ANSWER  DS    INTEGER

Declaring arrays
NAME    DS    LENGTH*INTEGER
TABLE   DS    100*INTEGER

Loading from memory to register
LABEL   L     REG,MEM
        L     1,ONE

Loading from register to register
LABEL   LR    REG1,REG2
        LR    1,2
  
Loading from register to memory
LABEL   ST    REG,MEM
        LR    1,ANSWER

Adding memory to register
LABEL   A     REG,MEM
        A     1,ONE

Subtracting register by memory
LABEL   S     REG,MEM
        S     1,ONE

Multiplying register by memory
LABEL   M     REG,MEM
        M     1,FOUR

Dividing register by memory
LABEL   D     REG,MEM
        D     1,FOUR

Adding register to register
LABEL   AR    REG1,REG2
        AR    1,2

Subtracting register by register
LABEL   SR    REG1,REG2
        SR    1,2

Multiplying register by register
LABEL   MR    REG1,REG2
        MR    1,2

Dividing register by register
LABEL   DR    REG1,REG2
        DR    1,2

Comparing (subtracting) register by memory
LABEL   C     REG,MEM
        C     1,ONE

Comparing (subtracting) register by register
LABEL   CR    REG1,REG2
        CR    1,2

Unconditional jump
LABEL   J     LABEL_TO_JUMP
        J     END

Jump if last comparision was zero
LABEL   JZ    LABEL_TO_JUMP
        JZ    END

Jump if last comparision was negative
LABEL   JN    LABEL_TO_JUMP
        JN    END

Jump if last comparision was positive
LABEL   JP    LABEL_TO_JUMP
        JP    END

Print memory
LABEL   P     MEM
        P     ANSWER

Print register
LABEL   PR    REG
        PR    1
```

## Running

```sh
$ python3 papy.py filename.papy
```

## Examples

```sh
$ python3 papy.py examples/euclidean_algorithm.papy
7

$ python3 papy.py examples/sum_positive_elements.papy
2420
```

## Author

The author of this repository is [Jakub Rudnik](https://github.com/Zeraye).
