import cmath as cm
z = input().strip()
if "+" in z:
    
    if "j" in z.split("+")[1] and len(z) != 3:
        real = int(z.split("+")[0])
        imaginary = int(z.split("+")[1][0])
        
    elif "j" in z.split("+")[0] and len(z) != 3:
        real = int(z.split("+")[1])
        imaginary = int(z.split("+")[0][0])
        
    else:
        real = int(z.split("+")[0])
        imaginary = 1
        
elif "-" in z: 
    if z.count("-") == 1:
        
        if "j" in z.split("-")[1]:
            real = int(z.split("-")[0])
            imaginary = int(z.split("-")[1][0])
            
        else:
            real = int(z.split("-")[1])
            imaginary = int(z.split("-")[0][0])
            
    else:
        if "j" in z.split("-")[2]:
            real = int(z.split("-")[1])
            imaginary = int(z.split("-")[2].split("j")[0])
        
        else:
            if "j" in z.split("-")[1]:
                real = int(z.split("-")[2])
                imaginary = int(z.split("-")[1].split("j")[0])
            

else:
    if "j" in z:
        real = 0
        imaginary = int(z.split("j")[0])
    else:
        real = int(z)
        imaginary = 0


print(abs(complex(real, imaginary)))
print(cm.phase(complex(real, imaginary)))
