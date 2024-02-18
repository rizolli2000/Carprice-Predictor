# Carprice-Predictor

Import Libraries:

pandas: For data manipulation and loading the dataset.
sklearn.model_selection.train_test_split: For splitting the dataset into training and testing sets.
sklearn.ensemble.GradientBoostingRegressor: For building a Gradient Boosting Regression model.
tkinter: For creating the GUI.
tkinter.messagebox: For displaying message boxes in the GUI.
Load the Dataset:

Reads a CSV file named "CarPricesPrediction.csv" containing car data into a pandas DataFrame (df).
Preprocess the Data:

Extracts the features (X - 'Year' and 'Mileage') and the target variable (y - 'Price') from the DataFrame.
Split the Data:

Splits the dataset into training and testing sets using train_test_split() function from scikit-learn.
80% of the data is used for training (X_train, y_train), and 20% is used for testing (X_test, y_test).
Train the Model:

Initializes a GradientBoostingRegressor model with 100 estimators and a random state of 42.
Fits the model to the training data using fit() method.
Define GUI Components:

Creates a tkinter window (window) with the title "Car Price Predictor".
Defines labels for "Enter Year" and "Enter Mileage".
Creates entry fields (entry_year and entry_mileage) for users to input the year and mileage of the car.
Adds a button (predict_button) labeled "Predict Price" that triggers the predict_price() function when clicked.
Define predict_price() Function:

Gets the input values of year and mileage from the entry fields.
Uses the trained model to predict the price based on the input values.
Displays the predicted price in a message box using messagebox.showinfo().
Main Loop:

Enters the tkinter event loop with window.mainloop(), which keeps the GUI window running and responsive until the user closes it.
Overall, this program allows users to input the year and mileage of a car and predicts its price based on a trained Gradient Boosting Regression model. It provides a simple and interactive interface for users to make predictions on car prices.
