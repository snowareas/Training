def test(a, *b) :
    print('a='+str(a)+ ' b='+str(b))

test(1)
test(1,2)
test(1,2,3)

q = (0,1,2)
test(*q)
test(q)
