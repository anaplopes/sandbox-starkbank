class GeradorBrasileiroException(Exception):
    def __init__(self, message: str, status_code: int):
        super(GeradorBrasileiroException, self).__init__(message)
        self.error = "Unknown"
        self.message = message
        self.status_code = status_code


class GeradorBrasileiroRequestException(GeradorBrasileiroException):
    def __init__(self, error: str, message: str, status_code: int):
        super(GeradorBrasileiroRequestException, self).__init__(message, status_code)
        self.error = error
        self.message = message
        self.status_code = status_code
