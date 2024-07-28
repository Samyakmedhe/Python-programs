from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np

def MarvellousPrediction():
    file_path = '/Users/apple/Downloads/PlayPredictor (2).csv'
    df = pd.read_csv(file_path)

# Display the original dataset
    print("Original dataset:")
    print(len(df))

# Step 2: Clean, Prepare, and Manipulate Data

# Use LabelEncoder to convert categorical variables (Weather and Temperature) to numerical values
    le_Whether = LabelEncoder()
    le_Temperature = LabelEncoder()

    df['Whether'] = le_Whether.fit_transform(df['Whether'])
    df['Temperature'] = le_Temperature.fit_transform(df['Temperature'])

# Display the modified dataset
    print("\nModified dataset:")
    print(df.head())

    return df , le_Whether , le_Temperature

# Step 3: Train Data
def train_model(df , le_Whether , le_Temperature):

# Prepare data for training
    X = df[['Whether', 'Temperature']].values
    y = df['Play'].values

# Create KNN classifier with K=3
    knn = KNeighborsClassifier(n_neighbors=3)

# Train the model using the entire dataset
    knn.fit(X, y)
    return knn

# Step 4: Test Data
def test_model(knn,le_Whether , le_Temperature):

    test_data = [
        ['Sunny', 'Cool'],
        ['Overcast', 'Hot'],
        ['Rainy', 'Mild']
    ]

# Convert test data to numerical format using LabelEncoder
    test_data_encoded = []
    for i in range(len(test_data)):
        Weather_encoded = le_Whether.transform([test_data[i][0]])[0]
        temp_encoded = le_Temperature.transform([test_data[i][1]])[0]
        test_data_encoded.append([Weather_encoded, temp_encoded])

    # Predict using the trained model
    predictions = knn.predict(test_data_encoded)

    # Display the predictions
    print("\nPredictions:")
    for i in range(len(test_data)):
        print(f"Whether: {test_data[i][0]}, Temperature: {test_data[i][1]} => Prediction: {predictions[i]}")

    # Step 5: Calculate Accuracy

# Define a function to calculate accuracy with different K values
def check_accuracy(knn, X , y):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    # Train the model using the training data
    knn.fit(X_train, y_train)

    # Predict using the test data
    y_pred = knn.predict(X_test)

    # Calculate and return accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy

def main():

    print("---------Marvellous Weather case Study-------")

    df , le_Whether , le_Temperature = MarvellousPrediction()
    

    knn = train_model(df, le_Whether ,le_Temperature)

    test_model(knn, le_Whether , le_Temperature)

    X = df[['Whether', 'Temperature']].values
    y = df['Play'].values
    MarvellousPrediction()
    accuracy= check_accuracy(knn , X , y)
    print(f"\nAccuracy of the KNN model with K=3: ",accuracy*100 ,"%")
    

    
if __name__ == "__main__":
    main()


