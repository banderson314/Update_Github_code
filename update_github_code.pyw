import os
import requests
import tkinter as tk
from tkinter import messagebox

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

# Get the current directory where the script is located
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))

# GitHub API URL for downloading a file from the repository
def get_file_url(repo_name, file_path):
    return f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/{BRANCH}/{file_path}"

def update_specific_files():
    update_success = True
    for repo in REPOS:
        repo_name = repo["repo_name"]
        for file_path in repo["files_to_update"]:
            print(f"Downloading {file_path} from {repo_name}...")
            url = get_file_url(repo_name, file_path)
            response = requests.get(url)

            if response.status_code == 200:
                # Write the updated content to the local file
                local_file_path = os.path.join(LOCAL_DIR, file_path)
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
                with open(local_file_path, "wb") as file:
                    file.write(response.content)
                print(f"Successfully updated {file_path} from {repo_name}")
            else:
                print(f"Failed to download {file_path} from {repo_name}. HTTP Status Code: {response.status_code}")
                print(response.text)
                update_success = False

    return update_success

def show_update_complete_dialog(update_success):
    """Shows a dialog to inform the user that the update is complete."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    if update_success:
        messagebox.showinfo("Update Complete", "The repositories were successfully updated.")
    else:
        messagebox.showerror("Update Failed", "Some repositories failed to update.")
    
    root.quit()

if __name__ == "__main__":
    update_success = update_specific_files()
    show_update_complete_dialog(update_success)
