import streamlit as st

st.set_page_config(page_title="SIS AI Assistant", layout="centered")

# ======================
# SESSION STATE
# ======================
if "role" not in st.session_state:
    st.session_state.role = None

if "step" not in st.session_state:
    st.session_state.step = 0

if "job" not in st.session_state:
    st.session_state.job = ""

if "count" not in st.session_state:
    st.session_state.count = ""

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

    with col1:
        if st.button("🏢 Hire Workers"):
            st.session_state.role = "employer"
            st.session_state.step = 1
            st.rerun()

    with col2:
        if st.button("🧑 Get Job"):
            st.session_state.role = "candidate"
            st.session_state.step = 1
            st.rerun()

# ======================
# EMPLOYER FLOW
# ======================
elif st.session_state.role == "employer":

    st.success("Selected: Employer")

    # STEP 1 → Job role
    if st.session_state.step == 1:
        st.markdown("""
        👋 Welcome Employer!

        What type of workers do you need?
        (Example: Carpenter, Mason, Driver)
        """)

        job = st.text_input("Your answer", key="emp_job")

        if job:
            st.session_state.job = job
            st.session_state.step = 2
            st.rerun()

    # STEP 2 → Count
    elif st.session_state.step == 2:
        st.markdown(f"""
        👍 Great! You need **{st.session_state.job.title()} workers**

        How many workers do you need?
        """)

        count = st.text_input("Enter number", key="emp_count")

        if count.isdigit():
            st.session_state.count = count
            st.session_state.step = 3
            st.rerun()

    # STEP 3 → Final
    elif st.session_state.step == 3:
        st.markdown(f"""
        ✅ Perfect!

        👷 Job Role: {st.session_state.job.title()}  
        🔢 Workers Needed: {st.session_state.count}  

        📍 Available Countries:
        Croatia, Serbia, Bulgaria  
        """)

        st.markdown("### 🚀 Contact Our Team")

        col1, col2 = st.columns(2)

        with col1:
            st.link_button("📞 Call Now", "tel:+385993665624")

        with col2:
            st.link_button(
                "💬 WhatsApp",
                f"https://wa.me/385993665624?text=Hi%20I%20need%20{st.session_state.count}%20{st.session_state.job}%20workers"
            )

# ======================
# CANDIDATE FLOW
# ======================
elif st.session_state.role == "candidate":

    st.success("Selected: Candidate")

    # STEP 1 → Job role
    if st.session_state.step == 1:
        st.markdown("""
        👋 Welcome Candidate!

        What job are you looking for?
        (Example: Driver, Helper, Cleaner)
        """)

        job = st.text_input("Your answer", key="can_job")

        if job:
            st.session_state.job = job
            st.session_state.step = 2
            st.rerun()

    # STEP 2 → Final
    elif st.session_state.step == 2:
        st.markdown(f"""
        👍 {st.session_state.job.title()} jobs available!

        📍 Countries:
        Croatia, Serbia, Bulgaria, North Macedonia  

        💰 Salary:
        • Unskilled: €700 – €900  
        • Skilled: €1000 – €1200  

        📋 Required Documents:
        • CV (with education details)  
        • Passport  
        • Education Certificate  
        • Experience Certificate  
        • Trade Certificate (added advantage)  
        • PCC (Police Clearance – depends on country)  
        • Medical Certificate (optional)  

        ⏳ Visa Processing:
        30–90 days (depends on country)
        """)

        st.markdown("### 🚀 Apply Now")

        col1, col2 = st.columns(2)

        with col1:
            st.link_button("📞 Call Now", "tel:+919994562962")

        with col2:
            st.link_button(
                "💬 WhatsApp Apply",
                f"https://wa.me/919994562962?text=Hi%20I%20want%20to%20apply%20for%20{st.session_state.job}%20job"
            )

# ======================
# RESET BUTTON
# ======================
st.markdown("---")

if st.button("🔄 Start Again"):
    st.session_state.role = None
    st.session_state.step = 0
    st.session_state.job = ""
    st.session_state.count = ""
    st.rerun()
