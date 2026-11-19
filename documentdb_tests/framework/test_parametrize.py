"""Unit tests for the parametrize helpers (no database needed)."""

import pytest

from documentdb_tests.framework.parametrize import with_marks

_GATE = pytest.mark.requires(spec_since="8.2")


@pytest.mark.unit
class TestWithMarks:
    def test_adds_marks_to_named_params_only(self):
        params = [pytest.param(1, id="a"), pytest.param(2, id="b", marks=pytest.mark.smoke)]
        a, b = with_marks(params, ["b"], _GATE)
        assert a is params[0]
        assert (b.values, b.id) == ((2,), "b")
        assert [m.name for m in b.marks] == ["smoke", "requires"]

    def test_unknown_id_raises(self):
        with pytest.raises(ValueError, match="no param with id"):
            with_marks([pytest.param(1, id="a")], ["b"], _GATE)
