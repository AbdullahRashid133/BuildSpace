# test_buildspace.py
"""
Tests for BuildSpace module.
"""

import unittest
from buildspace import BuildSpace

class TestBuildSpace(unittest.TestCase):
    """Test cases for BuildSpace class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BuildSpace()
        self.assertIsInstance(instance, BuildSpace)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BuildSpace()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
