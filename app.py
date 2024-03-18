from flask import Flask, request, render_template
# Assuming all conversion functions are defined in imp_metric_conversion.py
from imp_metric_conversion import convert_temp, convert_length, convert_weight, convert_volume

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_temp = None
    result_length = None
    result_weight = None
    result_volume = None

    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form.get('from_unit')
            to_unit = request.form.get('to_unit', None)  # to_unit is not used for temperature conversions

            # Determine the type of conversion based on the presence of units in the form data
            if 'celsius' in from_unit or 'fahrenheit' in from_unit:
                result_temp = convert_temp(value, from_unit.replace('_to_', ''))
                result_format = "Celsius" if 'to_celsius' in from_unit else "Fahrenheit"
                result_temp = f"{result_temp:.2f} {result_format}"
            elif any(unit in from_unit for unit in ['miles', 'yards', 'feet', 'inches', 'meters', 'centimeters']):
                result_length = convert_length(value, from_unit, to_unit)
                result_length = f"{result_length:.2f} {to_unit}"
            elif any(unit in from_unit for unit in ['tons', 'pounds', 'ounces', 'kilograms', 'grams']):
                result_weight = convert_weight(value, from_unit, to_unit)
                result_weight = f"{result_weight:.2f} {to_unit}"
            elif any(unit in from_unit for unit in ['gallons', 'quarts', 'pints', 'liters', 'milliliters']):
                result_volume = convert_volume(value, from_unit, to_unit)
                result_volume = f"{result_volume:.2f} {to_unit}"
        except ValueError:
            pass  # Handle invalid input gracefully

    return render_template('index.html', 
                           result_temp=result_temp,
                           result_length=result_length,
                           result_weight=result_weight,
                           result_volume=result_volume)

if __name__ == '__main__':
    app.run(debug=True)
