def makeEqual(x: str, y: str) -> Tuple[str, str]:
    """If numbers are not of same size then we make them equal."""
    n1 = x.size()
    n2 = y.size()
    if n1 > n2:
        y = "0"*(n1-n2) + y
    else:
        x = "0"*(n2-n1) + x
    return x,y



def addBits(x: str, y: str) -> str:
    """Method to add the two numbers."""
    n = x.size()
    sumi = 0
    carry = 0
    for i in range(n):
        temp = (x[i]-'0') + (y[i]-'0')
        carry = temp % 10
        sumi = sumi*10 + temp//10
   return sumi


def karatsuba(x: str, y: str) -> str:
    """Implementation of karatsuba multiplication for two numbers."""
    n1 = x.size()
    n2 = y.size()
    if n1 != n2:
        x, y = makeEqual(x, y)
    n = x.size()
    fh = n//2
    sh = n - fh
    xl = x[0:fh+1]
    xr = x[fh+1:]
    yl = y[0:fh+1]
    yr = y[fh+1:]
    p1 = multiply
    return (xl*yl)*(1<<(2*sh)) + (
    
    

if __name__ == "__main__":
    x = input("Enter first number")
    y = input("Enter second number")
    print(f"Their multiplication is {karatsuba(x, y)}")



