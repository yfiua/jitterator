import random

def jitterate(jitter=0.05, mode='+'):
    def decorator_with_arbitrary_arguments(function):
        def wrapper_accepting_arguments(*args, **kwargs):
            print(f'Inside jitterator. jitter = {jitter}, mode = {mode}')

#            print("kwargs:")
#            for kwarg in kwargs:
#                val = kwargs.get(kwarg)
#                print(kwarg, type(kwarg), val, type(val))
#

            jittered_args = list(args)
            for i, arg in enumerate(args):
                if isinstance(arg, (int, float)):
                    jittered_args[i] += random.uniform(-jitter, jitter)
                else:
                    print(f'jitterator: arg {i} is not additive, skipping.')

            return function(*jittered_args, **kwargs), jittered_args

        return wrapper_accepting_arguments

    return decorator_with_arbitrary_arguments
