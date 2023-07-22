import sklearn, pickle
from sklearn import linear_model


class Train_model:

    def __init__(self, x, y, test_size, path_to_save_model):
        self.x = x
        self.y = y
        self.test_size = test_size
        self.path_to_save_model = path_to_save_model

        best_accuracy = 0
        multi_trainning = input("How many times do you want to train your model: ")
        while multi_trainning.isnumeric() is False:
            multi_trainning = input("Error 9: It is not a number! How many times do you want to train your model: ")

        name_of_model = input("Give name for your model (without extension): ")
        name_of_model = path_to_save_model +  name_of_model + ".pickle"

        multi_trainning = int(multi_trainning)
        i = 1
        while multi_trainning >= i:

            # Divide data into proper four variable.
            x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=self.test_size)

            # Creat model
            model = linear_model.LinearRegression()

            print("Model ", i, " in trainig. ", end="")

            # Train model
            model.fit(x_train, y_train)

            # Test model
            accuracy = model.score(x_test, y_test)

            if accuracy > best_accuracy:
                best_accuracy = accuracy
                # Save model.
                with open(name_of_model, "wb") as file:
                    pickle.dump(model, file)

            print("Done ", end="")
            print("Accuracy for actual model: ", accuracy)
            i += 1


        print("Best accurracy of your model: ", best_accuracy)