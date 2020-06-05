"""Simple test of just running the README example. Better tests to come."""

from __future__ import print_function
import crayons
from crayons import *  # NOQA

print(crayons.red('red string'))
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))
crayons.disable()
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))
print('non-string value {!s}'.format(crayons.red(1234)))
crayons.enable()
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))
print('non-string value {!s}'.format(crayons.red(1234)))
print(crayons.red('red string', bold=True))
print(crayons.yellow('yellow string', bold=True))
print(crayons.magenta('magenta string', bold=True))
print(crayons.white('white string', bold=True))
print(crayons.random('random color'))
print(crayons.random('random and bold', bold=True))
print(crayons.red('red'))
print(crayons.green('green'))
print(crayons.yellow('yellow'))
print(crayons.blue('blue'))
print(crayons.black('black', bold=True))


print(crayons.magenta('magenta'))
print(crayons.cyan('cyan'))
print(crayons.white('white'))
print(crayons.normal('normal'))
print(crayons.clean('{} clean {}'.format(
    crayons.red('red'),
    crayons.blue('blue')
)))
print(red('red'))  # NOQA
print(green('green'))  # NOQA
print(yellow('yellow'))  # NOQA
print(blue('blue'))  # NOQA
print(black('black', bold=True))  # NOQA
print(magenta('magenta'))  # NOQA
print(cyan('cyan'))  # NOQA
print(white('white'))  # NOQA
print(normal('normal'))  # NOQA
print(clean('{} clean {}'.format(red('red'), blue('blue'))))  # NOQA

crayons.replace_colors({'magenta': 'blue'})
print(crayons.magenta('this is blue!'))
crayons.reset_replace_colors()
print(crayons.magenta('this is magenta again!'))
