def test(origin_method):
    def wrap_test():
        print('{} 실행 전'.format(origin_method.__name__))
        return origin_method
    return wrap_test()

def origin():
    print('origin 실행')

func = test(origin)
func()