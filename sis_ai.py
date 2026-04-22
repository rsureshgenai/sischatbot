import streamlit as st
import time

st.set_page_config(page_title="SIS AI Assistant", layout="centered")

# ---------------- SESSION ----------------
if "role" not in st.session_state:
    st.session_state.role = None
if "step" not in st.session_state:
    st.session_state.step = 0
if "job" not in st.session_state:
    st.session_state.job = ""
if "count" not in st.session_state:
    st.session_state.count = ""

# ---------------- STYLE ----------------
st.markdown("""
<style>
body {background:#0b0f1a; color:white;}

.chat-box {
    background:#111827;
    padding:15px;
    border-radius:12px;
    margin-bottom:10px;
}

.bot {
    background:#1f2937;
}

.user {
    background:#374151;
    text-align:right;
}

.badge {
    background:#16a34a;
    padding:10px;
    border-radius:10px;
    margin-bottom:10px;
}

a {
    transition:0.3s;
}
a:hover {
    transform:scale(1.03);
    opacity:0.95;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("## 🌍 SIS AI Assistant")
st.caption("Hiring & Jobs in Europe")

# ---------------- RESET ----------------
def reset():
    st.session_state.role = None
    st.session_state.step = 0
    st.session_state.job = ""
    st.session_state.count = ""

# ---------------- ROLE SELECT ----------------
if st.session_state.role is None:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏢 Hire Workers"):
            st.session_state.role = "employer"
            st.session_state.step = 1

    with col2:
        if st.button("👷 Get Job"):
            st.session_state.role = "candidate"
            st.session_state.step = 1

# ---------------- AFTER SELECT ----------------
if st.session_state.role:

    st.markdown(f"""
    <div class="badge">
    Selected: {st.session_state.role.capitalize()}
    </div>
    """, unsafe_allow_html=True)

# ---------------- EMPLOYER FLOW ----------------
if st.session_state.role == "employer":

    if st.session_state.step == 1:
        st.markdown("👋 Welcome Employer!")
        st.markdown("What type of workers do you need?")

        job = st.text_input("Enter job role")

        if job:
            st.session_state.job = job
            st.session_state.step = 2

    elif st.session_state.step == 2:
        st.markdown(f"👷 Job Role: **{st.session_state.job}**")
        count = st.text_input("How many workers needed?")

        if count.isdigit():
            st.session_state.count = count
            st.session_state.step = 3

    elif st.session_state.step == 3:

        st.markdown("✅ Perfect!")

        st.markdown(f"""
👷 Job Role: {st.session_state.job}  
🔢 Workers Needed: {st.session_state.count}  

📍 Available Countries: Croatia, Serbia, Bulgaria  

🚀 Our team will contact you shortly.
        """)

        # PREMIUM BUTTONS
        st.markdown("### 🚀 Contact Our Team")

        st.markdown(f"""
<a href="tel:+385993665624" style="
display:block;
width:100%;
padding:15px;
margin-bottom:10px;
background:linear-gradient(45deg,#4f46e5,#6a5cff);
color:white;
text-align:center;
border-radius:10px;
text-decoration:none;
font-weight:bold;">
📞 Call Now
</a>

<a href="https://wa.me/385993665624?text=Need {st.session_state.count} {st.session_state.job} workers" style="
display:block;
width:100%;
padding:15px;
background:linear-gradient(45deg,#25D366,#128C7E);
color:white;
text-align:center;
border-radius:10px;
text-decoration:none;
font-weight:bold;">
💬 WhatsApp
</a>
""", unsafe_allow_html=True)

        if st.button("🔄 Start Again"):
            reset()

# ---------------- CANDIDATE FLOW ----------------
if st.session_state.role == "candidate":

    if st.session_state.step == 1:
        st.markdown("👍 What job are you looking for?")
        job = st.text_input("Enter job")

        if job:
            st.session_state.job = job
            st.session_state.step = 2

    elif st.session_state.step == 2:

        st.markdown(f"""
👍 {st.session_state.job} jobs available!

📍 Countries: Croatia, Serbia, Bulgaria, North Macedonia  

💰 Salary:
• Unskilled: €700 – €900  
• Skilled: €1000 – €1200  

📋 Required Documents:
• CV (with education details)  
• Passport  
• Education Certificate  
• Experience Certificate  
• Trade Certificate (added advantage)  
• PCC (depends on country)  
• Medical Certificate (optional)  

⏳ Visa Processing: 30–90 days  
        """)

        # PREMIUM BUTTONS
        st.markdown("### 🚀 Apply Now")

        st.markdown(f"""
<a href="tel:+919994562962" style="
display:block;
width:100%;
padding:15px;
margin-bottom:10px;
background:linear-gradient(45deg,#4f46e5,#6a5cff);
color:white;
text-align:center;
border-radius:10px;
text-decoration:none;
font-weight:bold;">
📞 Call Now
</a>

<a href="https://wa.me/919994562962?text=Interested in {st.session_state.job} job" style="
display:block;
width:100%;
padding:15px;
background:linear-gradient(45deg,#25D366,#128C7E);
color:white;
text-align:center;
border-radius:10px;
text-decoration:none;
font-weight:bold;">
💬 WhatsApp Apply
</a>
""", unsafe_allow_html=True)

        if st.button("🔄 Start Again"):
            reset()
