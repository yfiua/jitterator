import random

def jitterate(jitter=0.05, mode='+'):
    def decorator_with_arbitrary_arguments(function):
        def wrapper_accepting_arguments(*args, **kwargs):
            print(f'Inside jitterator. jitter = {jitter}, mode = {mode}')

            print("args:")
            for arg in args:
                print(f'type = {type(arg)}, value = {arg}')

#            print("kwargs:")
#            for kwarg in kwargs:
#                val = kwargs.get(kwarg)
#                print(kwarg, type(kwarg), val, type(val))
#

            jittered_args = list(args)
            for i, arg in enumerate(args):
                if isinstance(arg, (int, float)):
                    jittered_args[i] += random.uniform(-jitter, jitter)

            print("jittered args:")
            for arg in jittered_args:
                print(f'type = {type(arg)}, value = {arg}')

            return function(*jittered_args, **kwargs)

        return wrapper_accepting_arguments

    return decorator_with_arbitrary_arguments
