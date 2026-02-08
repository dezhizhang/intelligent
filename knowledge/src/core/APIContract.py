from src.core.response_code import ResponseCode


class APIContract:
    @staticmethod
    def success(data):
        return {
            "status": "success",
            "code": ResponseCode.SUCCESS,
            "message": "Request was successful",
            "data": data
        }

    @staticmethod
    def failure(data, msg):
        return {
            "status": "failure",
            "code": ResponseCode.FAILED,
            "message": msg,
        }
