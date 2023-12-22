from ini import generate_engine


class DefaultInterface:
    def __init__(self):
        self.connection = generate_engine()

    def __del__(self):
        try:
            self.connection.dispose()
        except Exception as ex:
            print(ex)
