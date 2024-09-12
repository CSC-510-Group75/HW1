import pytest
import hw2_debugging.py as hw2_debugging.py
def testempty():
    input_arr = []
    expected_output = []
    assert merge_sort(input_arr) == expected_output, f"Failed for input {input_arr}"
