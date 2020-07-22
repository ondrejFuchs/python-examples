# Readme to completed tests

Sometimes it was necessary to **import** parts into the code, but in the readme I understood that this is not forbidden (often it was necessary).

### 1. Make the tests pass

Script ```test_ex1.py``` was tested by command ```$ pytest test_ex1.py```.

### 2. Implement the description

Script ```decorators.py``` was tested by my own tests in ```tests/test_decorators.py```(I did not find a specification for it.). Script ```tests/test_decorators.py``` is executable and there are used __count_calls__ and __memorize__ decorators with functions for count rectangular area and cube content. 

- count_calls test: The number of calls for ```count_rectangular``` func varies depending on the generated random number. 

- memorize test: Three cube dimensions were defined. The content is calculated for all and then the whole output is checked with the expected one.


```
...
FIRST = [1,2,3]
SECOND = [2,3,4]
THIRD = [10,20,30]
...
# Output format:
# (count_cube calls: content)
expected_output = "{1: 6, 2: 24, 3: 6000}"
...

```

In script is also used ```add``` function with the similar tests as with the ```count_cube``` func = function is called three times with pre-defined parameters and output is checked.

### 3. Make the tests pass

Script ```test_ex2.py``` was tested by command ```$ pytest test_ex2.py```. Solution was to write the appropriate logic.

### 4. Make the doctests pass

Script ```dataclasses_exercises.py``` was tested by ```python3  -m doctest -v dataclasses_exercises.py```

Line ```DIR = Path(__file__).parent``` return relative path of file, so problem was that ```EnsureInitExist(DIR)``` and ```EnsureInitExist(DIR.parrent)``` returned the same results. 

### 5. Implement the fixture and tests and implement the code in wheelme_lines.py.

Script ```test_ex4.py``` was tested by command ```$ pytest test_ex4.py``` and ```wheelme_lines.py``` script was tested by ```python3  -m doctest -v wheelme_lines.py```.

In script ```wheelme_lines.py``` was also changed import Iterable from collections to collections.abs because of **"DeprecationWarning"**. I also created class SubKafka, which is subclass of Kafka class to by able to use Kafka abstractmethod ```produce```.

In script ```test_ex4.py``` I created other two dict (lines1, lines2) for ```pytest.mark.parametrize``` needs.

### 6. Make the test pass and doctests in immutable_class.py

Script ```test_ex5.py``` was tested by command ```$ pytest test_ex5.py``` and ```immutable_class.py``` with command ```$ python3  -m doctest -v immutable_class.py```.

### 7. Make the tests pass

Scripts was tested by command ```$ pytest test_ex6.py```. 