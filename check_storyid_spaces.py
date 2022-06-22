import import_csv
import pathlib


# Check for spaces after the Story ID
def check_spaces(dcon_folder):
    # Setup
    file = pathlib.Path().joinpath(dcon_folder, "StoryOverrides.csv")
    (headers, rows) = import_csv.import_csv(file)

    # Default Offset for when the Story IDs rows start
    offset = 1

    # Determine the story ID column index
    story_id_col_index = headers.index('identifier')

    print("\nSTARTING STORY ID SPACE CHECK")

    # For each row in rows, check to see if there's a space after the story ID
    for row in rows:
        story_id_to_check = row[story_id_col_index]

        # Debug
        # print("Currently checking " + story_id_to_check)

        # Offset Addition
        if story_id_to_check == "String":
            offset += 1

        # Print Method
        elif story_id_to_check[-1] == " ":
            print("     Row " + str(rows.index(row) + offset) + ": " + story_id_to_check + "has a space at the end.")

    print("STORY ID SPACE CHECK IS COMPLETE")

