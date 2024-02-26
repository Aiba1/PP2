def nu_m(a,b):
    start = a
    stop = b
    if start <stop:
        yield start
        nu_m(start+1,stop)
    else:
        return stop
    
print(list(nu_m(1,10)))