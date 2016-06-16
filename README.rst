This app created for find 3 perpendicular for each other lines in cube matrix

Using
=====

This app provide one class which can get 1 not required parameter - matrix size.

    class Matrix

class Matrix has and 2 methods:

    calc_max_sum()
    print_matrix()

first is using for display generated matrix
and second - for start calculation process

Example
=======

    matrix = Matrix()
    matrix.calc_max_sum()

After that you can call

    matrix.result
    
for get result of calculation. result format is x-y-z.x-y-z.x-y-z where 0 show in it is

    0-15-10.5-0-10.5-32-0

also you can check sum for this  result:

    matrix.result_sum
