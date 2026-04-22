import streamlit as st

# PAGE CONFIG
st.set_page_config(page_title="SIS AI Assistant", layout="centered")

# ---------- CSS FIX (CENTER + RESPONSIVE) ----------
st.markdown("""
<style>

/* Remove extra top space */
.block-container {
    padding-top: 1.5rem !important;
    max-width: 700px;
    margin: auto;
}

/* Center content */
.main {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 90vh;
}

/* Buttons */
.stButton button {
    border-radius: 12px;
    padding: 10px 18px;
    font-weight: 500;
}

/* Chat bubble */
.chat-box {
    background-color: #F2DDE3;
    padding: 16px;
    border-radius: 14px;
    margin-top: 15px;
    color: black;
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

# SHOW SELECTED
if st.session_state.role:
    st.success(f"Selected: {st.session_state.role.capitalize()}")

# ---------- INPUT ----------
user_input = st.text_input("Type your answer...")

# ---------- RESPONSE LOGIC ----------
if user_input:

    user_input = user_input.lower()

    # ---------------- CANDIDATE FLOW ----------------
    if st.session_state.role == "candidate":

        if "job" in user_input:
            st.markdown("""
<div class="chat-box">
<b>Awesome 🌍</b><br><br>

<b>Top jobs:</b><br>
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

👉 Which job are you looking for?
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

👉 Required Documents:<br>
• CV<br>
• Passport<br>
• Education Certificate<br>
• Experience Certificate<br>
• PCC (if required)<br>
• Medical (optional)
</div>
""", unsafe_allow_html=True)

        else:
            st.markdown("""
<div class="chat-box">
🚀 <b>Next Step:</b><br><br>
Please contact our team to start your application process.
</div>
""", unsafe_allow_html=True)

    # ---------------- EMPLOYER FLOW ----------------
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

📍 Countries:<br>
Croatia, Serbia, Bulgaria<br><br>

👉 How many workers do you need?
</div>
""", unsafe_allow_html=True)

        elif user_input.isdigit():
            st.markdown(f"""
<div class="chat-box">
👍 Great! You need <b>{user_input}</b> workers.<br><br>
Our team will assist you with hiring and documentation process.
</div>
""", unsafe_allow_html=True)

        else:
            st.markdown("""
<div class="chat-box">
📩 Please share your requirement (industry, number of workers).
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("⚡ SIS AI • Powered by SIS International Recruiters")
