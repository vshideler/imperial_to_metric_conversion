def convert_length(value, from_unit, to_unit):
    length_factors = {
        'miles': 1.60934,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }

    if from_unit in length_factors and to_unit == 'meters':
        return value * length_factors[from_unit]
    elif from_unit == 'meters' and to_unit in length_factors:
        return value / length_factors[to_unit]
    else:
        return None  # Conversion not supported

def convert_weight(value, from_unit, to_unit):
    weight_factors = {
        'tons': 907.185,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }

    if from_unit in weight_factors and to_unit == 'kilograms':
        return value * weight_factors[from_unit]
    elif from_unit == 'kilograms' and to_unit in weight_factors:
        return value / weight_factors[to_unit]
    else:
        return None  # Conversion not supported

def convert_volume(value, from_unit, to_unit):
    volume_factors = {
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176
    }

    if from_unit in volume_factors and to_unit == 'liters':
        return value * volume_factors[from_unit]
    elif from_unit == 'liters' and to_unit in volume_factors:
        return value / volume_factors[to_unit]
    else:
        return None  # Conversion not supported

def convert_temp(value, from_unit):
    if from_unit == 'celsius':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit':
        return (value - 32) * 5/9
    else:
        return None  # Conversion not supported
