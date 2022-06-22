import os
import pathlib
import check_loc_stories_priority
import check_profile_names
import check_storyid_spaces


# Checkers List. Add to this list if we need more proofreading scripts
def checkers():
    possible_checks = {
        "loc_stories_priority": check_loc_stories_priority.localization_priority,
        "profile_names": check_profile_names.check_profile_names,
        "storyid_spaces": check_storyid_spaces.check_spaces
    }
    return possible_checks


# Ask User for which DCON to check
def query_dcon_folder():
    dcon_number = int(input("Enter the DCON Number: "))
    return dcon_number


# Ask user for which checker(s) to check
def query_checkers():
    possible_checks = checkers()
    queried_checks = []

    for check in possible_checks:
        query = str(input("Do you wish to run " + check + "? y/n: "))
        if query == "y":
            queried_checks.append(check)
        else:
            print("Skipped. Moving to next checker.")

    return queried_checks


# Find the right DCON folder based on the passed-in DCON number
def find_dcon_folder(dcon_number):
    final_dir = ""
    dcon_number_string = str(dcon_number)
    working_dir_path = pathlib.Path().resolve().parent
    working_dir = os.listdir(working_dir_path)

    for item in working_dir:
        item_string = str(item)
        if os.path.isdir(pathlib.Path().joinpath(working_dir_path, item_string)):
            if dcon_number_string in item_string:
                final_dir = pathlib.Path().joinpath(working_dir_path, item_string)

    return final_dir


# Determine which checker(s) were queried and run them
def run_checkers(queried_checks, dcon_folder):
    possible_checks = checkers()
    for check in queried_checks:
        possible_checks[check](dcon_folder)
    print("\nALL CHECKS FINISHED.")


if __name__ == '__main__':
    DCON = query_dcon_folder()
    CHECKERS = query_checkers()
    DCON_FOLDER = find_dcon_folder(DCON)
    run_checkers(CHECKERS, DCON_FOLDER)
