
def a(ll, from_=0):
    if len(ll) == 3:
        return [ll]

    ret = []
    for i in range(from_,len(ll)):
        la = ll[:i] + ll[i+1:]
        ret += a(la, i)

    return ret


r = a([1, 2, 3, 4, 5])
print(r)
