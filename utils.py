import os

class Utils():

    @staticmethod
    def get_base_dir():
        return os.path.dirname(__file__)

    @staticmethod
    def read_file(filepath):

        try:

            file = open(file=filepath, mode="r")
            return file.read()
        except FileNotFoundError and FileExistsError:

            panic_msg = 'The system has been returned a unexpected error'
            raise FileNotFoundError(panic_msg) or FileExistsError(panic_msg)
        