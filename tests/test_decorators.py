from ex1.decorators import count_calls, memorize, add
import logging
import random

### Cubes dimensions
FIRST = [1,2,3]
SECOND = [2,3,4]
THIRD = [10,20,30]

def generate_random_int():
    """ Func for generate random int 

    Function for count rectangular area for demonstration of decorators

    Returns:
       int: random integer in range 0 to 10 

    """
    return random.randint(0, 10)


@count_calls
def count_rectangular(a, b):
    """ Func for count rectangular area

    Function for count rectangular area for demonstration of decorators

    Args:
       a (int): length of side a
       b (int): length of side b

    Returns:
       int: area of rectangular

    """
    
    return a * b
    
@memorize
@count_calls
def count_cube(a, b, c):
    """ Func for count cube content

    Function for count cube content for demonstration of decorators

    Args:
       a (int): length of side a
       b (int): length of side b
       c (int): length of side c

    Returns:
       int: cube content

    """

    return a * b * c
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s\t%(levelname)s\t%(message)s')

    # Get random num for tests
    set_calls = generate_random_int()
    
    # Test count_calls decorator                  
    for i in range(set_calls):
        # For tests it does not matter length of sides
        count_rectangular(generate_random_int(), generate_random_int())

    if count_rectangular.calls ==  set_calls:
        logging.info("Real_calls: {}, set_calls: {} - OK".format(count_rectangular.calls, set_calls))
    else:
        logging.error("Real_calls: {} and set_calls: {} are not the same.".format(count_rectangular.calls, set_calls))
        exit(1)
    
    # Count cubes content
    count_cube(FIRST[0],FIRST[1],FIRST[2])
    count_cube(SECOND[0],SECOND[1],SECOND[2])
    count_cube(THIRD[0],THIRD[1],THIRD[2])

    # Output format:
    # (count_cube calls: content)
    expected_output = "{1: 6, 2: 24, 3: 6000}"
    
    if str(count_cube.mem) == expected_output:
        logging.info("Result (count_cube calls: content): {} - OK".format(count_cube.mem))
    else:
        logging.error("Result: {} is not as expected {}".format(count_cube.mem, expected_output))
        exit(1)
    
    # Tests with add function
    add(0,1)
    add(1,2)
    add(2,3)
    
    expected_output = "{1: 1, 2: 3, 3: 5}"
    
    if str(add.mem) == expected_output:
        logging.info("Result (count_cube calls: sum): {} - OK".format(add.mem))
    else:
        logging.error("Result: {} is not as expected {}".format(add.mem, expected_output))
        exit(1)
        
    