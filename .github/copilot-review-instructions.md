# Copilot Review Instructions

## 1. Test Coverage Completeness

- Check every test file against the rules in `docs/testing/TEST_COVERAGE.md`.
- Verify that all applicable rules have corresponding test cases for the feature under test.
- Cross-reference claimed gaps against shared constants in `framework/test_constants.py` — values like `DOUBLE_HALF`, `DECIMAL128_NEGATIVE_ONE_AND_HALF`, `INT32_MAX`, etc. may already cover cases that appear missing at first glance.
- Flag any test category from the checklist in TEST_COVERAGE.md that has no corresponding test.

## 2. Folder Structure

Read `docs/testing/FOLDER_STRUCTURE.md` and check every test file against all rules. Apply BOTH directions:

1. **Feature isolation**: A feature folder (e.g., `/cond/`) must ONLY test that feature's own behavior (edge cases, self-nesting). Any test exercising another operator belongs in the parent folder.
2. **Meaningful cross-tests only**: Only MEANINGFUL same-level cross-tests belong in the parent folder — ones where the combination produces different or interesting behavior.
   - **Meaningful**: `{$dateFromString: {$dateToString: $date}}` (roundtrip), `{$subtract: [2, 1]} == {$add: [2, -1]}` (equivalence).
   - **Not meaningful**: `{$add: [{$cond: ...}, 5]}` (just passing a value — `$cond` returns a number, `$add` adds it, no interesting interaction).

## 3. Test Format

- Check every test file against the rules in `docs/testing/TEST_FORMAT.md`.
- Verify test functions follow the setup/execute/assert pattern.
- Verify parametrized test cases use shared constants where applicable.
- Flag new helpers that over-abstract — test cases should remain readable without needing to trace through multiple layers of indirection. New helpers must not contradict `docs/testing/TEST_FORMAT.md` rules.

## 4. Redundancy and Duplication

- Flag any test case that is redundant or duplicates another test case in the same file or across files in the same feature folder.
- Check if a test case is already covered by shared parametrized constants.

## 5. Documentation Updates

- If the PR introduces new test patterns or coverage rules, verify that `docs/testing/TEST_COVERAGE.md` is updated accordingly.
