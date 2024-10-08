import hw2_debugging

def test_merge_sort():
    assert hw2_debugging.merge_sort([15, 8, 12, 6, 17, 10, 15, 18, 1, 9, 9, 2, 19, 11, 8, 9, 1, 6, 1, 12]) == [1, 1, 1, 2, 6, 6, 8, 8, 9, 9, 9, 10, 11, 12, 12, 15, 15, 17, 18, 19]
    assert hw2_debugging.merge_sort([13, 8, 5, 6, 10, 5, 14, 1, 11, 6, 13, 13, 8, 10, 12, 17, 10, 5, 2, 8]) == [1, 2, 5, 5, 5, 6, 6, 8, 8, 8, 10, 10, 10, 11, 12, 13, 13, 13, 14, 17]
    assert hw2_debugging.merge_sort([8, 20, 14, 13, 5, 7, 9, 2, 3, 17, 17, 3, 9, 14, 1, 19, 18, 3, 6, 7]) == [1, 2, 3, 3, 3, 5, 6, 7, 7, 8, 9, 9, 13, 14, 14, 17, 17, 18, 19, 20]