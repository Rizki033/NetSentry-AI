import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('Network_data.csv')
#print(data.head())
label_encoder = LabelEncoder()
data['protocol_type'] = label_encoder.fit_transform(data['protocol_type'])
data['service'] = label_encoder.fit_transform(data['service'])
data['flag'] = label_encoder.fit_transform(data['flag'])

x = data.drop(columns=['label']) # normal and attack  
y = data['label']

X_train , X_test , Y_train , Y_test = train_test_split(x , y,test_size=0.2,random_state=42)
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train ,Y_train )

def test_network(data_input):
    data_input['protocol_type'] = label_encoder.fit_transform(data_input['protocol_type'])
    data_input['service'] = label_encoder.fit_transform(data_input['service'])  
    data_input['flag'] = label_encoder.fit_transform(data_input['flag'])
    pred = model.predict(data_input)
    for i , p in enumerate(pred):
        print(f"results  data : {i+1}:{p}")
  
    
new_data = pd.DataFrame({
    'duration':[1,3,6,7],
    'protocol_type' : ['TCP','UDP','ICMP','TCP'],
    'service' : ['HTTP','DNS','FTP','HTTPS'],
    'flag' :['SF','REJ','S0','S1'], # S0 ==> DDOS Attack
    'src_bytes' : [100,400,700,900],
    'dst_bytes' : [200,1000,400,1500],
    'label' : [None, None,None,None]
})
#test_network(new_data.drop(columns=['label'])) # 7 , TCP , HTTPS , S1 , 900 , 1500 ==>attack 
test_network(data.drop(columns=['label'])) 



