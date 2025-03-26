# Python-AI-based-DDoS-Detection
This project uses artificial intelligence to detect DDoS attacks on a network based on a machine learning model. It utilizes a network traffic dataset to train a classification model that can identify whether traffic is normal or malicious.

## Technologies Used 

- Python

- Pandas  

- Scikit-learn

- Random Forest Classifier

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/Rizki033/Python-AI-based-DDoS-Detection.git
```
### 2. Install dependencies
Make sure Python is installed, then use pip to install the required libraries:
```bash
pip install pandas scikit-learn
```
### 3. Run the project 
  1. Run data.py to generate the Network_data.csv file:
     ```bash
     python data.py
     ```
 2. Run app.py to train the model and test detection:
    ```bash
    python app.py
    ```
## How It Works 

### Data Preprocessing :
- Load data from Network_data.csv
- Encode categorical variables (protocol_type, service, flag)
- Split data into input variables (X) and output labels (y)
- Divide into training and testing sets
### Model Training:
- Use RandomForestClassifier to train a model for DDoS attack detection
### Model Testing:
- A test_network function is provided to test new data for potential attacks


## Detection Example :
```bash
results  data : 1:normal
results  data : 2:normal
results  data : 3:attack
results  data : 4:normal
```


