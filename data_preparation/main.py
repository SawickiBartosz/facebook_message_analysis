from create_csv import create_csv
from create_csv_2 import create_csv_2
import emoji

if __name__ == '__main__':

    # Create your csv files
    # a list to all directories created by facebook
    # sometimes it is only one directory, sometimes more - make sure to put it in a list
    # e.g. list_of_paths_to_directories = ['path/facebook-kubalis186-1/', 'path/facebook-kubalis186-2/']

    list_of_paths_to_directories = None

    # a file with all emojis - maybe it can be used in R
    with open('all_emoji.txt', 'w') as f:
        for key in emoji.UNICODE_EMOJI.keys():
            f.write(key + '\n')

    create_csv(
        "Imię Naziwsko",  # e.g. "Kuba Lis"
        list_of_paths_to_directories,
        'data/outputfile_1.csv',
        True
    )

    create_csv_2(
        "Imię Naziwsko",
        list_of_paths_to_directories,
        'data/outputfile_2.csv',
        True
    )




