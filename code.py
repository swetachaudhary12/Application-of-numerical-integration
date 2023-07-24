import pandas as pd
df=pd.read_excel("/content/drive/MyDrive/modified data.xlsx")
Strain = list(df['Strain '])
Stress = list(df['Stress'])
x= Strain[0:5891]
y= Stress[0:5891]

def Trap(h,f,g):
  Trap = h *(f+g)/2
  return Trap
def Simp13(h,f,g,i):
  return h*(f+4*g+i)/6
def Simp38(h,f,g,i,j):
 return h*(f+3*(g+i)+j)/8

def Uneven (n,x,y):
 sum = 0
 for j in range(n-1):
   hf = x[j]-x[j-1]; ht=x[j-2]-x[j-3];hg=x[j-1]-x[j-2];
   sum=sum+Trap(x[1]-x[0],y[1],y[0])
   if(hf==hg ):
     sum=sum+Simp13(x[j]-x[j-2],y[j],y[j-1],y[j-2])
   elif(hf==hg and hg==ht):
     sum=sum+Simp38(x[j]-x[j-3],y[j],y[j-1],y[j-2],y[j-3])
   else:
     sum = sum + Trap(x[j]-x[j-1],y[j],y[j-1])
  print("Toughness of material=",sum)

