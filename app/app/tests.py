"""
Sample tests
"""

from django.test import SimpleTestCase

from . import calc


class ClacTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
