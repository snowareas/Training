def test(a, **b) :
    print('a='+str(a)+ ' b='+str(b))

test(a=1)
test(a=1,b=1)
test(a=1,b=2,c=3)

#test(1,a=2)
#test(1,2)

q={'a':1,'b':2,'c':3}

test(**q)
#test(*q)
#test(q)