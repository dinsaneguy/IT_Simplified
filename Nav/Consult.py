import streamlit as st
def consult():
    specializations = {
        "Diabetes": ["Dr. Alice", "Dr. Bob"],
        "Parkinson": ["Dr. Charlie", "Dr. David"],
        "Heart Diseases": ["Dr. Eve", "Dr. Frank"]
    }

    # Function to display doctors based on selected specialization
    def display_doctors(specialization):
        if specialization in specializations:
            st.write(f"Doctors specializing in {specialization}:")
            for doctor in specializations[specialization]:
                st.write(f"- {doctor}")
        else:
            st.write("No doctors available for this specialization.")

    # Function to handle appointment booking
    def book_appointment(doctor_name, date, time):
        # This function would interact with an appointment booking system
        # For this example, we'll just print the details
        st.write(f"Appointment booked with {doctor_name} on {date} at {time}.")

    # Streamlit app
    st.title('Medical Appointment Booking')

    # Select specialization
    specialization = st.selectbox("Choose a specialization", list(specializations.keys()))

    # Display list of doctors for the selected specialization
    display_doctors(specialization)

    # Appointment booking form
    st.subheader("Book an Appointment")
    doctor_name = st.selectbox("Select Doctor", specializations.get(specialization, []))
    date = st.date_input("Select Date")
    time = st.time_input("Select Time")

    if st.button("Book Appointment"):
        if doctor_name and date and time:
            book_appointment(doctor_name, date, time)
        else:
            st.error("Please fill in all fields.")

    # Additional functionalities can be added as needed
