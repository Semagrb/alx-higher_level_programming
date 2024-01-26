#!/usr/bin/python3
"""
Lists the 10 most recent commits on a specified GitHub repository.

Usage: ./100-github_commits.py <repository owner> <repository name>
"""

import sys
import requests

if __name__ == "__main__":
    # Check if both repository owner and name are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository owner> <repository name>")
    else:
        # Construct the URL for GitHub API to fetch commits for the specified repository
        url = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"

        # Send a GET request to the GitHub API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response into a list of commits
            commits = response.json()

            # Display the details of the 10 most recent commits
            for commit in commits[:10]:
                commit_sha = commit.get("sha")
                commit_author = commit.get("commit").get("author").get("name")
                print(f"{commit_sha}: {commit_author}")
        else:
            # Display an error message if the request was not successful
            print(f"Error: Unable to fetch commits. Status code: {response.status_code}")
