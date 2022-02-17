# how would I test Barky?
# First, I wouldn't test barky, I would test the reusable modules barky relies on:
# commands.py and database.py

# we will use pytest: https://docs.pytest.org/en/stable/index.html

# should we test quit? No, its behavior is self-evident and not logic dependent  ``
from barky import *

import commands
import pytest


def test_quit_command():
    pass

def test_option_choice_is_valid():
    #This is the arrange step from barky.py
    options = {
        "A": Option(
            "Add a bookmark",
            commands.AddBookmarkCommand(),
            prep_call=get_new_bookmark_data,
        ),
        "B": Option("List bookmarks by date", commands.ListBookmarksCommand()),
        "T": Option(
            "List bookmarks by title", commands.ListBookmarksCommand(order_by="title")
        ),
        "E": Option(
            "Edit a bookmark",
            commands.EditBookmarkCommand(),
            prep_call=get_new_bookmark_info,
        ),
        "D": Option(
            "Delete a bookmark",
            commands.DeleteBookmarkCommand(),
            prep_call=get_bookmark_id_for_deletion,
        ),
        "G": Option(
            "Import GitHub stars",
            commands.ImportGitHubStarsCommand(),
            prep_call=get_github_import_options,
        ),
        "Q": Option("Quit", commands.QuitCommand()),
    }
    choice = "J"
    
    #This is act
    result = option_choice_is_valid(choice, options)

    #This is assert
    assert result

# okay, should I test the other commands?
# not really, they are tighly coupled with sqlite3 and its use in the database.py module
