import os 
i=0
for filename in os.listdir("."):
	if filename.endswith(".h5"):
		i=i+1
		os.rename(filename,str(i)+".h5")
