import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="convert_temperature", auth_level=func.AuthLevel.ANONYMOUS)
def convert_temperature(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing temperature conversion request...")

    temp = req.params.get("temperature")
    unit = req.params.get("unit")

    if not temp or not unit:
        return func.HttpResponse("Error: temperature and unit must be provided.", status_code=400)

    try:
        temp = float(temp)
    except ValueError:
        return func.HttpResponse("Error: temperature must be a numeric value.", status_code=400)

    unit_lower = unit.lower()
    if unit_lower == "celsius":
        converted = temp * 9/5 + 32
        converted_unit = "Fahrenheit"
    elif unit_lower == "fahrenheit":
        converted = (temp - 32) * 5/9
        converted_unit = "Celsius"
    else:
        return func.HttpResponse(f"Error: invalid unit '{unit}'. Must be 'Celsius' or 'Fahrenheit'.", status_code=400)

    return func.HttpResponse(f"{temp} {unit} => {converted:.2f} {converted_unit}", mimetype="text/plain", status_code=200)
