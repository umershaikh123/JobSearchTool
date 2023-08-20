import unittest
from superagi.testing import BaseToolTestCase
from SimplyHiredJobSearch import SimplyHiredJobSearchTool

class TestSimplyHiredJobSearchTool(BaseToolTestCase):
    tool_class = SimplyHiredJobSearchTool

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

    def test_api_working(self):
        # Test if the API is accessible and returns a successful response
        job_listings = self.execute_tool(
            keywords="software engineer",
            location="San Francisco"
        )
        self.assertIsNotNone(job_listings)
        self.assertIsInstance(job_listings, list)
        self.assertTrue(len(job_listings) > 0)

if __name__ == "__main__":
    unittest.main()
