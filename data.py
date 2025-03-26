import pandas as pd

data = {
    'duration' : [1,2,4,5,3,8,9,2,6,7],
    'protocol_type':['TCP','UDP','ICMP','TCP','UDP','ICMP','TCP','UDP','ICMP','TCP'],
    'service' : ['HTTP','DNS','SMTP','HTTP','DNS','SMTP','HTTP','DNS','SMTP','HTTP'],
    'flag' : ['S1','S2','S0','SF','FIN','REJ','S2','S0','S1','REJ'],
    'src_bytes' : [100,200,66,567,88,34,890,4356,23,88],
    'dst_bytes' : [200,77,55,987,434,23,0,43,0,3245],
    'label' : ['normal','normal','attack','normal','normal','normal','attack','normal','attack','attack'],
    
}
df = pd.DataFrame(data)
df.to_csv('Network_data.csv',index=False)


