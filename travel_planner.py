import streamlit as st

# App title
st.title("AI-Powered Travel Planner")
st.subheader("Personalized Itineraries Made Just for You!")

# Step 1: Gather basic details
st.write("### Step 1: Tell me about your trip")
destination = st.text_input("Where are you planning to travel?")
duration = st.number_input("How many days will your trip last?", min_value=1)
budget = st.selectbox("What’s your budget?", ["Luxury", "Mid-range", "Budget-friendly"])
purpose = st.text_input("What’s the purpose of your trip? (e.g., leisure, adventure)")
preferences = st.text_area("Any specific preferences? (e.g., food, history, hidden gems)")

# Step 2: Refine inputs
if destination and duration and budget and purpose:
    st.write("### Step 2: Refining your preferences")
    dietary = st.text_input("Do you have any dietary restrictions?")
    accommodation = st.selectbox("What kind of accommodation do you prefer?", ["Luxury", "Budget-friendly", "Central location"])
    mobility = st.radio("Are you okay with walking a lot?", ["Yes", "No"])
    hidden_gems = st.checkbox("Do you want to explore hidden gems?")

    # Step 3: Generate itinerary
    if st.button("Generate Itinerary"):
        st.write("### Your Personalized Itinerary")
        st.write(f"**Destination:** {destination}")
        st.write(f"**Duration:** {duration} days")
        st.write(f"**Budget:** {budget}")
        st.write(f"**Purpose:** {purpose}")
        st.write(f"**Preferences:** {preferences}")

        st.write("#### Sample Itinerary")
        st.write("**Day 1:** Morning at Landmark A, lunch at Local Restaurant B, and afternoon exploring Hidden Gem C.")

        # Add more detailed itinerary generation by integrating OpenAI (optional)
