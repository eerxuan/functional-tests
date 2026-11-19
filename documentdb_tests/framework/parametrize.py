"""Pytest parametrize helpers for building test parameter lists."""

from collections.abc import Iterable, Sequence
from typing import Any

import pytest

from documentdb_tests.framework.test_case import BaseTestCase


def pytest_params(tests: Sequence[BaseTestCase]):
    """Build pytest parameters from a sequence of test cases, using each case's id.

    Passes through any pytest marks defined on individual test cases.
    """
    return [pytest.param(t, id=t.id, marks=t.marks) for t in tests]


def with_marks(params: Sequence[Any], ids: Iterable[str], *marks: Any) -> list[Any]:
    """Return ``params`` with ``marks`` added to the params whose id is in ``ids``.

    For parameter lists built by a generator that cannot carry per-case marks
    (e.g. the BSON type helpers). Raises if an id matches no param, so a renamed
    case cannot silently lose its marks.
    """
    wanted = set(ids)
    missing = wanted - {p.id for p in params}
    if missing:
        raise ValueError(f"no param with id {sorted(missing)}")
    return [
        pytest.param(*p.values, id=p.id, marks=(*p.marks, *marks)) if p.id in wanted else p
        for p in params
    ]
