from flask import Flask, request, render_template_string
from imp_metric_conversion import Converter

app = Flask(__name__)

html_template = """
<!doctype html>
<html>
<head><title>Unit Conversion</title></head>
<body>
    <h1 style="font-weight: bold;">Imperial to Metric Conversion</h1>
    <form method="post">
        <input type="text" name="value" placeholder="Enter a value" required>
        <select name="unit">
            <option value="fahrenheit">Fahrenheit</option>
            <option value="miles">Miles</option>
            <option value="yards">Yards</option>
            <option value="feet">Feet</option>
            <option value="inches">Inches</option>
            <option value="gallon">Gallons</option>
            <option value="quart">Quarts</option>
            <option value="pint">Pints</option>
            <option value="ton">Tons</option>
            <option value="pound">Pounds</option>
            <option value="ounce">Ounces</option>
        </select>
        <button type="submit">Submit</button>
    </form>
    {% if result %}
        <p style="color: blue;">{{ result }}</p>
    {% endif %}
    <hr>
    <h1 style="font-weight: bold;">Metric to Imperial Conversion</h1>
    <form method="post" action="/metric_to_imperial">
        <input type="text" name="value" placeholder="Enter a value" required>
        <select name="unit">
            <option value="celsius">Celsius</option>
            <option value="kilometers">Kilometers</option>
            <option value="meters">Meters</option>
            <option value="centimeters">Centimeters</option>
            <option value="liter">Liters</option>
            <option value="tonne">Tonne</option>
            <option value="kilogram">Kilogram</option>
            <option value="gram">Gram</option>
        </select>
        <button type="submit">Submit</button>
    </form>
    {% if metric_result %}
        <p style="color: blue;">{{ metric_result }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def imperial_to_metric():
    result = None
    if request.method == "POST":
        try:
            value = int(request.form["value"])
            unit = request.form["unit"]
            converter = Converter()
            result, _ = converter.convert(value, unit, "temperature" if unit in ["fahrenheit", "celsius"] else "length" if unit in ["miles", "yards", "feet", "inches", "kilometers", "meters", "centimeters"] else "volume" if unit in ["gallon", "quart", "pint", "liter"] else "weight")
            result = f"{value} {unit} is {result} {converter.conversions['temperature'][unit][0] if unit in ['fahrenheit', 'celsius'] else converter.conversions['length'][unit][0] if unit in ['miles', 'yards', 'feet', 'inches', 'kilometers', 'meters', 'centimeters'] else converter.conversions['volume'][unit][0] if unit in ['gallon', 'quart', 'pint', 'liter'] else converter.conversions['weight'][unit][0]}"
        except ValueError as e:
            result = "Error: " + str(e)
        except Exception as e:
            result = "An error occurred"
    return render_template_string(html_template, result=result)

@app.route("/metric_to_imperial", methods=["POST"])
def metric_to_imperial():
    metric_result = None
    try:
        value = int(request.form["value"])
        unit = request.form["unit"]
        converter = Converter()
        metric_result, _ = converter.convert(value, unit, "temperature" if unit in ["fahrenheit", "celsius"] else "length" if unit in ["miles", "yards", "feet", "inches", "kilometers", "meters", "centimeters"] else "volume" if unit in ["gallon", "quart", "pint", "liter"] else "weight")
        metric_result = f"{value} {unit} is {metric_result} {converter.conversions['temperature'][unit][0] if unit in ['fahrenheit', 'celsius'] else converter.conversions['length'][unit][0] if unit in ['miles', 'yards', 'feet', 'inches', 'kilometers', 'meters', 'centimeters'] else converter.conversions['volume'][unit][0] if unit in ['gallon', 'quart', 'pint', 'liter'] else converter.conversions['weight'][unit][0]}"
    except ValueError as e:
        metric_result = "Error: " + str(e)
    except Exception as e:
        metric_result = "An error occurred"
    return render_template_string(html_template, metric_result=metric_result)

if __name__ == "__main__":
    app.run(debug=True)
