# test_computelink.py
"""
Tests for ComputeLink module.
"""

import unittest
from computelink import ComputeLink

class TestComputeLink(unittest.TestCase):
    """Test cases for ComputeLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ComputeLink()
        self.assertIsInstance(instance, ComputeLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ComputeLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
