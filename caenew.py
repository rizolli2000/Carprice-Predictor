import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import tkinter as tk
from tkinter import messagebox

# Load the dataset
df = pd.read_csv("CarPricesPrediction.csv")

# Preprocess the data
X = df[['Year', 'Mileage']].values
y = df['Price'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = GradientBoostingRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# GUI
def predict_price():
    try:
        year = int(entry_year.get())
        mileage = int(entry_mileage.get())

        # Predict price
        predicted_price = model.predict([[year, mileage]])[0]

        messagebox.showinfo("Prediction", f"The predicted price is ${predicted_price:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")


# Create tkinter window
window = tk.Tk()
window.title("Car Price Predictor")

# Labels
label_year = tk.Label(window, text="Enter Year:")
label_year.grid(row=0, column=0)
label_mileage = tk.Label(window, text="Enter Mileage:")
label_mileage.grid(row=1, column=0)

# Entry fields
entry_year = tk.Entry(window)
entry_year.grid(row=0, column=1)
entry_mileage = tk.Entry(window)
entry_mileage.grid(row=1, column=1)

# Button
predict_button = tk.Button(window, text="Predict Price", command=predict_price)
predict_button.grid(row=2, column=0, columnspan=2)

window.mainloop()
