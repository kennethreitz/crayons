"""Simple test of just running the README example. Better tests to come."""

from __future__ import print_function
import crayons
from crayons import *

print(crayons.red('red string'))
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))
crayons.disable()
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))
crayons.enable()
print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))
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
print(crayons.clean('{} clean {}'.format(crayons.red('red'), crayons.blue('blue'))))
print(red('red'))
print(green('green'))
print(yellow('yellow'))
print(blue('blue'))
print(black('black', bold=True))
print(magenta('magenta'))
print(cyan('cyan'))
print(white('white'))
print(normal('normal'))
print(clean('{} clean {}'.format(red('red'), blue('blue'))))

crayons.replace_colors({'magenta': 'blue'})
print(crayons.magenta('this is blue!'))
crayons.reset_replace()
print(crayons.magenta('this is magenta again!'))
