import unittest
from superagi.testing import BaseToolTestCase
from GitHubJobSearch import GitHubJobSearchTool

class TestGitHubJobSearchTool(BaseToolTestCase):
    tool_class = GitHubJobSearchTool

    def test_job_search(self):
        job_listings = self.execute_tool(
            description="software engineer",
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
            description="nonexistent_keyword",
            location="Nonexistent_City"
        )
        self.assertIsNotNone(job_listings)
        self.assertIsInstance(job_listings, list)
        self.assertEqual(len(job_listings), 0)

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
