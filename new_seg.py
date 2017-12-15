import pandas as pd
import numpy

df = pd.read_csv("yieldmo.csv").sort_values('num1', ascending=True)

new_seg=[]
for(i=1; i< length(df); i++):
    for (j=1; j < length(sort_df); j++):
        number1=sort_df['num1'][i]
        number2=sort_df['num2'][i]
        if ((number2 - sort_df['num1'][j+1]) < 5 ) && (number2 - sort_df['num1'][j+1])> 0):
        	number2 = sort_df['num2'][j+1]
        	new_seg.append[(num1,num2)]
        
    	else 
        	j +=1
        
    print(new_seg)    





        

