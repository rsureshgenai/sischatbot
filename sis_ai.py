import streamlit as st

st.set_page_config(page_title="SIS AI Assistant", layout="centered")

# ======================
# SESSION STATE
# ======================
if "role" not in st.session_state:
    st.session_state.role = None

if "step" not in st.session_state:
    st.session_state.step = 0

# ======================
# HEADER
# ======================
st.markdown("## 🌍 SIS AI Assistant")
st.caption("Hiring & Jobs in Europe")

# ======================
# ROLE SELECTION
# ======================
if st.session_state.role is None:

    col1, col2 = st.columns(2)

    if col1.button("🏢 Hire Workers"):
        st.session_state.role = "employer"
        st.session_state.step = 1

    if col2.button("🧑 Get Job"):
        st.session_state.role = "candidate"
        st.session_state.step = 1

# ======================
# EMPLOYER FLOW
# ======================
if st.session_state.role == "employer":

    st.success("Selected: Employer")

    # STEP 1
    if st.session_state.step == 1:
        st.markdown("""
        👋 Welcome Employer!

        What type of workers do you need?
        (Example: Carpenter, Mason, Driver)
        """)

        job = st.text_input("Your answer")

        if job:
            st.session_state.job = job
            st.session_state.step = 2
            st.rerun()

    # STEP 2
    elif st.session_state.step == 2:
        st.markdown(f"""
        👍 Great! You need **{st.session_state.job.title()} workers**

        How many workers do you need?
        """)

        count = st.text_input("Enter number")

        if count.isdigit():
            st.session_state.count = count
            st.session_state.step = 3
            st.rerun()

    # STEP 3
    elif st.session_state.step == 3:
        st.markdown(f"""
        ✅ Perfect!

        👷 Job Role: {st.session_state.job.title()}  
        🔢 Workers Needed: {st.session_state.count}  

        📍 Available Countries:
        Croatia, Serbia, Bulgaria  

        🚀 Next Step:
        Our team will contact you shortly.
        """)

# ======================
# CANDIDATE FLOW
# ======================
elif st.session_state.role == "candidate":

    st.success("Selected: Candidate")

    # STEP 1
    if st.session_state.step == 1:
        st.markdown("""
        👋 Welcome Candidate!

        What job are you looking for?
        (Example: Driver, Helper, Cleaner)
        """)

        job = st.text_input("Your answer")

        if job:
            st.session_state.job = job
            st.session_state.step = 2
            st.rerun()

    # STEP 2
    elif st.session_state.step == 2:
        st.markdown(f"""
        👍 {st.session_state.job.title()} jobs available!

        📍 Countries:
        Croatia, Serbia, Bulgaria, North Macedonia  

        💰 Salary:
        • Unskilled: €700 – €900  
        • Skilled: €1000 – €1200  

        📋 Required Documents:
        • CV  
        • Passport  
        • Experience Certificate  
        • PCC (if required)  

        ⏳ Visa Processing:
        30–90 days (depends on country)

        🚀 Next Step:
        Our team will contact you shortly.
        """)

# ======================
# RESET BUTTON
# ======================
st.markdown("---")
if st.button("🔄 Start Again"):
    st.session_state.role = None
    st.session_state.step = 0
    st.rerun()
