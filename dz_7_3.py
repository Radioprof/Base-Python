import os
import shutil

try:
    root_dir = 'my_project'
    for root, dir, file in os.walk(root_dir):
            if root.endswith('templates') and not root.startswith(os.path.join(root_dir, 'templates')):
                for i in dir:
                    shutil.copytree(os.path.join(root, i), os.path.join(root_dir, 'templates', i))
except FileExistsError:
    print("Папка уже существует")