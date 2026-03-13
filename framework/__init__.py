"""
Reusable testing framework for DocumentDB functional tests.

This framework provides:
- Assertion helpers for common test scenarios
- Fixture utilities for test isolation and database management
"""
from framework.executor import execute_command
from framework.assertions import assertSuccess, assertFailure

__all__ = ["execute_command", "assertSuccess", "assertFailure"]
