import random
import numpy as np

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
            nonlocal jitter, mode

            jittered_args = list(args)

            # test if jitter is a list / numpy array or a single value
            if isinstance(jitter, list) or isinstance(jitter, np.ndarray):
                if len(jitter) != len(args):
                    raise ValueError('jitterate: jitter list must be same length as args.')
            else:
                jitter = [jitter] * len(args)

            if mode == '+':
                for i, arg in enumerate(args):
                    if is_additive(arg):
                        jittered_args[i] = jittered_args[i] + random.uniform(-jitter[i], jitter[i])
                    else:
                        print(f'jitterator: arg {i} is not additive, skipping.')
            elif mode == '*':
                for i, arg in enumerate(args):
                    if is_multiplicative(arg):
                        jittered_args[i] = jittered_args[i] * random.uniform(1-jitter[i], 1+jitter[i])
                    else:
                        print(f'jitterator: arg {i} is not multiplicative, skipping.')

            return function(*jittered_args, **kwargs), jittered_args

        return wrapper_accepting_arguments

    return decorator_with_arbitrary_arguments
