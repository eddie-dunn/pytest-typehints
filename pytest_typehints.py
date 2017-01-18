"""Pytest plugin that checks for type hinting."""
# -*- coding: utf-8 -*-

import pytest


def pytest_addoption(parser):
    """Adds typehinting check to pytest"""
    group = parser.getgroup('typehints')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2017',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def typehint(request):
    """Bar"""
    return request.config.option.dest_foo


def test_func_annotations(module, skiplist=None):
    """Code quality: Test that all functions in module have annotations"""
    from inspect import getmembers
    from inspect import isfunction
    from inspect import getfullargspec

    # Modify this to skip certain functions:
    skip_list = skiplist or []

    # failures list will contain all functions without annotations
    failures = []

    def is_function(func):
        """Return True only for objects (funcs) we wish to check"""
        return isfunction(func) and func.__name__ not in skip_list

    def check_annotations(func):
        """Raises AssertionError if args and return value are not annotated."""
        argspec = set(
            getfullargspec(func).args  # pylint: disable=deprecated-method
        )
        argspec.add('return')
        annotations = set(func.__annotations__)
        if not argspec == annotations:
            msg = "Function '{}' missing annotations for {}".format(
                func.__name__, sorted(argspec - annotations))
            failures.append(msg)

    # From http://stackoverflow.com/a/9794849/955014:
    funcs = [o[1] for o in getmembers(module) if is_function(o[1])]
    for func in funcs:
        check_annotations(func)

    if any(failures):
        msg = '\n'.join(failures)
        raise AssertionError("Missing annotations:\n{}".format(msg))
