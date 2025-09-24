import streamlit as st

# Emission factors for different vehicles (kgCO2/km)
EMISSION_FACTORS = {
    "Car (Petrol)": 0.192,
    "Car (Diesel)": 0.171,
    "Motorbike": 0.103,
    "Bus": 0.089,
    "Train": 0.041,
    "Bicycle/Walking": 0.0,
    "Electric Vehicle": 0.05
}

st.set_page_config(layout="wide")

st.title("🚗 Personal Carbon Calculator – Transportation Only")

# Vehicle selection
st.subheader("Select Your Vehicle Type")
vehicle = st.selectbox("Vehicle", list(EMISSION_FACTORS.keys()))

# Daily distance input
st.subheader("Enter Your Daily Travel Distance (in km)")
distance = st.slider("Distance", 0.0, 200.0, key="distance_input")

# Normalize distance (convert daily to yearly)
yearly_distance = distance * 365

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[vehicle] * yearly_distance
transportation_emissions = round(transportation_emissions / 1000, 2)  # convert to tonnes

if st.button("Calculate CO2 Emissions"):
    st.header("Results")
    st.info(
        f"🚙 Your selected vehicle: **{vehicle}**\n\n"
        f"📏 Yearly distance: **{yearly_distance} km**\n\n"
        f"🌍 Transportation Carbon Footprint: **{transportation_emissions} tonnes CO2 per year**"
    )

    st.warning(
        "Note: Transport emissions vary by fuel efficiency, maintenance, and driving habits. "
        "Switching to public transport or EVs can significantly reduce your footprint."
    )
