import os
import subprocess

# Define the path to the folder containing all the git repos
git_folder = os.path.expanduser('~/git')

# Iterate over each item in the git folder
for item in os.listdir(git_folder):
    item_path = os.path.join(git_folder, item)
    
    # Check if the item is a directory and a git repo
    if os.path.isdir(item_path) and os.path.isdir(os.path.join(item_path, '.git')):
        # Change the current working directory to the git repo
        os.chdir(item_path)
        
        # Print the name of the git repo
        print(f"**************************************************************************")

        # Print the name of the git repo
        print(f"Working on git repo: {item}")
        
        # Run 'git fetch --all --prune' command
        subprocess.run(['git', 'fetch', '--all', '--prune'])
        
        # Run 'git pull' command
        subprocess.run(['git', 'pull'])