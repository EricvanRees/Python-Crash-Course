'''Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file,
and call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''

import sandwiches
from sandwiches import make_sandwich
from sandwiches import make_sandwich as msw
import sandwiches as sw
from sandwiches import *

make_sandwich('ham', 'cheese', 'bacon')
make_sandwich('pepperoni', 'ham', 'butter')
make_sandwich('pindakaas', 'hagelslag', 'boter')

