class StarkBankException(Exception):
    def __init__(self, message: str, status_code: int):
        super(StarkBankException, self).__init__(message)
        self.error = "Unknown"
        self.message = message
        self.status_code = status_code


class StarkbankRequestException(StarkBankException):
    def __init__(self, error: str, message: str, status_code: int):
        super(StarkbankRequestException, self).__init__(message, status_code)
        self.error = error
        self.message = message
        self.status_code = status_code
