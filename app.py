import customtkinter as ctk
import pandas as pd
from joblib import load

# Load the trained model and feature names
model = load("car_price_predictor.joblib")  # Load the saved model
feature_names = model.feature_names_in_  # Extract feature names used during training

# Function to predict price
def predict_price():
    try:
        # Collect user inputs
        inputs = {
            "Prod. year": int(year_entry.get()),
            "Levy": float(levy_entry.get()),
            "Engine volume": float(engine_entry.get()),
            "Mileage": float(mileage_entry.get()),
        }

        # Convert inputs into a DataFrame row
        input_df = pd.DataFrame([inputs])
        input_df = pd.get_dummies(input_df)

        # Align columns to match the training set
        input_df = input_df.reindex(columns=feature_names, fill_value=0)

        # Make predictions
        prediction = model.predict(input_df)
        result_label.configure(text=f"Predicted Price: ${prediction[0]:,.2f}")
    except Exception as e:
        result_label.configure(text=f"Error: {str(e)}")

# Initialize the customtkinter GUI
ctk.set_appearance_mode("System")  # Options: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")  # Default theme: blue

root = ctk.CTk()
root.title("Car Price Predictor")

# Set min and max size for the window
root.minsize(400, 300)
root.maxsize(600, 400)

# Input fields
ctk.CTkLabel(root, text="Production Year:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
year_entry = ctk.CTkEntry(root, placeholder_text="e.g., 2020")
year_entry.grid(row=0, column=1, padx=10, pady=10)

ctk.CTkLabel(root, text="Levy:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
levy_entry = ctk.CTkEntry(root, placeholder_text="e.g., 500")
levy_entry.grid(row=1, column=1, padx=10, pady=10)

ctk.CTkLabel(root, text="Engine Volume:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
engine_entry = ctk.CTkEntry(root, placeholder_text="e.g., 1.6")
engine_entry.grid(row=2, column=1, padx=10, pady=10)

ctk.CTkLabel(root, text="Mileage:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
mileage_entry = ctk.CTkEntry(root, placeholder_text="e.g., 15000")
mileage_entry.grid(row=3, column=1, padx=10, pady=10)

# Predict button
predict_button = ctk.CTkButton(root, text="Predict Price", command=predict_price)
predict_button.grid(row=4, column=0, columnspan=2, pady=20)

# Result label
result_label = ctk.CTkLabel(root, text="Predicted Price: $0.00", text_color="green")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
