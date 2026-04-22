import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="SIS AI Assistant", layout="centered")

# ---------- CSS (FINAL CLEAN UI) ----------
st.markdown("""
<style>

/* Center container */
.block-container {
    max-width: 700px;
    margin: auto;
    padding-top: 4rem !important;
    padding-bottom: 4rem !important;
}

/* Center everything nicely */
[data-testid="stAppViewContainer"] {
    display: flex;
    justify-content: center;
}

[data-testid="stAppViewContainer"] > .main {
    width: 100%;
    max-width: 700px;
}

/* Title center */
h2 {
    text-align: center;
}

/* Buttons center */
.stButton {
    display: flex;
    justify-content: center;
}

/* Input styling */
.stTextInput input {
    border-radius: 12px;
    padding: 10px;
}

/* Chat bubble */
.chat-box {
    background-color: #F2DDE3;
    padding: 16px;
    border-radius: 14px;
    margin-top: 15px;
    color: black;
    line-height: 1.6;
}

/* Footer */
footer {
    text-align: center;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .block-container {
        padding-top: 2rem !important;
        padding-left: 1rem;
        padding-right: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("## 🌍 SIS AI Assistant")
st.caption("Hiring & Jobs in Europe")
st.markdown("---")

# ---------- SESSION ----------
if "role" not in st.session_state:
    st.session_state.role = None

# ---------- ROLE SELECTION ----------
col1, col2 = st.columns(2)

with col1:
    if st.button("🏢 Hire Workers"):
        st.session_state.role = "employer"

with col2:
    if st.button("👨‍💼 Get Job"):
        st.session_state.role = "candidate"

# ---------- SHOW ROLE ----------
if st.session_state.role:
    st.success(f"Selected: {st.session_state.role.capitalize()}")

# ---------- INPUT ----------
user_input = st.text_input("Type your answer...")

# ---------- CHAT LOGIC ----------
if user_input:

    user_input = user_input.lower()

    # ================== CANDIDATE ==================
    if st.session_state.role == "candidate":

        if "job" in user_input:
            st.markdown("""
<div class="chat-box">
<b>Awesome 🌍</b><br><br>

<b>Available Jobs:</b><br>
• Hospitality<br>
• Nursing / Caregiver<br>
• Construction<br>
• Factory / Warehouse<br>
• Housekeeping<br>
• Farm Worker<br>
• Driver Jobs<br>
• Retail Staff<br>
• Security Guard<br><br>

📍 <b>Countries:</b><br>
Croatia, Serbia, Bulgaria, North Macedonia & more<br><br>

💰 <b>Salary:</b><br>
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

📑 <b>Documents Required:</b><br>
• CV<br>
• Passport<br>
• Education Certificate<br>
• Experience Certificate<br>
• PCC (depends on country)<br>
• Medical (optional)
</div>
""", unsafe_allow_html=True)

        else:
            st.markdown("""
<div class="chat-box">
🚀 <b>Next Step:</b><br><br>
Our team will guide you through the complete process.<br>
Please connect with us to start your application.
</div>
""", unsafe_allow_html=True)

    # ================== EMPLOYER ==================
    elif st.session_state.role == "employer":

        if "worker" in user_input or "hire" in user_input:
            st.markdown("""
<div class="chat-box">
🏢 <b>We provide manpower for:</b><br><br>

• Hospitality<br>
• Nursing<br>
• Construction<br>
• Factory / Warehouse<br>
• Housekeeping<br>
• Farm Workers<br>
• Drivers<br>
• Retail<br>
• Security<br><br>

📍 <b>Countries:</b><br>
Croatia, Serbia, Bulgaria<br><br>

👉 How many workers do you need?
</div>
""", unsafe_allow_html=True)

        elif user_input.isdigit():
            st.markdown(f"""
<div class="chat-box">
👍 <b>Great!</b><br><br>

You need <b>{user_input}</b> workers.<br>
Our team will assist you with hiring, documentation & deployment.
</div>
""", unsafe_allow_html=True)

        else:
            st.markdown("""
<div class="chat-box">
📩 Please share your requirement:<br>
Industry + Number of workers needed
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("⚡ SIS AI • Powered by SIS International Recruiters")
