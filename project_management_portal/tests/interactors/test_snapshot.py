def int_add():
    a,b = 100,100
    return a+b

def int_mul():
    a,b = 100,100
    return a*b

def float_add():
    a,b = 11.1,11.1
    return a+b

def my_fuc():
    return 2

def test_mything(snapshot):
    return_value = my_fuc()
    snapshot.assert_match(return_value, 'test_mything')

def test_int_add(snapshot):
    return_value = int_add()
    snapshot.assert_match(return_value, 'int_add')

def test_int_mul(snapshot):
    return_value = int_mul()
    snapshot.assert_match(return_value, 'int_mul')

def test_float_add(snapshot):
    return_value = float_add()
    snapshot.assert_match(return_value, 'float_add')
