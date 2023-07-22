
import pandas as pd
import prepere_data, os

class New_model:

    path_to_save_model = ""
    path_to_data = ""
    extension = ""

    # Ask user what type of model he want.
    def __init__(self):
        self.get_data()  # Get paths from user.

    def get_data(self):
        self.path_to_save_model = input("Give path to lacalization where save your model: ")
        flag1 = False
        while flag1 is False:  # Until user don't give existing path.
            flag1 = os.path.exists(self.path_to_save_model)  # Check if path exist.
            if flag1 is True:
                break
            self.path_to_save_model = input("Error 1: Path to localization for save model do not exist.\n Give path to lacalization where save your model: ")

        self.path_to_data = input("Give path to file with data: ")
        flag2 = False
        while flag2 is False:
            flag2 = os.path.exists(self.path_to_data)
            if flag2 is True:
                break
            self.path_to_data = input("Error 2: Path to file with data do not exist.\n Give path to file with data: ")

        # Get extension of file with data.
        flag3 = False
        i = len(self.path_to_data)

        while flag3 is False:
            char = self.path_to_data[i - 1]
            if char == ".":
                break
            else:
                self.extension += char
            i -= 1


        self.extension = self.extension[::-1]

        print(self.extension)

        self.separator = input("Give separator for your data in .csv file: ")

        if self.extension == "csv":
            object_get_csv_format_data = Get_csv_format_data(self.path_to_data, self.separator)
            self.data = object_get_csv_format_data.give_back()
            to_model = prepere_data.Prepere_data(self.data, self.path_to_save_model)
        else:
            print("Error 3: Wrong type of file. Closing program.")
            exit(0)


class Get_csv_format_data:

    data = []

    # Get path to file with data.
    def __init__(self, path_to_data, separator):
        self.path_to_data = path_to_data
        self.separator = separator
        self.get_dataframe_object()

    def get_dataframe_object(self):
        self.data = pd.read_csv(self.path_to_data, sep=self.separator)  # Get DataFrame object from file.


    # Return DataFrame object.
    def give_back(self):
        return self.data
