from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from selenium import webdriver
import requests
 

class GitHubJobSearchInput(BaseModel):
    description: str = Field(..., description="Keywords for job search")
    location: str = Field(..., description="Location for job search")

class GitHubJobSearchTool(BaseTool):
    name: str = "GitHub Job Search Tool"
    args_schema: Type[BaseModel] = GitHubJobSearchInput
    description: str = "Tool for searching job listings on GitHub Jobs"

    def _execute(self, description: str, location: str):
        # GitHub Jobs API endpoint for job search
        api_url = "https://jobs.github.com/positions.json"

        # Query parameters for the job search
        params = {
            "description": description,
            "location": location,
        }

        response = requests.get(api_url, params=params)
        job_listings = response.json()

        # Return the job listings
        return job_listings            

# Usage example
github_tool = GitHubJobSearchTool()
github_tool.execute(description="software engineer", location="San Francisco")
print(job_listings)  # Print the returned job listings





# # Process and display job listings
# for job in job_listings:
#     print(f"Job Title: {job['title']}")
#     print(f"Company: {job['company']}")
#     print(f"Location: {job['location']}")
#     print("--------")
 