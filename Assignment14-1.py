from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np

def MarvellousPrediction():
    file_path = '/Users/apple/Downloads/WinePredictor (1) (1).csv'
    df = pd.read_csv(file_path)

# Display the original dataset
    print("Original dataset:")
    print(df.head())

# Step 2: Clean, Prepare, and Manipulate Data

    le_Alcohol = LabelEncoder()
    le_Malic_acid = LabelEncoder()
    le_Ash = LabelEncoder()
    le_Alcalinity_of_ash = LabelEncoder()
    le_Magnesium = LabelEncoder()
    le_total_phenols = LabelEncoder()
    le_Flavanoids = LabelEncoder()
    le_Nonflavanoids_phenols = LabelEncoder()
    le_Proanthocyanins = LabelEncoder()
    le_Color_intensity = LabelEncoder()
    le_Hue = LabelEncoder()
    le_OD280_OD315_of_diluted_wines = LabelEncoder()
    le_Proline = LabelEncoder()

    df['Alcohol'] = le_Alcohol.fit_transform(df['Alcohol'])
    df['Malic acid'] = le_Malic_acid.fit_transform(df['Malic acid'])
    df['Ash'] = le_Ash.fit_transform(df['Ash'])
    df['Alcalinity of ash'] = le_Alcalinity_of_ash.fit_transform(df['Alcalinity of ash'])
    df['Magnesium'] = le_Magnesium.fit_transform(df['Magnesium'])
    df['Total phenols'] = le_total_phenols.fit_transform(df['Total phenols'])
    df['Flavanoids'] = le_Flavanoids.fit_transform(df['Flavanoids'])
    df['Nonflavanoid phenols'] = le_Nonflavanoids_phenols.fit_transform(df['Nonflavanoid phenols'])
    df['Proanthocyanins'] = le_Proanthocyanins.fit_transform(df['Proanthocyanins'])
    df['Color intensity'] = le_Color_intensity.fit_transform(df['Color intensity'])
    df['Hue'] = le_Hue.fit_transform(df['Hue'])
    df['OD280/OD315 of diluted wines'] = le_OD280_OD315_of_diluted_wines.fit_transform(df['OD280/OD315 of diluted wines'])
    df['Proline'] = le_Proline.fit_transform(df['Proline'])

# Display the modified dataset
    print("\nModified dataset:")
    print(df.head())

    return df , le_Alcohol , le_Malic_acid ,le_Ash ,le_Alcalinity_of_ash , le_Magnesium, le_total_phenols , le_Flavanoids,le_Nonflavanoids_phenols, le_Proanthocyanins , le_Color_intensity , le_Hue , le_OD280_OD315_of_diluted_wines , le_Proline


# Step 3: Train Data
def train_model(df ,le_Alcohol , le_Malic_acid ,le_Ash ,le_Alcalinity_of_ash , le_Magnesium, le_total_phenols , le_Flavanoids,le_Nonflavanoids_phenols, le_Proanthocyanins , le_Color_intensity , le_Hue , le_OD280_OD315_of_diluted_wines , le_Proline):
# Prepare data for training
    X = df[['le_Alcoho', 'le_Malic_acid' ,'le_Ash','le_Alcalinity_of_ash','le_Magnesium','le_total_phenols','le_Flavanoids','le_Nonflavanoids_phenols','le_Proanthocyanins','le_Color_intensity','le_Hue','le_OD280/OD315_of_diluted_wines']].values
    y = df['le_Proline'].values

# Create KNN classifier with K=3
    knn = KNeighborsClassifier(n_neighbors=3)

# Train the model using the entire dataset
    knn.fit(X, y)
    return knn

# Step 4: Test Data
def test_model(knn,le_Alcohol , le_Malic_acid ,le_Ash ,le_Alcalinity_of_ash , le_Magnesium, le_total_phenols , le_Flavanoids,le_Nonflavanoids_phenols, le_Proanthocyanins , le_Color_intensity , le_Hue , le_OD280_OD315_of_diluted_wines ):

    test_data = [
        ['14.23','1.71','2.43','15.6','127','2.8','3.06','0.28','2.29','5.64','1.04','3.92'],
        ['13.2','1.78','2.14','11.2','100','2.65','2.76','0.26','1.28','4.38','1.05','3.4'],
        ['13.16','2.36','2.67','18.6','101','2.8','3.24','0.3','2.81','5.68','1.03','3.17']
    ]

# Convert test data to numerical format using LabelEncoder
    # Predict using the trained model
    predictions = knn.predict(test_data)

    # Display the predictions
    print("\nPredictions:")
    for i in range(len(test_data)):
        print(f"Whether: {test_data[i][0]}, Temperature: {test_data[i][1]} => Prediction: {predictions[i]}")

    # Step 5: Calculate Accuracy

# Define a function to calculate accuracy with different K values
def check_accuracy(knn, X , y):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=42)

    # Train the model using the training data
    knn.fit(X_train, y_train)

    # Predict using the test data
    y_pred = knn.predict(X_test)

    # Calculate and return accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nAccuracy of the KNN model with K=3: ",accuracy*100 ,"%")

def main():

    print("---------Marvellous Weather case Study-------")
    df ,le_Alcohol,le_Malic_acid,le_Ash,le_Alcalinity_of_ash,le_Magnesium,le_total_phenols,le_Flavanoids,le_Nonflavanoids_phenols,le_Proanthocyanins ,le_Color_intensity,le_Hue,le_OD280_OD315_of_diluted_wines = MarvellousPrediction()
    knn = train_model(df , le_Alcohol , le_Malic_acid ,le_Ash ,le_Alcalinity_of_ash , le_Magnesium, le_total_phenols , le_Flavanoids,le_Nonflavanoids_phenols, le_Proanthocyanins , le_Color_intensity , le_Hue , le_OD280_OD315_of_diluted_wines)

    test_model(knn,le_Alcohol , le_Malic_acid ,le_Ash ,le_Alcalinity_of_ash , le_Magnesium, le_total_phenols , le_Flavanoids,le_Nonflavanoids_phenols, le_Proanthocyanins , le_Color_intensity , le_Hue , le_OD280_OD315_of_diluted_wines)
    X = df[['le_Alcoho', 'le_Malic_acid' ,'le_Ash','le_Alcalinity_of_ash','le_Magnesium','le_total_phenols','le_Flavanoids','le_Nonflavanoids_phenols','le_Proanthocyanins','le_Color_intensity','le_Hue','le_OD280/OD315_of_diluted_wines']].values
    y = df['le_Proline'].values
    
    MarvellousPrediction() 
    accuracy= check_accuracy(knn , X , y)
    print(f"\nAccuracy of the KNN model with K=3: ",accuracy*100 ,"%")
   
    
if __name__ == "__main__":
    main()


