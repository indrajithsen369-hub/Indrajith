import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib


conn = sqlite3.connect("house_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bedrooms INTEGER,
    bathrooms INTEGER,
    area FLOAT,
    location TEXT,
    predicted_price FLOAT
)
""")
conn.commit()


data = {
    'bedrooms':   [2,3,4,3,5,2,4,1,3,5,2,4,3,6,2],
    'bathrooms':  [1,2,3,2,4,1,3,1,2,4,1,3,2,5,1],
    'area':       [900,1200,1600,1400,2000,850,1800,600,1100,2500,750,1700,1300,3000,800],
    'location':   ['city','suburb','city','suburb','city','rural','city','rural','suburb',
                   'city','rural','suburb','city','city','suburb'],
    'price':      [75,120,180,140,250,60,200,45,110,320,55,190,130,400,65]
}

df = pd.DataFrame(data)

# Encode location
df['location'] = df['location'].map({'city': 2, 'suburb': 1, 'rural': 0})

X = df[['bedrooms', 'bathrooms', 'area', 'location']]
y = df['price']


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "house_price_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\n model trained successfully!")


def predict_price():
    print("\n--- Enter House Details ---")
    bedrooms = int(input("Bedrooms: "))
    bathrooms = int(input("Bathrooms: "))
    area = float(input("Area (sq ft): "))
    location = input("Location (city/suburb/rural): ").lower()

    loc_value = 2 if location == "city" else 1 if location == "suburb" else 0

    loaded_model = joblib.load("house_price_model.pkl")
    loaded_scaler = joblib.load("scaler.pkl")

    features = [[bedrooms, bathrooms, area, loc_value]]
    scaled_features = loaded_scaler.transform(features)

    predicted_price = loaded_model.predict(scaled_features)[0] *10000


    print(f"\nPredicted House Price: ₹{predicted_price:.2f} \n")

    cursor.execute("""
        INSERT INTO predictions (bedrooms, bathrooms, area, location, predicted_price)
        VALUES (?, ?, ?, ?, ?)
    """, (bedrooms, bathrooms, area, location, predicted_price))

    conn.commit()
    print(" Prediction saved to database!\n")


def view_history():
    cursor.execute("SELECT * FROM predictions")
    rows = cursor.fetchall()

    if not rows:
        print("\n No prediction history available.\n")
    else:
        print("\n------ SAVED PREDICTIONS ------\n")
        for row in rows:
            print(f"ID: {row[0]} | Bedrooms: {row[1]} | Bathrooms: {row[2]} | "
                  f"Area: {row[3]} sq.ft | Location: {row[4]} | Price: ₹{row[5]:.2f} lakhs")
        print()


while True:
    print("\n===== HOUSE PRICE PREDICTION SYSTEM =====")
    print("1. Predict House Price")
    print("2. View Prediction History")
    print("3. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        predict_price()
    elif choice == "2":
        view_history()
    elif choice == "3":
        print("\n Program closed. Thankyou!")
        break
    else:
        print("\n Invalid choice. Try again.")

conn.close()