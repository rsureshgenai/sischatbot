import streamlit as st
import time

st.set_page_config(page_title="SIS AI Assistant", layout="centered")

# ======================
# CUSTOM CSS (PREMIUM UI)
# ======================
st.markdown("""
<style>

/* Typing animation */
.typing {
  font-style: italic;
  opacity: 0.7;
  animation: blink 1s infinite;
}

@keyframes blink {
  0% {opacity: 0.3;}
  50% {opacity: 1;}
  100% {opacity: 0.3;}
}

/* Buttons */
.stLinkButton > a {
    display: block;
    width: 100%;
    padding: 16px;
    border-radius: 14px;
    font-weight: 600;
    text-align: center;
    text-decoration: none;
}

/* Call */
.call-btn a {
    background: linear-gradient(45deg, #4f46e5, #6a5cff);
    color: white !important;
}

/* WhatsApp */
.whatsapp-btn a {
    background: linear-gradient(45deg, #25D366, #128C7E);
    color: white !important;
}

/* Hover */
.stLinkButton > a:hover {
    transform: translateY(-2px);
}

</style>
""", unsafe_allow_html=True)

# ======================
# SESSION
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

    if col1.button("🏢 Hire Workers"):
        st.session_state.role = "employer"
        st.session_state.step = 1
        st.rerun()

    if col2.button("🧑 Get Job"):
        st.session_state.role = "candidate"
        st.session_state.step = 1
        st.rerun()

# ======================
# EMPLOYER FLOW
# ======================
elif st.session_state.role == "employer":

    st.success("Selected: Employer")

    # STEP 1
    if st.session_state.step == 1:
        st.markdown("👋 Welcome Employer!")
        st.markdown("What type of workers do you need?")

        job = st.text_input("Your answer", key="emp_job")

        if job:
            st.session_state.job = job
            st.session_state.step = 2
            st.rerun()

    # STEP 2
    elif st.session_state.step == 2:
        st.markdown(f"👍 You need **{st.session_state.job.title()} workers**")

        count = st.text_input("How many workers?", key="emp_count")

        if count.isdigit():
            st.session_state.count = count
            st.session_state.step = 3
            st.rerun()

    # STEP 3 (WITH TYPING EFFECT)
    elif st.session_state.step == 3:

        placeholder = st.empty()
        placeholder.markdown('<div class="typing">🤖 AI is typing...</div>', unsafe_allow_html=True)

        time.sleep(1.2)

        placeholder.empty()

        st.markdown(f"""
        ✅ Perfect!

        👷 Job Role: {st.session_state.job.title()}  
        🔢 Workers Needed: {st.session_state.count}  

        📍 Available Countries:
        Croatia, Serbia, Bulgaria  
        """)

        st.markdown("### 🚀 Contact Our Team")

        st.markdown('<div class="call-btn">', unsafe_allow_html=True)
        st.link_button("📞 Call Now", "tel:+385993665624")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="whatsapp-btn">', unsafe_allow_html=True)
        st.link_button(
            "💬 WhatsApp",
            f"https://wa.me/385993665624?text=Hi%20I%20need%20{st.session_state.count}%20{st.session_state.job}%20workers"
        )
        st.markdown('</div>', unsafe_allow_html=True)

# ======================
# CANDIDATE FLOW
# ======================
elif st.session_state.role == "candidate":

    st.success("Selected: Candidate")

    # STEP 1
    if st.session_state.step == 1:
        st.markdown("👋 Welcome Candidate!")
        st.markdown("What job are you looking for?")

        job = st.text_input("Your answer", key="can_job")

        if job:
            st.session_state.job = job
            st.session_state.step = 2
            st.rerun()

    # STEP 2 (WITH TYPING EFFECT)
    elif st.session_state.step == 2:

        placeholder = st.empty()
        placeholder.markdown('<div class="typing">🤖 AI is typing...</div>', unsafe_allow_html=True)

        time.sleep(1.2)

        placeholder.empty()

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
        • PCC (depends on country)  
        • Medical Certificate (optional)  

        ⏳ Visa Processing:
        30–90 days  
        """)

        st.markdown("### 🚀 Apply Now")

        st.markdown('<div class="call-btn">', unsafe_allow_html=True)
        st.link_button("📞 Call Now", "tel:+919994562962")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="whatsapp-btn">', unsafe_allow_html=True)
        st.link_button(
            "💬 WhatsApp Apply",
            f"https://wa.me/919994562962?text=Hi%20I%20am%20interested%20in%20{st.session_state.job}%20job"
        )
        st.markdown('</div>', unsafe_allow_html=True)

# ======================
# RESET
# ======================
st.markdown("---")

if st.button("🔄 Start Again"):
    st.session_state.role = None
    st.session_state.step = 0
    st.session_state.job = ""
    st.session_state.count = ""
    st.rerun()
