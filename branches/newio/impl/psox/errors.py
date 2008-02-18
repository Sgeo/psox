class PSOXError(Exception): pass

class IllegalPSOXError(PSOXError): pass
class UnsupportedVersionError(PSOXError): pass
class ImproperTypeError(IllegalPSOXError): pass
