class NotFoundError(Exception):
    def __init__(self, message="Recurso não encontrado", status_code=404):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {
            "error": self.message
        }