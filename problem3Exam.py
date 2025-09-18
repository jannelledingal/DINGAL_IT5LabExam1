mobilenumber = int(input("Enter mobile number: "))

if len(mobilenumber) !=11:
    print("Invalid mobile number")
elif mobilenumber[0:2] !="09":
    print("invalid mobile number")
else:
    prefix = mobilenumber[0:4]

    if prefix in["0903", "0904", "0905", "0906","0907"]:
        print("The network of the mobile number is TM")
    elif prefix in ["0915", "0916", "0917","0925","0926","0927"]:
        print("The network of the mobile number is GLOBE")
    elif prefix in ["0913", "0914", "0920","0921","0928","0929","0930"]:
        print("The network of the mobile number is SMART")
    elif prefix in ["0922", "0923", "0932","0933"]:
        print("The network of the mobile number is SUN")
    elif prefix in ["0909", "0909", "0910","0911","0911","0912","0918","0919"]:
        print("The network of the mobile number is TNT")
    elif prefix in ["0901", "0902", "0924"]:
        print("The network of the mobile number is RED")
    elif prefix in ["0991", "0992", "0993","0994","0995","0996", ]:
        print("The network of the mobile number is DITO")
    else:
        print("Unknown network")
    
    
    
