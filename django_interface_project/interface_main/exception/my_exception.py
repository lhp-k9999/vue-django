class ErrorCode:
    DB      = 10000
    UNKNOWN = 30000
    COMMON  = 40000
    SYSTEM  = 50000

class MyException(Exception):
    def __init__(self, code=ErrorCode.COMMON, message='参数错误'):
        self.message = message
        self.code = code

    def __str__(self):
        return self.message
