
# Validation function to allow only numbers
def validate_number(input_value):
    if input_value == "":
            return True
    # Return True only if the input is numeric
    return input_value.isdigit()