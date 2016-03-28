
import math

Infinity = float("inf")

def thrt(x):
    return math.pow(x, 1.0/3) if x>0 else -math.pow(-x, 1.0/3)

def sqrt(x):
    return math.sqrt(x) if x>0 else 0

def sq(x):
    return x*x

def cb(x):
    return x*x*x

# x(t) = t^3 T + 3t^2(1-t) U + 3t(1-t)^2 V + (1-t)^3 W 
def time(pt1, ct1, ct2, pt2, x):
    #var C = Cubic, a,b,c,d,p,q,lambda,sqlambda,tmp,addcoef,t,qb,qc,norm,angle,fact;
    a =  pt1.x  - 3*ct1.x + 3*ct2.x - pt2.x
    b = 3*ct1.x - 6*ct2.x + 3*pt2.x
    c = 3*ct2.x - 3*pt2.x
    d =  pt2.x  - x

    if(abs(a) < 0.000000001): #quadratic
        if(abs(b) < 0.000000001): #linear
            return -d/c

        qb = c/b
        qc = d/b
        tmp = sqrt(sq(qb)-4*qc)
        return (-qb +(tmp if (qb>0 or qc<0) else -tmp)) / 2


    p = -sq(b)/(3*sq(a)) + c/a
    q = 2*cb(b/(3*a)) - b*c/(3*sq(a)) + d/a
    addcoef = -b/(3*a)

    lmbd = sq(q)/4 + cb(p)/27
    if(lmbd >= 0): #real
        sqlambda = sqrt(lmbd)
        tmp = thrt(-q/2 + (sqlambda if q<0 else -sqlambda))
        return tmp - p/(3*tmp) + addcoef
    else:
        norm = sqrt(sq(q)/4 - lmbd)
        if(norm < 0.0000000001):
            return addcoef

        angle = math.acos(-q/(2*norm)) / 3
        fact = 2 * thrt(norm)
        t = Infinity
        for i in range(-1, 2):
            tmp = fact * math.cos(angle + i*math.pi*2/3) + addcoef
            if(tmp>=-0.000000001 and tmp < t):
                t = tmp

        return t;

def value(pt1, ct1, ct2, pt2, x):
    t = time(pt1, ct1, ct2, pt2, x);
    return cb(t)*pt1.y + 3*sq(t)*(1-t)*ct1.y + 3*t*sq(1-t)*ct2.y + cb(1-t)*pt2.y

class pt:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return "(%f,%f)" % (self.x, self.y)

if __name__ == "__main__":
    pt1 = pt(0,0)
    ct1 = pt(0.25, 0.1)
    ct2 = pt(0.25, 1.0)
    pt2 = pt(1,1)
    
    part = 100
    with open('ease.txt', 'w') as f:
        for i in range(0,part+1,1):
            x = float(i) / part
            y = value(pt1, ct1, ct2, pt2, x)
            f.write("%f %f\n" % (x,y))