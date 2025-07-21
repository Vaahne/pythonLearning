
def divide_by_zero(filename):

    try:

        with open(filename) as f:
            data = f.readlines()
            
        if len(data) < 2:
            raise ValueError("Not enough data")

        num1 = int(data[0])
        num2 = int(data[1])

        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
            
        return num1/num2
    except FileNotFoundError:
        return "Error: File not found"
    except ValueError as v:
        return f"Value Error: {v}"
    except ZeroDivisionError as zde:
        return f"Division err: {zde}"

