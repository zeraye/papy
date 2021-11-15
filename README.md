# Papy

Pseudo assembly interpreter made in Python3.

## Important

- Neger use register 0, it is reserved for `C` and `CR` (comparision operators)
- Arrays are generated with random numbers from -99 to 99 (including both), unless you change it (TODO)
- To refer to N-th position in the array use `ARR_NAME(N*4)`
- At the very beginning registers have some trash values in them (TODO)

## Operations
Label | Operator | Value(s) | Description
--- | --- | --- | ---
`VAR_NAME` | `DC` | `INTEGER(SOME_NUMBER)` | declare `INTEGER` and assign `SOME_NUMBER`
`VAR_NAME` | `DS` | `INTEGER` | declare `INTEGER`
`ARR_NAME` | `DS` | `LENGTH*INTEGER` | declare array of `INTEGER`'s with length of  `LENGTH`
`LABEL_NAME` | `L` | `REG, MEM` | load value from `MEM` to `REG`
`LABEL_NAME` | `LR` | `REG1, REG2` | load `REG2` to `REG1`
`LABEL_NAME` | `ST` | `REG, MEM` | load `MEM` address to `REG`
`LABEL_NAME` | `A` | `REG, MEM` | add value from `MEM` to `REG`
`LABEL_NAME` | `S` | `REG, MEM` | subtract value from `MEM` from `REG`
`LABEL_NAME` | `M` | `REG, MEM` | multiply `REG` by value from `MEM`
`LABEL_NAME` | `D` | `REG, MEM` | divide `REG` by value from `MEM`
`LABEL_NAME` | `AR` | `REG1, REG2` | add `REG2` to `REG1`
`LABEL_NAME` | `SR` | `REG1, REG2` | subtract `REG2` from `REG1`
`LABEL_NAME` | `MR` | `REG1, REG2` | multiply `REG1` by `REG2`
`LABEL_NAME` | `DR` | `REG1, REG2` | divide `REG1` by `REG2`
`LABEL_NAME` | `C` | `REG, MEM` | compare `REG` with value from `MEM` (subtract value from `MEM` from `REG` and write to register 0)
`LABEL_NAME` | `CR` | `REG1, REG2` | compare `REG1` with `REG2` (subtract `REG2` from `REG1` and write to register 0)
`LABEL_NAME` | `J` | `LABEL_TO_JUMP` | unconditionally jump to `LABEL_TO_JUMP`
`LABEL_NAME` | `JP` | `LABEL_TO_JUMP` | if register 0 is positive jump to `LABEL_TO_JUMP`
`LABEL_NAME` | `JZ` | `LABEL_TO_JUMP` | if register 0 is zero jump to `LABEL_TO_JUMP`
`LABEL_NAME` | `JN` | `LABEL_TO_JUMP` | if register 0 is negative jump to `LABEL_TO_JUMP`
`LABEL_NAME` | `P` | `MEM` | write value from `MEM` to terminal
`LABEL_NAME` | `PR` | `REG` | write `REG` to terminal

## Running

```sh
$ python3 papy.py filename.papy
```

## Examples

```sh
$ python3 papy.py examples/euclidean_algorithm.papy
7
```

```sh
$ python3 papy.py examples/sum_positive_elements.papy
2420
```

## Requirements

[Python 3.6+](https://www.python.org) is required.

## Roadmap

- [ ] Error handling
- [ ] Preprocessor directive
- [ ] Debugging tools
- [ ] Trash values in registers at the very beginning

## Author

The author of this repository is [Jakub Rudnik](https://github.com/Zeraye).
