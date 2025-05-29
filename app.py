import streamlit as st

def convert_length(value, from_unit, to_unit):

    length_factors = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254,
        'nautical miles': 1852
    }

    return value * length_factors[from_unit] / length_factors[to_unit]

def convert_weight(value, from_unit, to_unit):

    weight_factors = {
        'kilograms': 1,
        'grams': 0.001,
        'milligrams': 1e-6,
        'pounds': 0.453592,
        'ounces': 0.0283495,
        'tons': 907.185,
        'metric tons': 1000,
        'carats': 0.0002
    }

    return value * weight_factors[from_unit] / weight_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):

    if from_unit == 'Celsius':

        if to_unit == 'Fahrenheit':

            return (value * 9/5) + 32
        
        elif to_unit == 'Kelvin':

            return value + 273.15
        
        else:

            return value
        
    elif from_unit == 'Fahrenheit':

        if to_unit == 'Celsius':

            return (value - 32) * 5/9
        
        elif to_unit == 'Kelvin':

            return (value - 32) * 5/9 + 273.15
        
        else:

            return value
        
    elif from_unit == 'Kelvin':

        if to_unit == 'Celsius':

            return value - 273.15
        
        elif to_unit == 'Fahrenheit':

            return (value - 273.15) * 9/5 + 32
        
        else:

            return value
        
    else:

        return value
    

def convert_area(value, from_unit, to_unit):

    area_factors = {
        'square meters': 1,
        'square kilometers': 1e6,
        'square miles': 2589988.11,
        'acres': 4046.86,
        'hectares': 10000,
        'square yards': 0.836127,
        'square feet': 0.092903,
        'square inches': 0.00064516
    }

    return value * area_factors[from_unit] / area_factors[to_unit]

def convert_volume(value, from_unit, to_unit):

    volume_factors = {
        'liters': 1,
        'milliliters': 0.001,
        'cubic meters': 1000,
        'cubic centimeters': 0.001,
        'cubic feet': 28.3168,
        'cubic inches': 0.0163871,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.24
    }

    return value * volume_factors[from_unit] / volume_factors[to_unit]

def convert_time(value, from_unit, to_unit):

    time_factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'months': 2629800,
        'years': 31557600

    }
    return value * time_factors[from_unit] / time_factors[to_unit]

# Streamlit UI
st.set_page_config(page_title="Universal Unit Converter", page_icon="📐", layout="centered")

st.title("📐 Universal Unit Converter")

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background: linear-gradient(45deg, #4a5568, #2d3748);
        color: white;
    }
    .sidebar .sidebar-content {
        color: white;
    }
    h1 {
        color: #2d3748;
    }
</style>
            
""", unsafe_allow_html=True)

with st.sidebar:

    st.header("Settings")

    category = st.selectbox("Select Conversion Category", [
        "Length",
        "Weight",
        "Temperature",
        "Area",
        "Volume",
        "Time"
    ])

conversion_functions = {
    "Length": convert_length,
    "Weight": convert_weight,
    "Temperature": convert_temperature,
    "Area": convert_area,
    "Volume": convert_volume,
    "Time": convert_time
}

unit_options = {
    "Length": ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches', 'nautical miles'],
    "Weight": ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces', 'tons', 'metric tons', 'carats'],
    "Temperature": ['Celsius', 'Fahrenheit', 'Kelvin'],
    "Area": ['square meters', 'square kilometers', 'square miles', 'acres', 'hectares', 'square yards', 'square feet', 'square inches'],
    "Volume": ['liters', 'milliliters', 'cubic meters', 'cubic centimeters', 'cubic feet', 'cubic inches', 'gallons', 'quarts', 'pints', 'cups'],
    "Time": ['seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years']
}

col1, col2 = st.columns(2)

with col1:

    from_unit = st.selectbox("From", unit_options[category], key="from_unit")

    value = st.number_input("Value", min_value=0.0, value=1.0, step=0.1, key="value")

with col2:

    to_unit = st.selectbox("To", unit_options[category], key="to_unit")

if from_unit == to_unit:

    result = value

else:
    conversion_func = conversion_functions[category]

    result = conversion_func(value, from_unit, to_unit)

st.markdown("---")

st.subheader("Conversion Result")

st.markdown(f"### {value:.2f} {from_unit} = {result:.4f} {to_unit}")

st.success("Conversion completed successfully!")

st.markdown("---")

st.markdown("""
**Features:**
- Convert between 6 different measurement categories
- Over 50 supported units
- Real-time calculations
- Professional interface
- Precise decimal formatting
""")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: green;'>Made by MUHAMMAD ABDUR REHMAN</p>", unsafe_allow_html=True)
