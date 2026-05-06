def check_perfect_num(n):
    if n<2:
        return False
    tonguoc = 0
    can = int(n**0.5)
    i=2
    while i<=can:
        if n%i==0:
            tonguoc = tonguoc +i +n//i
    return tonguoc==n
    
print(check_perfect_num(6))