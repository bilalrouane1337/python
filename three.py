class ApplicationError(Exception):
    pass


class ValidationError(ApplicationError):
    pass


class AgeError(ValidationError):
    pass


exceptions = [
    ApplicationError("General application error"),
    ValidationError("Validation failed"),
    AgeError("Invalid age"),
]

for error in exceptions:
    try:
        raise error
    except AgeError:
        print("Caught: AgeError")
    except ValidationError:
        print("Caught: ValidationError")
    except ApplicationError:
        print("Caught: ApplicationError")
