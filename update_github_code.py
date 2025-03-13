import os
import requests

# Configuration
GITHUB_USER = "banderson314"
REPOS = [
    {
        "repo_name": "Update_Github_code",
        "files_to_update": ["update_github_code.py"]
    },
    {
        "repo_name": "Convert_OCT_files_to_TIF",
        "files_to_update": [
            "convert_OCT_files.py",
            "convert_OCT_files_imagej_supplement.ijm"
        ]
    }
]
BRANCH = "main"
LOCAL_DIR = "C:/Users/bran314/Desktop/Test"  # Replace with the actual directory where the code is stored

# GitHub API URL for downloading a file from the repository
def get_file_url(repo_name, file_path):
    return f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/{BRANCH}/{file_path}"

def update_specific_files():
    for repo in REPOS:
        repo_name = repo["repo_name"]
        for file_path in repo["files_to_update"]:
            print(f"Downloading {file_path} from {repo_name}...")
            url = get_file_url(repo_name, file_path)
            response = requests.get(url)

            if response.status_code == 200:
                # Write the updated content to the local file
                local_file_path = os.path.join(LOCAL_DIR, repo_name, file_path)
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
                with open(local_file_path, "wb") as file:
                    file.write(response.content)
                print(f"Successfully updated {file_path} from {repo_name}")
            else:
                print(f"Failed to download {file_path} from {repo_name}. HTTP Status Code: {response.status_code}")
                print(response.text)

if __name__ == "__main__":
    update_specific_files()
