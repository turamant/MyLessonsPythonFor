class CustomError(Exception):
    pass


age = 1

if age == 1:
    raise CustomError("This is custom error")
