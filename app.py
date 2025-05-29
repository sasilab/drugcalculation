import streamlit as st

def calculate_infusion_rate(concentration_mg_per_ml, dose_value, dose_unit, weight_kg):
    # Convert dose to mg/kg/min if it's in microgram
    if dose_unit == "µg/kg/min":
        dose_mg_per_kg_per_min = dose_value / 1000  # convert microgram to mg
    else:
        dose_mg_per_kg_per_min = dose_value

    # Calculate total dose in mg/min
    total_dose_mg_per_min = dose_mg_per_kg_per_min * weight_kg

    # Calculate ml/min and ml/hour
    ml_per_min = total_dose_mg_per_min / concentration_mg_per_ml
    ml_per_hour = ml_per_min * 60
    return ml_per_min, ml_per_hour

st.title("💉 IV Infusion Rate Calculator")

st.markdown("""
This app calculates the **infusion rate** (ml/min and ml/hour) based on:
- Drug concentration (mg/ml)
- Dose (µg/kg/min or mg/kg/min)
- Patient weight (kg)
""")

# Inputs
concentration = st.number_input("🔬 Drug concentration (mg/ml)", min_value=0.01, value=1.0, step=0.01)
dose_value = st.number_input("💊 Dose", min_value=0.001, value=5.0, step=0.1)
dose_unit = st.selectbox("Dose unit", ["µg/kg/min", "mg/kg/min"])
weight = st.number_input("⚖️ Patient weight (kg)", min_value=0.1, value=70.0, step=0.1)

# Calculate
if st.button("🧮 Calculate Infusion Rate"):
    ml_per_min, ml_per_hour = calculate_infusion_rate(concentration, dose_value, dose_unit, weight)

    st.success("💡 Infusion Rate:")
    st.write(f"**{ml_per_min:.2f} ml/min**")
    st.write(f"**{ml_per_hour:.2f} ml/hour**")
