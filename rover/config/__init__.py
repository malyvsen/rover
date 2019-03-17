from rover.config.default import *
try:
    from rover.config.overrides import * # overwrite defaults where override was provided
except ImportError:
    pass
