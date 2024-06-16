def calculate(a,b,c="+"):
    """
        This function is for performing operations of calculation 
    """
    if c == "-":
        return a-b
    elif c == "*":
        return a*b
    elif c == "/":
        return a/b
    else:
        return a+b
    
if __name__ == "__main__":
   print(calculate(2,3))
