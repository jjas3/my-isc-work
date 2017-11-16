def calc_hypo(a,b):
    if type(a) not in (float,int) or type(b) not in (float,int):
        print "Bad argument"
        return False    
    hypo = ((a**2)+(b**2))**0.5
    return hypo
    

y= calc_hypo("hi","oi")
print y
