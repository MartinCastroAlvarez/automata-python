# Python Automata
Implementation Automatas using Python

## Papers

* [Automatas Finitos No Deterministas](AFN1.pdf)

## Instructions

#### Run the AFN that accepts email addresses.

```bash
python3 emailAfn.py "loremipsum@gmail.com"
```
```bash
Transitioning: <Symbol: 'l'> causes (<State: '0'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: 'o'> causes (<State: '1'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: 'r'> causes (<State: '1'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: 'e'> causes (<State: '1'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: 'm'> causes (<State: '1'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: 'i'> causes (<State: '1'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: 'p'> causes (<State: '1'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: 's'> causes (<State: '1'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: 'u'> causes (<State: '1'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: 'm'> causes (<State: '1'>, <Symbol: '[DEFAULT]'>) => {<State: '1'>}
Transitioning: <Symbol: '@'> causes (<State: '1'>, <Symbol: '@'>) => {<State: '3'>}
Transitioning: <Symbol: 'g'> causes (<State: '3'>, <Symbol: '[DEFAULT]'>) => {<State: '4'>}
Transitioning: <Symbol: 'm'> causes (<State: '4'>, <Symbol: '[DEFAULT]'>) => {<State: '5'>}
Transitioning: <Symbol: 'a'> causes (<State: '5'>, <Symbol: '[DEFAULT]'>) => {<State: '5'>}
Transitioning: <Symbol: 'i'> causes (<State: '5'>, <Symbol: '[DEFAULT]'>) => {<State: '5'>}
Transitioning: <Symbol: 'l'> causes (<State: '5'>, <Symbol: '[DEFAULT]'>) => {<State: '5'>}
Transitioning: <Symbol: '.'> causes (<State: '5'>, <Symbol: '.'>) => {<State: '6'>}
Transitioning: <Symbol: 'c'> causes (<State: '6'>, <Symbol: '[DEFAULT]'>) => {<State: '7'>}
Transitioning: <Symbol: 'o'> causes (<State: '7'>, <Symbol: '[DEFAULT]'>) => {<State: '7'>}
Transitioning: <Symbol: 'm'> causes (<State: '7'>, <Symbol: '[DEFAULT]'>) => {<State: '7'>}
Accepted: 'loremipsum@gmail.com'
```
