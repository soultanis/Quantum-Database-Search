# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class ToManyQubits(Error):
   """Raised when the input value is too small"""
   pass

class ValueOutOfRange(Error):
   """Raised when the input value is too large"""
   pass
