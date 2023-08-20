import requests
from superagi.tools.base_tool import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class AdzunaJobSearchInput(BaseModel):
    keywords: str = Field(..., description="Keywords for job search")
    location: str = Field(..., description="Location for job search")

class AdzunaJobSearchTool(BaseTool):
    name: str = "Adzuna Job Search Tool"
    args_schema: Type[BaseModel] = AdzunaJobSearchInput
    description: str = "Tool for searching job listings using the Adzuna API"

    def _execute(self, keywords: str, location: str):
        # Replace 'YOUR_APP_ID' and 'YOUR_APP_KEY' with your actual Adzuna API credentials
        app_id = '89a99c52'
        app_key = '3e4f21e3a38452b165e3bc6cb4d5df66'

        # Adzuna API endpoint for job search
        api_url = "https://api.adzuna.com/v1/api/jobs/us/search/1"

        # Query parameters for the job search
        params = {
            "app_id": app_id,
            "app_key": app_key,
            "what": keywords,
            "where": location,
        }

        response = requests.get(api_url, params=params)
        job_listings = response.json()

        # Return the job listings
        return job_listings

# Usage example
adzuna_tool = AdzunaJobSearchTool()
job_listings = adzuna_tool.execute(keywords="software engineer", location="San Francisco")
print(job_listings)  # Print the returned job listings
