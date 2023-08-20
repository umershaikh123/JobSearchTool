from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List

from JoobleJobSearch import JoobleJobSearchTool
from CareerjetJobSearch import CareerjetJobSearchTool
from SimplyHiredJobSearch import SimplyHiredJobSearchTool
from GitHubJobSearch import GitHubJobSearchTool

class JobSearchToolkit(BaseToolkit):
    name: str = "Job Search Toolkit"
    description: str = "Toolkit for searching job listings from various platforms"

    def get_tools(self) -> List[BaseTool]:
        # Return instances of your job searching tool classes
        return [
            JoobleJobSearchTool(),
            CareerjetJobSearchTool(),
            SimplyHiredJobSearchTool(),
            GitHubJobSearchTool(),
            # Add more tools as needed
        ]

    def get_env_keys(self) -> List[str]:
        # Return a list of environment variable keys required by your toolkit
        return []