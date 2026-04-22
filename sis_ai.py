import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SIS AI Assistant", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

/* Container */
.block-container {
    max-width: 700px;
    margin: auto;
    padding-top: 3rem !important;
}

/* Title animation */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-5px); }
    100% { transform: translateY(0px); }
}

.title-emoji {
    display:inline-block;
    animation: float 2s infinite;
}

/* Chat box */
.chat-box {
    background-color: #F2DDE3;
    padding: 16px;
    border-radius: 14px;
    margin-top: 15px;
    color: black;
    animation: fadeIn 0.4s ease-in-out;
}

@keyframes fadeIn {
    from {opacity:0; transform: translateY(10px);}
    to {opacity:1; transform: translateY(0);}
}

/* Input */
.stTextInput input {
    border-radius: 12px;
    padding: 10px;
}

/* Mobile */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("""
<h2 style='text-align:center; font-size:28px;'>
<span class='title-emoji'>🌍</span> SIS AI Assistant
</h2>
<p style='text-align:center; color:gray;'>Hiring & Jobs in Europe</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- SESSION ----------
if "role" not in st.session_state:
    st.session_state.role = None

# ---------- ROLE SELECTION ----------
if st.session_state.role is None:

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        c1, c2 = st.columns(2)

        with c1:
            if st.button("🏢 Hire Workers"):
                st.session_state.role = "employer"

        with c2:
            if st.button("👨‍💼 Get Job"):
                st.session_state.role = "candidate"

# ---------- AFTER SELECTION ----------
if st.session_state.role == "employer":

    st.success("Selected: Employer")

    st.markdown("""
<div class="chat-box">
👋 Welcome Employer!<br><br>
We help you hire skilled workers across Europe.<br><br>
👉 What type of workers do you need?
</div>
""", unsafe_allow_html=True)

elif st.session_state.role == "candidate":

    st.success("Selected: Candidate")

    st.markdown("""
<div class="chat-box">
👋 Welcome!<br><br>
We help candidates get jobs in Europe.<br><br>
👉 What job are you looking for?
</div>
""", unsafe_allow_html=True)

# ---------- INPUT ----------
user_input = st.text_input("Type your answer...")

# ---------- CHAT LOGIC ----------
if user_input:

    user_input = user_input.lower()

    # ================== CANDIDATE ==================
    if st.session_state.role == "candidate":

        if "job" in user_input or "work" in user_input:
            st.markdown("""
<div class="chat-box">
🌍 <b>Available Jobs:</b><br><br>

• Hospitality<br>
• Nursing / Caregiver<br>
• Construction<br>
• Factory / Warehouse<br>
• Housekeeping<br>
• Farm Worker<br>
• Driver Jobs<br>
• Retail Staff<br>
• Security Guard<br><br>

💰 Salary:<br>
Unskilled: €700 – €900<br>
Skilled: €1000 – €1200<br><br>

👉 Which job are you interested in?
</div>
""", unsafe_allow_html=True)

        elif "visa" in user_input:
            st.markdown("""
<div class="chat-box">
📄 <b>Visa Process:</b><br><br>

Croatia: 60–90 days<br>
Serbia: 45–60 days<br>
Bulgaria: 60–90 days<br>
North Macedonia: 30–45 days<br><br>

📑 Documents:<br>
CV, Passport, Education, Experience,<br>
PCC (if required), Medical (optional)
</div>
""", unsafe_allow_html=True)

        else:
            st.markdown("""
<div class="chat-box">
🚀 Our team will guide you step-by-step.<br>
Please contact us to proceed further.
</div>
""", unsafe_allow_html=True)

    # ================== EMPLOYER ==================
    elif st.session_state.role == "employer":

        if "worker" in user_input or "hire" in user_input:
            st.markdown("""
<div class="chat-box">
🏢 <b>Industries we serve:</b><br><br>

• Hospitality<br>
• Nursing<br>
• Construction<br>
• Factory / Warehouse<br>
• Housekeeping<br>
• Drivers<br>
• Retail<br>
• Security<br><br>

👉 How many workers do you need?
</div>
""", unsafe_allow_html=True)

        elif user_input.isdigit():
            st.markdown(f"""
<div class="chat-box">
👍 Great! You need <b>{user_input}</b> workers.<br><br>
We will assist you with hiring & documentation.
</div>
""", unsafe_allow_html=True)

        else:
            st.markdown("""
<div class="chat-box">
📩 Please share your requirement (industry + number).
</div>
""", unsafe_allow_html=True)

# ---------- RESET ----------
if st.session_state.role:
    if st.button("🔄 Start Over"):
        st.session_state.role = None
        st.rerun()

# ---------- FOOTER ----------
st.markdown("<br>", unsafe_allow_html=True)
st.caption("⚡ SIS AI • Powered by SIS International Recruiters")
