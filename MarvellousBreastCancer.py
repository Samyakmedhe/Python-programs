##############################################################
#Required Python Packages
##############################################################
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

##############################################################
# File Path
##############################################################
INPUT_PATH = "breast-cancer-wisconsin.data"
OUTPUT_PATH = "breast-cancer-wisconsin.csv"

HEADERS = ["CodeNumber", "ClumpThickness", "UniformityCellSize","UniformityCellShape", "MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"]

#############################################################
# Function name : read_data
# Description : Read the data into pandas dataframe
# Input : path of CSV file
# Author : Samyak Kailas Medhe 
# Date : 08/07/2024
#############################################################

def read_data(path):
    data = pd.read_csv(path)
    return data

#############################################################
# Function name : get_headers
# Description : dataset header
# Input : dataset
# Output : Return the header
# Author : Samyak Kailas Medhe
# Date : 08/07/2024
#############################################################

def get_headers(dataset):
    return dataset.columns.values

#############################################################
# Function name : Add_header
# Description : add the headers to the dataset
# Input : dataset
# Output : Updated datset
# Author : Samyak Kailas Medhe
# Date : 08/07/2024
#############################################################

def Add_header(dataset , headers):
    dataset.columns = headers
    return dataset

#############################################################
# Function name : data_file_to_csv
# Input : Nothing 
# Output : write the data to CSV
# Author : Samyak Kailas Medhe
# Date : 08/07/2024
#############################################################

def data_file_to_csv():
    #header
    headers =["CodeNumber", "ClumpThickness", "UniformityCellSize","UniformityCellShape", "MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"]
    # load the data set into pandas data frame
    dataset = read_data(INPUT_PATH)
    #Add the header to the loaded dataset
    dataset = Add_header(dataset,headers)
    dataset.to_csv(OUTPUT_PATH , index = False)
    print("File saved...!")


#############################################################
# Function name : split_dataset
# description : split the dataset with train_percentage
# Input : dataset with related information  
# Output : dataset after Spliting 
# Author : Samyak Kailas Medhe
# Date : 08/07/2024
#############################################################

def split_dataset(dataset,train_percentage , feature_headers, target_header):
    
    train_X , test_X , train_Y , test_Y = train_test_split(dataset[feature_headers],dataset[target_header],train_size= train_percentage)

    return train_X , test_X , train_Y , test_Y


#############################################################
# Function name : handel_missing_values
# description : filter missing values from the dataset
# Input : dataset with missing vales
# Output : dataset by remocking missing values  
# Author : Samyak Kailas Medhe
# Date : 08/07/2024
#############################################################

def handel_missing_values(dataset , missing_values_header, missing_label):
    return dataset[dataset[missing_values_header]!= missing_label]

#############################################################
# Function name : random_forest_classifier
# description : to train the random forest classifier with feature and target data
# Author : Samyak Kailas Medhe
# Date : 08/07/2024
#############################################################

def random_forest_classifier(feature , target):
    clf = RandomForestClassifier()
    clf.fit(feature,target)
    return clf


#############################################################
# Function name : dataset_statistics
# description : basic statistics of the dataset
# Author : Samyak Kailas Medhe
# Date : 08/07/2024
#############################################################
def dataset_statistics(dataset):
    print(dataset.describe())

#############################################################
# Function name : main
# description : Main fuction from where excetion starts
# Author : Samyak Kailas Medhe
# Date : 08/07/2024
#############################################################

def main():

    dataset = pd.read_csv(OUTPUT_PATH)

    dataset_statistics(dataset)

    dataset = handel_missing_values(dataset , HEADERS[6],'?')

    train_X , test_X , train_Y , test_Y = split_dataset(dataset, 0.7,HEADERS[1:-1],HEADERS[-1])

    print("train_x Shape :: ",train_X.shape)
    print("train_y shape :: ",train_Y.shape)
    print("test_x shape :: ",test_X.shape)
    print("test_y shpae :: ",test_Y.shape)

    trained_model = random_forest_classifier(train_X , train_Y)
    print("Train model :: ",trained_model)
    prediction = trained_model.predict(test_X)

    for i in range (0,205):
        print("actual outcome :: {} and Predicted Outcome :: {} ".format(list(test_Y)[i],prediction[i]))
    

    print("Train Accuracy :: ",accuracy_score(train_Y,trained_model.predict(train_X)))
    print("test Accuracy :: ",accuracy_score(test_Y,prediction))
    print("Confusion matrix : ",confusion_matrix(test_Y,prediction))


##################################################################
# Application starter
##################################################################

if __name__ == "__main__":
    main()