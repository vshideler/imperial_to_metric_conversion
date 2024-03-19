class Converter:
    """
    A class to convert values between different units of measurement.
    Supports temperature, length, volume, and weight conversions.
    """
    def __init__(self):
        """
        Initializes the Converter class with dictionaries mapping units
        within categories to their target unit and conversion function.
        """
        self.conversions = {
            'temperature': {
                'celsius': ('fahrenheit', self.celsius_to_fahrenheit),
                'fahrenheit': ('celsius', self.fahrenheit_to_celsius),
            },
            'length': {
                'kilometers': ('miles', self.kilometers_to_miles),
                'miles': ('kilometers', self.miles_to_kilometers),
                'yards': ('meters', self.yards_to_meters),
                'meters': ('yards', self.meters_to_yards),
                'feet': ('meters', self.feet_to_meters),
                'inches': ('centimeters', self.inches_to_centimeters),
                'centimeters': ('inches', self.centimeters_to_inches),
            },
            'volume': {
                'gallon': ('liter', self.gallon_to_liter),
                'liter': ('gallon', self.liter_to_gallon),
                'quart': ('liter', self.quart_to_liter),
                'pint': ('liter', self.pint_to_liter),
            },
            'weight': {
                'ton': ('tonne', self.ton_to_tonne),
                'tonne': ('ton', self.tonne_to_ton),
                'pound': ('kilogram', self.pound_to_kilogram),
                'kilogram': ('pound', self.kilogram_to_pound),
                'ounce': ('gram', self.ounce_to_gram),
                'gram': ('ounce', self.gram_to_ounce),
            }
        }

    def convert(self, value, from_unit, category):
        """
        Converts a given value from one unit to another within a specified category.

        Parameters:
        - value: The numerical value to convert.
        - from_unit: The unit of the value to convert from.
        - category: The category of the conversion (e.g., 'temperature').

        Returns:
        A tuple of the converted value and its unit.
        """
        if category in self.conversions and from_unit in self.conversions[category]:
            to_unit, conversion_function = self.conversions[category][from_unit]
            result = conversion_function(value)
            return result, to_unit
        else:
            raise ValueError("Unsupported unit or category for conversion")

    """
    Temperature Conversion
    """

    @staticmethod
    def celsius_to_fahrenheit(value):
        return round((value * 9 / 5) + 32, 2)

    @staticmethod
    def fahrenheit_to_celsius(value):
        return round((value - 32) * 5 / 9, 2)

    """
    Distance Conversion
    """

    @staticmethod
    def kilometers_to_miles(value):
        return round(value * 0.621371, 2)

    @staticmethod
    def miles_to_kilometers(value):
        return round(value / 0.621371, 2)

    @staticmethod
    def yards_to_meters(value):
        return round(value * 0.9144, 2)

    @staticmethod
    def meters_to_yards(value):
        return round(value / 0.9144, 2)

    @staticmethod
    def feet_to_meters(value):
        return round(value * 0.3048, 2)

    @staticmethod
    def inches_to_centimeters(value):
        return round(value * 2.54, 2)

    @staticmethod
    def centimeters_to_inches(value):
        return round(value / 2.54, 2)

    """
    Volume Conversion
    """

    @staticmethod
    def gallon_to_liter(value):
        return round(value * 3.785, 2)

    @staticmethod
    def liter_to_gallon(value):
        return round(value / 3.785, 2)

    @staticmethod
    def quart_to_liter(value):
        return round(value * 0.946353, 2)

    @staticmethod
    def pint_to_liter(value):
        return round(value * 0.473176, 2)

    """
    Weight Conversion
    """

    @staticmethod
    def ton_to_tonne(value):
        return round(value * 0.907185, 2)

    @staticmethod
    def tonne_to_ton(value):
        return round(value / 0.907185, 2)

    @staticmethod
    def pound_to_kilogram(value):
        return round(value * 0.453592, 2)

    @staticmethod
    def kilogram_to_pound(value):
        return round(value / 0.453592, 2)

    @staticmethod
    def ounce_to_gram(value):
        return round(value * 28.3495, 2)

    @staticmethod
    def gram_to_ounce(value):
        return round(value / 28.3495, 2)
