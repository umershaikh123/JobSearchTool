import unittest
from unittest.mock import patch, MagicMock
from GitHubJobSearch import GitHubJobSearchTool

class TestGitHubJobSearchTool(unittest.TestCase):
    def setUp(self):
        self.github_tool = GitHubJobSearchTool()

    @patch("GitHubJobSearch.requests.get")
    def test_job_search(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {"title": "Software Engineer", "company": "Example Inc."},
            # Add more mock data as needed
        ]
        mock_get.return_value = mock_response

        job_listings = self.github_tool._execute(
            description="software engineer",
            location="San Francisco"
        )

        self.assertIsNotNone(job_listings)
        self.assertIsInstance(job_listings, list)
        self.assertTrue(len(job_listings) > 0)
        self.assertTrue(all("title" in job for job in job_listings))
        self.assertTrue(all("company" in job for job in job_listings))
        # Add more assertions as needed

    @patch("GitHubJobSearch.requests.get")
    def test_empty_results(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        job_listings = self.github_tool._execute(
            description="nonexistent_keyword",
            location="Nonexistent_City"
        )

        self.assertIsNotNone(job_listings)
        self.assertIsInstance(job_listings, list)
        self.assertEqual(len(job_listings), 0)

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
