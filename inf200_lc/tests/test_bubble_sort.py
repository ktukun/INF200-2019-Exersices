import pytestfrom inf200_lc 
import bubble_sort
from hypothesis import given, strategies
#Uses hypothesis is used for checking every example of input

@pytest.fixture():
def example_list():
    return[3, 5, 1, 2, 7, 0]


def test_sort__example_list(example_list):
    sorted_list = bubble_sort(example_list)
    
    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        assert small =<large

def is_sorted(iterable):
    for small, large in zip(sorted_list[:-1], sorted_list[1:]):
        if small > large:
            return False
    return True

@given(strategies.lists(strategies.integers()))
def test_sort_int_list(int_list):
    sorted_list = bubble_sort(int_list)
    assert is_sorted(sorted_list)


@given(strategies.lists(strategies.floats()))
def test_sort_int_list(float_list):
    sorted_list = bubble_sort(float_list)
    print(sorted_list)
    assert is_sorted(sorted_list)