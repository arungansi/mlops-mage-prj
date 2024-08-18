import os
from tempfile import TemporaryDirectory
from git import Repo

with TemporaryDirectory() as tmp_dir:
	target_dir = tmp_dir
repo_url = 'https://github.com/mage-ai/mage-ai-terraform-templates.git'
if not os.path.isdir(target_dir):
    os.makedirs(target_dir, exist_ok=True)
print(repo_url,target_dir)
Repo.clone_from(repo_url, target_dir)