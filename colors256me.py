for i in range(38,49,10):
    print("\n\n\33[4;37mBackground\33[0;0m") if i==48 else print("\33[4;37mForeground\33[0;0m")
    for j in range(0,256):
        if j%16==0: print(f"\n\33[{i};5;{j}m{str(j).rjust(3, " ")}\33[0;0m", end=" ")
        else: print(f"\33[{i};5;{j}m{str(j):>3}\33[0;0m", end=" ")