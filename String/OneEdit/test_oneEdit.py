import pytest
from oneEdit import oneEdit

def test_strings_are_equal():
    print("Test Case: Strings are equal ('hello', 'hello')")
    assert oneEdit("hello", "hello")
    print("Passed: Strings are equal")

def test_one_replacement():
    print("Test Case: One replacement ('hello', 'hollo')")
    assert oneEdit("hello", "hollo")
    print("Passed: One replacement ('hello', 'hollo')")

    print("Test Case: One replacement ('abc', 'adc')")
    assert oneEdit("abc", "adc")
    print("Passed: One replacement ('abc', 'adc')")

def test_one_addition():
    print("Test Case: One addition ('abc', 'abdc')")
    assert oneEdit("abc", "abdc")
    print("Passed: One addition ('abc', 'abdc')")

    print("Test Case: One addition ('hello', 'helllo')")
    assert oneEdit("hello", "helllo")
    print("Passed: One addition ('hello', 'helllo')")

def test_one_removal():
    print("Test Case: One removal ('abc', 'ac')")
    assert oneEdit("abc", "ac")
    print("Passed: One removal ('abc', 'ac')")

    print("Test Case: One removal ('hello', 'helo')")
    assert oneEdit("hello", "helo")
    print("Passed: One removal ('hello', 'helo')")

def test_more_than_one_edit():
    print("Test Case: More than one edit ('hello', 'world')")
    assert not oneEdit("hello", "world")
    print("Passed: More than one edit ('hello', 'world')")

    print("Test Case: More than one edit ('abc', 'xyz')")
    assert not oneEdit("abc", "xyz")
    print("Passed: More than one edit ('abc', 'xyz')")

def test_edge_cases():
    print("Test Case: Edge case ('a', 'b')")
    assert oneEdit("a", "b")
    print("Passed: Edge case ('a', 'b')")

    print("Test Case: Edge case ('', 'a')")
    assert oneEdit("", "a")
    print("Passed: Edge case ('', 'a')")

    print("Test Case: Edge case ('', 'ab')")
    assert not oneEdit("", "ab")
    print("Passed: Edge case ('', 'ab')")

    print("Test Case: Edge case ('a', 'abc')")
    assert not oneEdit("a", "abc")
    print("Passed: Edge case ('a', 'abc')")