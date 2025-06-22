print("Hello, World!")

def status():
    """
    Returns the status of the application.
    """
    return "Application is running smoothly."


class Status:
    """
    A class to represent the status of the application.
    """

    def __init__(self):
        self.message = "Application is running smoothly."

    def get_status(self):
        """
        Returns the status message.
        """
        return self.message

def main():
    """
    Main function to demonstrate the status functionality.
    """
    print(status())
    app_status = Status()
    print(app_status.get_status())  

print("Status module loaded successfully.")
print("Running main function...")