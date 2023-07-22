import numpy as np
import model


class Prepere_data:

    test_size = 0.0

    def __init__(self, data, path_to_save_model):
        self.data = data
        self.path_to_save_model = path_to_save_model

        # Get from user a amount of test size. + Protection.
        self.test_size = input("How many percent of your data, should be use for tests: ")
        while self.test_size.isnumeric() is False or len(self.test_size) == 0:  # If input is not numerical or is empty:
            self.test_size = input("Error 4:How many percent of your data, should be use for tests: ")

        self.test_size = int(self.test_size)
        while True:
            if self.test_size <= 0 or self.test_size >= 100:  # If number is higher than 100 or less or equal 0:
                self.test_size = int(input("Error 5: Wrong number! Try again: "))
            elif self.test_size >= 50:  # Ask if user want to train model with so large amount of test data.
                self.are_you_sure = input("A data to test should have rather less data than data to train. Are you sure you want to continue (y/n): ")
                if self.are_you_sure == "y" or self.are_you_sure == "Y":
                    break
                else:
                    self.test_size = int(input("How many percent of your data, should be use for tests: "))
            else:
                break
        self.test_size = float(self.test_size / 100.0)  # Get from int float, from 0 to 1.

        self.columns_name = self.data.columns.values.tolist() # Get names of columns into DataFrame object.


        print(self.columns_name)

        # Get from user target data.
        self.target_data = input(
            "Give name of column with target data. Target data: is data you want your model to predict: ")
        while True:

            if self.target_data in self.columns_name:
                break
            else:
                print("Error 6: There is no column's name in file!")
                print("List of columns names: ", self.columns_name)
                self.target_data = input(
                    "Give name of column with target data. Target data: is data you want your model to predict: ")

        self.feature_data_names = []  # List for colum's names with feature data.

        while True:
            print("Your columns names with feature data: ", self.feature_data_names)
            buffor = input("Give name of columns with feature data. Feature data is data that you provide to your model for get prediction: ")
            if buffor in self.columns_name and buffor != self.target_data:  # If there exist in file that column's name and it is not a target data colun's name.
                self.feature_data_names.append(buffor)
            else:
                print("Error 7: There is no column's name into file as you give!")
                continue

            next = input("Do you want to add next name of column with your feature data (y/n): ")
            if next == "y" or next == "Y":
                continue
            else:
                if len(self.feature_data_names) == 0:
                    print("Error 8: There is no feature data! You have to add at least one name column.")
                    continue
                else:
                    break

        x = np.array(self.data[self.feature_data_names])
        y = np.array(self.data[self.target_data])

        to_model = model.Train_model(x, y, self.test_size, self.path_to_save_model)