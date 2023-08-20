import requests
from superagi.tools.base_tool import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class SimplyHiredJobSearchInput(BaseModel):
    keywords: str = Field(..., description="Keywords for job search")
    location: str = Field(..., description="Location for job search")

class SimplyHiredJobSearchTool(BaseTool):
    name: str = "SimplyHired Job Search Tool"
    args_schema: Type[BaseModel] = SimplyHiredJobSearchInput
    description: str = "Tool for searching job listings using the SimplyHired API"

    def _execute(self, keywords: str, location: str):
        # SimplyHired API endpoint for job search
        api_url = "https://api.simplyhired.com/a/jobroll"

        # Query parameters for the job search
        params = {
            "q": keywords,
            "l": location,
            "pshid": "YOUR_PUBLISHER_ID",  # Replace with your actual publisher ID
        }

        response = requests.get(api_url, params=params)
        job_listings = response.json()

        # Return the job listings
        return job_listings

# Usage example
simplyhired_tool = SimplyHiredJobSearchTool()
job_listings = simplyhired_tool.execute(keywords="software engineer", location="San Francisco")
print(job_listings)  # Print the returned job listings
