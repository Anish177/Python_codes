import itertools
import re

def solve(formula):
    return filter(valid, letter_replacements(formula))

def letter_replacements(formula):
    formula = formula.replace(' = ', ' == ')
    letters = concat(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        yield formula.translate(str.maketrans(letters, concat(digits)))

def valid(exp):
    try:
        return not leading_zero(exp) and eval(exp) is True
    except ArithmeticError:
        return False

concat = ''.join
    
leading_zero = re.compile(r'\b0[0-9]').search

word1 = input('Enter first word: ').upper()
word2 = input('Enter second word: ').upper()
result = input('Enter their result: ').upper()
expression = word1 + '+' + word2 + '==' + result #input('Enter the expression: ')
print('Expression is:', expression)
print('Solution is:', next(solve(expression)))
