import random

def jitterate(jitter=0.05, mode='+'):

    # mode: '+' for additive, '*' for multiplicative
    if mode not in ['+', '*']:
        raise ValueError('jitterate: mode must be either "+" or "*".')

    def decorator_with_arbitrary_arguments(function):

        def is_additive(obj):
            return hasattr(obj, '__add__') and callable(obj.__add__)

        def is_multiplicative(obj):
            return hasattr(obj, '__mul__') and callable(obj.__mul__)

        def wrapper_accepting_arguments(*args, **kwargs):
#            print("kwargs:")
#            for kwarg in kwargs:
#                val = kwargs.get(kwarg)
#                print(kwarg, type(kwarg), val, type(val))
#
            jittered_args = list(args)

            if mode == '+':
                for i, arg in enumerate(args):
                    if is_additive(arg):
                        jittered_args[i] += random.uniform(-jitter, jitter)
                    else:
                        print(f'jitterator: arg {i} is not additive, skipping.')
            elif mode == '*':
                for i, arg in enumerate(args):
                    if is_multiplicative(arg):
                        jittered_args[i] *= random.uniform(1-jitter, 1+jitter)
                    else:
                        print(f'jitterator: arg {i} is not multiplicative, skipping.')

            return function(*jittered_args, **kwargs), jittered_args

        return wrapper_accepting_arguments

    return decorator_with_arbitrary_arguments
