import requests
from superagi.tools.base_tool import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class JoobleJobSearchInput(BaseModel):
    keywords: str = Field(..., description="Keywords for job search")
    location: str = Field(..., description="Location for job search")

class JoobleJobSearchTool(BaseTool):
    name: str = "Jooble Job Search Tool"
    args_schema: Type[BaseModel] = JoobleJobSearchInput
    description: str = "Tool for searching job listings using the Jooble API"

    def _execute(self, keywords: str, location: str):
        # Jooble API endpoint for job search
        api_url = "https://us.jooble.org/api/jobs"

        # Query parameters for the job search
        params = {
            "keywords": keywords,
            "location": location,
            "partnerid": "YOUR_PARTNER_ID",  # Replace with your actual partner ID
        }

        response = requests.get(api_url, params=params)
        job_listings = response.json()

        # Return the job listings
        return job_listings

# Usage example
jooble_tool = JoobleJobSearchTool()
job_listings = jooble_tool.execute(keywords="software engineer", location="San Francisco")
print(job_listings)  # Print the returned job listings
