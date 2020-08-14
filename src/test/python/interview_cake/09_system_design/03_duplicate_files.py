"""
# Duplicate files

## Problem statement

You left your computer unlocked and your friend decided to troll you by copying
 a lot of your files
to random spots all over your file system.

Even worse, she saved the duplicate files with random, embarrassing names
("this_is_like_a_digital_wedgie.txt" was clever, I'll give her that).

Write a function that returns a list of all the duplicate files. We'll check 
them by hand before
actually deleting them, since programmatically deleting files is really scary. 
To help us confirm that two files are actually duplicates, 
return a list of tuples where:

    the first item is the duplicate file
    the second item is the original file

For example:

[
  ('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'), 
  ('/home/trololol.mov', '/etc/apache2/httpd.conf')]

You can assume each file was only duplicated once.

---

## Solution

Brute force

O(n ^ 2)

- Walk through the file system 
- Store all the paths in a list
- Compare each path with other paths in the list and if file are equal then 
  add it to dups_list
- Exit when the outer loop reaches the end

Optimization

O(n)

- Walk through the file system 
- Store each file and content in a dict
- For every new file check if the file is already in the dict
  - If yes, then we have a duplicate, add it to the dups list
    - To determine if file is dups, we can use the created_at time for the file
  - Else add the file to dict
- Return the dups list at the end
"""

import os


def find_duplicate_files(starting_directory):
    files_already_seen = {}
    stack = [starting_directory]
    duplicates = []

    while len(stack) > 0:
        current_path = stack.pop()

        # if file is a directory then put the path in stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)
        # it's a file
        else:
            # Get the file contents
            with open(current_path) as file:
                file_contents = file.read()

            # Get file's last edited time
            current_last_edited_time = os.path.getmtime(current_path)

            # If we've seen it before
            if file_contents in files_already_seen:
                existing_last_edited_time, existing_path = files_already_seen[
                    file_contents
                ]

                if current_last_edited_time > existing_last_edited_time:
                    # current file is the dup
                    duplicates.append((current_path, existing_path))
                else:
                    # existing file is the dup
                    duplicates.append((existing_path, current_path))
                    # update files already seen
                    files_already_seen[file_contents] = (
                        current_last_edited_time,
                        current_path,
                    )
            # If its a new file then add it to files_already_seen
            # along with the last edited time so that we can delete it later
            # if its a dup
            else:
                files_already_seen[file_contents] = (
                    current_last_edited_time,
                    current_path,
                )

    return duplicates
