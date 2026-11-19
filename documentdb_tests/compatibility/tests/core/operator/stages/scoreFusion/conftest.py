"""Every test in this folder covers behavior added in spec 8.2.

The $scoreFusion stage is new in MongoDB 8.2.
"""

from documentdb_tests.framework.preconditions import spec_gate_folder

pytest_collection_modifyitems = spec_gate_folder(__file__, spec_since="8.2")
