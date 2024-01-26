#!/usr/bin/python3
"""
Lists the 10 most recent commits on a specified GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""

import sys
import requests

if __name__ == "__main__":
    # Check if both repository name and owner are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <repository owner>")
    else:
        # Construct the URL for GitHub API to fetch commits for the specified repository
        url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

        # Send a GET request to the GitHub API
        response = requests.get(url)

        # Parse the JSON response into a list of commits
        commits = response.json()

        # Display the details of the 10 most recent commits
        try:
            for i in range(10):
                commit_sha = commits[i].get("sha")
                commit_author = commits[i].get("commit").get("author").get("name")
                print("{}: {}".format(commit_sha, commit_author))
        except IndexError:
            # Handle the case where there are fewer than 10 commits
            pass
