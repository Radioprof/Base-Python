import os
import yaml


def new_starter(dir_def, r=''):
    for root, _a in dir_def.items():
        sbdir = os.path.join(r, root)
        if not os.path.exists(sbdir):
            os.mkdir(sbdir)
        if isinstance(_a, dict):
            new_starter(_a, sbdir)
        elif isinstance(_a, list):
            for list_item in _a:
                if isinstance(list_item, dict):
                    new_starter(list_item, sbdir)
                elif isinstance(list_item, str):
                    with open(os.path.join(sbdir,list_item), 'w') as f:
                        pass
                else: continue


with open('config.yaml') as list_1:
    dir_path = yaml.safe_load(list_1)
    new_starter(dir_path)
