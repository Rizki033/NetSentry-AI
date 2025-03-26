import pandas as pd 

new_data = {
    'duration':[1,3,6,7],
    'protocol_type' : ['TCP','UDP','ICMP','TCP'],
    'service' : ['HTTP','DNS','FTP','HTTPS'],
    'flag' :['SF','REJ','S0','S1'], # S0 ==> DDOS Attack
    'src_bytes' : [100,400,700,900],
    'dst_bytes' : [200,1000,400,1500],
    'label' : [None, None,None,None]
}

df = pd.DataFrame(new_data)
df.to_csv('Network_new_data.csv',index=False)