from sort_final import sortFunction
import pytest


def test_sort_function():
    """This function will test the sortFuntion() to review
    if it returns a list sorted correctly.
    It will call the sortFunction with the no-sorted list as
    argument and then compare it with a expected sorted list
    if both lists area the same it will pass the test.
    It takes no parameters.
    """
    # list without sorting
    list1 = [
        "Python",
        "C++",
        "Java",
        "C#",
        "Swift",
        "JavaScript",
        "PHP",
        "C",
        "Perl",
        "VB",
        "Kotlin"
    ]
    # call the sortFunciont(), use list1 as argument
    sortFunction(list1)

    # expected sorted list
    sorted_list = [
        "C",
        "C#",
        "C++",
        "Java",
        "JavaScript",
        "Kotlin",
        "PHP",
        "Perl",
        "Python",
        "Swift",
        "VB",

    ]

    # once list1 is sorted compare if both lists are the same
    assert list1 == sorted_list, "Lists are not the same."


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
