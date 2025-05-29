import streamlit as st

def convert_concentration(value, unit):
    # Convert to mg/ml
    return value / 1000 if unit == "µg/ml" else value

def convert_dose(value, unit):
    # Convert to mg/kg/min
    return value / 1000 if unit == "µg/kg/min" else value

def calculate_infusion_rate(concentration_value, concentration_unit, dose_value, dose_unit, weight_kg):
    concentration_mg_per_ml = convert_concentration(concentration_value, concentration_unit)
    dose_mg_per_kg_per_min = convert_dose(dose_value, dose_unit)

    total_dose_mg_per_min = dose_mg_per_kg_per_min * weight_kg
    ml_per_min = total_dose_mg_per_min / concentration_mg_per_ml
    ml_per_hour = ml_per_min * 60
    return ml_per_min, ml_per_hour

st.title("💉 IV Infusion Rate Calculator")

st.markdown("""
This app calculates the **infusion rate** (ml/min and ml/hour) based on:
- Drug concentration (µg/ml or mg/ml)
- Dose (µg/kg/min or mg/kg/min)
- Patient weight (kg)
""")

# Inputs
concentration_value = st.number_input("🔬 Drug concentration", min_value=0.001, value=1000.0, step=0.1)
concentration_unit = st.selectbox("Concentration unit", ["mg/ml", "µg/ml"])

dose_value = st.number_input("💊 Dose", min_value=0.001, value=5.0, step=0.1)
dose_unit = st.selectbox("Dose unit", ["µg/kg/min", "mg/kg/min"])

weight = st.number_input("⚖️ Patient weight (kg)", min_value=0.1, value=70.0, step=0.1)

# Calculate
if st.button("🧮 Calculate Infusion Rate"):
    try:
        ml_per_min, ml_per_hour = calculate_infusion_rate(concentration_value, concentration_unit, dose_value, dose_unit, weight)
        st.success("💡 Infusion Rate:")
        st.write(f"**{ml_per_min:.2f} ml/min**")
        st.write(f"**{ml_per_hour:.2f} ml/hour**")
    except ZeroDivisionError:
        st.error("Drug concentration cannot be zero.")
