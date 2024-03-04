a = 5 #(inline comment) this is a instance of an object

"""
This is a block comment
We can add a lot of lines
"""


def f(x):   
    """
    this is a docstring
    A docstring explain what a function does
    :param x:
    :return:
    """
    return x * x #Returns the square of x


for item in 'python':
    #An indented comment
    if item == 'p':
        #Another indented comment
        print('Found!')