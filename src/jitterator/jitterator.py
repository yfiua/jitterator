import numpy as np

def jitterate(jitter=0.05, mode='+'):

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

            # check if jitter is a list / numpy array or a single value
            if isinstance(jitter, list) or isinstance(jitter, np.ndarray):
                if len(jitter) != len(args):
                    raise ValueError('jitterate: jitter list must be same length as args.')
            else:
                jitter = [jitter] * len(args)

            # check if mode is a list or a single value
            if isinstance(mode, list):
                if len(mode) != len(args):
                    raise ValueError('jitterate: mode list must be same length as args.')
            else:
                if mode != '+' and mode != '*':
                    raise ValueError('jitterate: mode must be "+" or "*".')

                mode = [mode] * len(args)

            # jitterate args
            for i, arg in enumerate(args):
                if mode[i] == '+':
                    if is_additive(arg):
                        jittered_args[i] = jittered_args[i] + np.random.uniform(-jitter[i], jitter[i])
                    else:
                        print(f'jitterator: arg {i} is not additive, skipping.')
                elif mode[i] == '*':
                    if is_multiplicative(arg):
                        jittered_args[i] = jittered_args[i] * np.random.uniform(1-jitter[i], 1+jitter[i])
                    else:
                        print(f'jitterator: arg {i} is not multiplicative, skipping.')
                else:
                    raise ValueError(f'jitterate: mode {i} is neither "+" nor "*".')

            return function(*jittered_args, **kwargs), jittered_args

        return wrapper_accepting_arguments

    return decorator_with_arbitrary_arguments
