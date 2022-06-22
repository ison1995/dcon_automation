import import_csv
import pathlib


def check_profile_names(dcon_folder):
    # Folder Setup
    story_overrides_file = pathlib.Path().joinpath(dcon_folder, "StoryOverrides.csv")
    profiles_file = pathlib.Path().joinpath(dcon_folder, "ProfileOfficialUser.csv")

    # Headers and Rows Setup
    (h1, r1) = import_csv.import_csv(story_overrides_file)
    (h2, r2) = import_csv.import_csv(profiles_file)

    storyoverrides_profile_index = h1.index("associatedProfile")
    profiles_profile_index = h2.index("identifier")
    offset = 1

    print("\nSTARTING AUTHOR PROFILE PRIORITY CHECK")
    for row_story in r1:
        # Determine Story ID and the Profile Priority
        storyoverrides_profile = row_story[storyoverrides_profile_index]

        # Add Offset
        if storyoverrides_profile == "String":
            offset += 1

        # Look for Profile obtained from StoryOverrides.csv in ProfileOfficialUser.csv
        elif storyoverrides_profile != "-1" and storyoverrides_profile != "":
            match_flag = False
            for row_profile in r2:
                profiles_profile = row_profile[profiles_profile_index]
                if storyoverrides_profile == profiles_profile:
                    match_flag = True
                    break

            if not match_flag:
                print("     The author " + storyoverrides_profile + " does not have a match in Profile Priority.")

    print("AUTHOR PROFILE PRIORITY CHECK IS COMPLETE")

