class RemoteNotAvailableException(Exception):
    """Exception raised when the remote service is not available."""

    def __init__(self, name: str, message="Remote service '{name}' is not available."):
        self.message = message.format(name=name)
        super().__init__(self.message)
