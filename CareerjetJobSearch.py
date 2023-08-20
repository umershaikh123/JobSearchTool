import requests
from superagi.tools.base_tool import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class CareerjetJobSearchInput(BaseModel):
    keywords: str = Field(..., description="Keywords for job search")
    location: str = Field(..., description="Location for job search")

class CareerjetJobSearchTool(BaseTool):
    name: str = "Careerjet Job Search Tool"
    args_schema: Type[BaseModel] = CareerjetJobSearchInput
    description: str = "Tool for searching job listings using the Careerjet API"

    def _execute(self, keywords: str, location: str):
        # Careerjet API endpoint for job search
        api_url = "https://public.api.careerjet.net/search"

        # Query parameters for the job search
        params = {
            "keywords": keywords,
            "location": location,
            "affid": "YOUR_AFFILIATE_ID",  # Replace with your actual affiliate ID
        }

        response = requests.get(api_url, params=params)
        job_listings = response.json()

        # Return the job listings
        return job_listings

# Usage example
careerjet_tool = CareerjetJobSearchTool()
job_listings = careerjet_tool.execute(keywords="software engineer", location="San Francisco")
print(job_listings)  # Print the returned job listings
