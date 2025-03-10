import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Streamlit app title
st.title(" Google-Style Unit Converter")

# Define unit categories
unit_categories = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch", "centimeter"],
    "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour", "foot/second"],
    "Time": ["second", "minute", "hour", "day"],
}

# Sidebar for selecting unit category
category = st.sidebar.selectbox("Select a category:", list(unit_categories.keys()))

# Select source and target units based on category
units = unit_categories[category]
from_unit = st.selectbox("Convert from:", units)
to_unit = st.selectbox("Convert to:", units)

# Input field for value
value = st.number_input(f"Enter value in {from_unit}:", min_value=1.0, format="%.6f")

# Convert function
def convert_units(value, from_unit, to_unit):
    try:
        if category == "Temperature":
            if from_unit == "celsius" and to_unit == "fahrenheit":
                return value * 9/5 + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                return (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                return value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                return value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                return (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                return (value - 273.15) * 9/5 + 32
            else:
                return value  # Same unit
        else:
            return (value * ureg(from_unit)).to(to_unit).magnitude
    except Exception as e:
        return f"Error: {e}"

# Perform conversion when button is clicked
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")


