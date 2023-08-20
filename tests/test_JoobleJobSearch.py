import unittest
from superagi.testing import BaseToolTestCase
from JoobleJobSearch import JoobleJobSearchTool

class TestJoobleJobSearchTool(BaseToolTestCase):
    tool_class = JoobleJobSearchTool

    def test_job_search(self):
        job_listings = self.execute_tool(
            keywords="software engineer",
            location="San Francisco"
        )
        self.assertIsNotNone(job_listings)
        self.assertIsInstance(job_listings, list)
        self.assertTrue(len(job_listings) > 0)
        self.assertTrue(all("title" in job for job in job_listings))
        self.assertTrue(all("company" in job for job in job_listings))
        # Add more assertions as needed

    def test_empty_results(self):
        job_listings = self.execute_tool(
            keywords="nonexistent_keyword",
            location="Nonexistent_City"
        )
        self.assertIsNotNone(job_listings)
        self.assertIsInstance(job_listings, list)
        self.assertEqual(len(job_listings), 0)

    def test_invalid_location(self):
        with self.assertRaises(ValueError):
            self.execute_tool(
                keywords="software engineer",
                location=""
            )

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
