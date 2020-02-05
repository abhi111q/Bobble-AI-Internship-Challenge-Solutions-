import pandas as panda   # To read csv file pandas has been imported
 
import sys               # sys is imported to read Command line arguments
 
command_line_arguments=sys.argv


datafile=panda.read_csv(command_line_arguments[1],header=None)
 
datafile=datafile.fillna("na")         # filling Null with 'na'
 
def BobbleAiPermutation(n):              
    if n>=datafile.shape[0]:
        emptyl=[""]
        return emptyl
    ml=BobbleAiPermutation(n+1)
    answer=[str(i)+str(j) for i in datafile.iloc[n] for j in ml if i!='na' and j!='na']
    return answer
 
 
result=BobbleAiPermutation(0)     # Calling The function 
 
 
for i in range(len(result)-1):           # Printing the result
    print(result[i],end=", ")
print(result[len(result)-1],end="")
