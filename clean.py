import os


def clean():
    directory = "media/GeeksForGeeks"
    parent_dir = os.path.dirname(os.path.abspath('manage.py'))
    print(parent_dir)
    # Removing Folders





    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    return print("Done")

clean()