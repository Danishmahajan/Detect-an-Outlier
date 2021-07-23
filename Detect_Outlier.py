import numpy as np
print("\n \n                    Detect an Outlier................")

# list1=[10,11,11,111,11,11,11,12,12,12,12,12,12,10,10,10,10,10,13,13,567]

def detect_outlier(list):
    threshold = 2
    outlier=[]
    mean = np.mean(list)
    print("\nMean : ",mean,"\n")
    sd = np.std(list)
    print("Standard Deviation : ",sd,"\n")
    for i in list:
        z_score=(i-mean)/sd
        # print(z_score)
        if np.abs(z_score)>threshold:
            outlier.append(i)
    print("The Outliers in the given Data are : ",outlier,"\n")

#The   Data is given below =>
list1=[10,11,11,111,15,15,16,15,14,13,12,12,12,10,10,10,10,10,13,13,567,478,498]
print("\nThe Given Data is =>",list1)
detect_outlier(list1)