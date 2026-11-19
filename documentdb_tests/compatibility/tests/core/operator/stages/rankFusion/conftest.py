"""Every test in this folder covers behavior added in spec 8.2.

The $rankFusion stage is on by default from MongoDB 8.1; an 8.0 server
rejects it unless a feature flag is set.
"""

from documentdb_tests.framework.preconditions import spec_gate_folder

pytest_collection_modifyitems = spec_gate_folder(__file__, spec_since="8.2")
