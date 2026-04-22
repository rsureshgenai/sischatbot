import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="SIS AI Assistant", layout="centered")

# =========================
# UI STYLE
# =========================
st.markdown("""
<style>
.block-container {
    max-width: 700px;
    padding-top: 1rem;
}

/* Chat bubble */
.chat {
    background:#F2DDE3;
    padding:14px;
    border-radius:12px;
    margin-top:10px;
    color:#000;
    font-size:14px;
    line-height:1.6;
}

/* Selected badge */
.selected {
    background:#1E3A8A;
    color:white;
    padding:6px 12px;
    border-radius:8px;
    display:inline-block;
    margin-bottom:10px;
    font-size:13px;
}

/* Mobile fix */
.stTextInput {
    position: sticky;
    bottom: 0;
    background-color: #0E1117;
    padding-bottom: 10px;
}

@media (max-width:768px){
    .block-container{
        padding:1rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "step" not in st.session_state:
    st.session_state.step = "start"

if "user_type" not in st.session_state:
    st.session_state.user_type = ""

if "job" not in st.session_state:
    st.session_state.job = ""

if "count" not in st.session_state:
    st.session_state.count = ""

if "industry" not in st.session_state:
    st.session_state.industry = ""

# =========================
# HEADER
# =========================
st.markdown("<h3 style='text-align:center;color:#4F46E5;'>🌍 SIS AI Assistant</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Hiring & Jobs in Europe</p>", unsafe_allow_html=True)
st.markdown("---")

# =========================
# USER TYPE SELECTION
# =========================
col1, col2 = st.columns(2)

with col1:
    if st.button("🏢 Hire Workers"):
        st.session_state.user_type = "Employer"
        st.session_state.step = "ask_workers"

with col2:
    if st.button("👷 Get Job"):
        st.session_state.user_type = "Candidate"
        st.session_state.step = "ask_job"

# SHOW SELECTED
if st.session_state.user_type:
    st.markdown(f"<div class='selected'>Selected: {st.session_state.user_type}</div>", unsafe_allow_html=True)

# =========================
# INPUT
# =========================
user_input = st.text_input("Type your answer...")

# =========================
# 👷 CANDIDATE FLOW
# =========================
if st.session_state.user_type == "Candidate":

    # STEP 1
    if st.session_state.step == "ask_job":
        st.markdown("<div class='chat'>👋 Which job are you looking for?</div>", unsafe_allow_html=True)

        if user_input:
            st.session_state.job = user_input
            st.session_state.step = "job_info"
            st.rerun()

    # STEP 2
    elif st.session_state.step == "job_info":
        st.markdown(f"""
        <div class='chat'>
        👍 <b>Job:</b> {st.session_state.job.title()} <br><br>

        📍 Countries: Croatia, Serbia, Bulgaria, North Macedonia <br>
        💰 Salary: €700 – €1200 <br>
        📄 Visa: 30–60 days <br><br>

        👉 You can type:
        • documents  
        • salary  
        • apply  
        • change job
        </div>
        """, unsafe_allow_html=True)

        if user_input:
            txt = user_input.lower()

            if "document" in txt:
                st.session_state.step = "documents"

            elif "salary" in txt:
                st.session_state.step = "salary"

            elif "apply" in txt:
                st.session_state.step = "apply"

            elif "change" in txt:
                st.session_state.step = "ask_job"

            else:
                # Accept ANY new job
                st.session_state.job = user_input
                st.session_state.step = "job_info"

            st.rerun()

    # STEP 3
    elif st.session_state.step == "documents":
        st.markdown("""
        <div class='chat'>
        📄 Documents Required:<br><br>
        • CV<br>
        • Passport<br>
        • Education Certificate<br>
        • Experience Certificate<br>
        • PCC (depending on country)<br>
        • Medical (optional)
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.step == "salary":
        st.markdown("""
        <div class='chat'>
        💰 Salary Range:<br><br>
        • Unskilled: €700 – €900<br>
        • Skilled: €1000 – €1200
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.step == "apply":
        st.markdown("""
        <div class='chat'>
        🚀 Next Step:<br><br>
        Please contact our team to start your application process.
        </div>
        """, unsafe_allow_html=True)


# =========================
# 🏢 EMPLOYER FLOW
# =========================
elif st.session_state.user_type == "Employer":

    # STEP 1
    if st.session_state.step == "ask_workers":
        st.markdown("<div class='chat'>👋 How many workers do you need?</div>", unsafe_allow_html=True)

        if user_input:
            st.session_state.count = user_input
            st.session_state.step = "ask_industry"
            st.rerun()

    # STEP 2
    elif st.session_state.step == "ask_industry":
        st.markdown(f"""
        <div class='chat'>
        👍 Workers needed: {st.session_state.count} <br><br>

        Which industry?<br>
        • Construction<br>
        • Hospitality<br>
        • Factory<br>
        • Warehouse<br><br>

        👉 You can type any industry
        </div>
        """, unsafe_allow_html=True)

        if user_input:
            st.session_state.industry = user_input
            st.session_state.step = "employer_info"
            st.rerun()

    # STEP 3
    elif st.session_state.step == "employer_info":
        st.markdown(f"""
        <div class='chat'>
        👍 Industry: {st.session_state.industry.title()} <br><br>

        📍 Countries: Croatia, Serbia, Bulgaria <br>
        ⏱ Hiring Time: 15–30 days <br><br>

        👉 Our team will assist you further.
        </div>
        """, unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<p style='text-align:center;color:gray;margin-top:20px;font-size:12px;'>
⚡ SIS AI • Powered by SIS International Recruiters
</p>
""", unsafe_allow_html=True)