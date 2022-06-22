import import_csv
import pathlib


def localization_priority(dcon_folder):
    # Setup
    file = pathlib.Path().joinpath(dcon_folder, "StoryOverrides.csv")
    loc_storyid_footers = ["es-ES", "fr-FR", "pt-BR", "de-DE", "ru-RU"]
    offset = 1

    # Import CSV
    (headers, rows) = import_csv.import_csv(file)
    story_id_col_index = headers.index("identifier")
    prof_priority_col_index = headers.index("profilePriority")

    print("\nSTARTING LOCALIZATION PROFILE PRIORITY CHECK")

    for row in rows:
        # Determine Story ID and the Profile Priority
        story_id = row[story_id_col_index]
        prof_priority = row[prof_priority_col_index]

        # Add Offset
        if story_id == "String":
            offset += 1

        else:
            # Iterate through all possible localization footers and check if they are in story_id
            for footer in loc_storyid_footers:
                if footer in story_id:

                    # Debug
                    # print(story_id)

                    # Print Method
                    if prof_priority != "-1":
                        print("     Row " + str(rows.index(row) + offset) + ": " + story_id + " profilePriority is not -1.")

    print("LOCALIZATION PROFILE PRIORITY CHECK IS COMPLETE")

