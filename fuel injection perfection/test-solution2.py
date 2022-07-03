import timeit

def timer(func):
	"""Print the runtime of the decorated function"""
	#@functools.wraps(func)
	def wrapper_timer(*args, **kwargs):
		start_time = timeit.default_timer()
		value = func(*args, **kwargs)
		run_time = timeit.default_timer() - start_time
		print func.__name__, " ", " in ", run_time, " seconds."
		return value
	return wrapper_timer


m = dict()

def steps(n):
    ops = 0

    key = str(n)
    if key in m.keys():
        return m[key]

    if (n & 1 == 0):
        n >>= 1
    elif ((n == 3) or ((n + 1) & n) > ((n - 1) & (n - 2))):
        n -= 1
    else:
        n += 1

    ops += 1
    
    if (n != 1):
        ops += steps(n)

    m[str(n)] = (ops - 1)
    
    return ops


@timer
def solution1(n):
	global m
	key = str(n)
	if key in m.keys():
		return m[key]

	tempDict = dict()
	tempDict[key] = 0

	n = long(n)

	ops = steps(n)
				
	if (tempDict[key] != ops):
		tempDict[key] = ops

	m.update(tempDict)

	return ops


@timer
def solution2(n):
	#print "solution(%d)" % n
	key = n = long(n)
	ops = 0

	while (n != 1):
		if (n & 1 == 0):
			n >>= 1
		elif ((n == 3) or ((n + 1) & n) > ((n - 1) & (n - 2))):
			n -= 1
		else:
			n += 1
		
		ops += 1

	#print "%d: %d" % (key, ops)
	return ops

