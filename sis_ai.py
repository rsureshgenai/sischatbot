import streamlit as st
import time

st.set_page_config(page_title="SIS AI Assistant", layout="centered")

# ---------------- HIDE STREAMLIT UI ----------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION INIT ----------------
if "role" not in st.session_state:
    st.session_state.role = None
if "step" not in st.session_state:
    st.session_state.step = 0
if "job" not in st.session_state:
    st.session_state.job = ""
if "count" not in st.session_state:
    st.session_state.count = ""

# ---------------- RESET ----------------
def reset():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# ---------------- HEADER ----------------
st.markdown("## 🌍 SIS AI Assistant")
st.caption("Hiring & Jobs in Europe")

# ---------------- ROLE SELECT ----------------
if st.session_state.role is None:
    col1, col2 = st.columns(2)

    if col1.button("🏢 Hire Workers"):
        st.session_state.role = "employer"
        st.session_state.step = 1

    if col2.button("👷 Get Job"):
        st.session_state.role = "candidate"
        st.session_state.step = 1

# ---------------- SHOW SELECTED ----------------
if st.session_state.role:
    st.success(f"Selected: {st.session_state.role.capitalize()}")

# =====================================================
# ================= EMPLOYER FLOW ======================
# =====================================================
if st.session_state.role == "employer":

    if st.session_state.step == 1:

        def set_job():
            if st.session_state.job_input.strip():
                st.session_state.job = st.session_state.job_input
                st.session_state.step = 2

        st.markdown("👋 Welcome Employer!")
        st.text_input("What workers do you need?", key="job_input", on_change=set_job)
        st.caption("Example: Carpenter, Mason, Driver, Factory Worker")

    elif st.session_state.step == 2:

        def set_count():
            if st.session_state.count_input.isdigit():
                st.session_state.count = st.session_state.count_input
                st.session_state.step = 3
            else:
                st.warning("⚠️ Enter valid number")

        st.markdown(f"👷 Job Role: **{st.session_state.job}**")
        st.text_input("How many workers?", key="count_input", on_change=set_count)

    elif st.session_state.step == 3:

        with st.spinner("🤖 Processing..."):
            time.sleep(1)

        st.markdown(f"""
### ✅ Requirement Summary

👷 Job Role: **{st.session_state.job}**  
🔢 Workers Needed: **{st.session_state.count}**  

📍 Countries: Croatia, Serbia, Bulgaria  
        """)

        st.markdown("### 🚀 Contact Our Team")

        st.markdown(f"""
<a href="tel:+385993665624" style="
display:block;width:100%;padding:16px;margin-bottom:12px;
background:linear-gradient(135deg,#4f46e5,#7c3aed);
color:white;text-align:center;border-radius:12px;
text-decoration:none;font-weight:600;">
📞 Call Now
</a>

<a href="https://wa.me/385993665624?text=Need {st.session_state.count} {st.session_state.job} workers" style="
display:block;width:100%;padding:16px;
background:linear-gradient(135deg,#25D366,#128C7E);
color:white;text-align:center;border-radius:12px;
text-decoration:none;font-weight:600;">
💬 WhatsApp Chat
</a>
""", unsafe_allow_html=True)

        if st.button("🔄 Start Again"):
            reset()
            st.rerun()

# =====================================================
# ================= CANDIDATE FLOW =====================
# =====================================================
if st.session_state.role == "candidate":

    COMMON_JOBS = [
        "welder", "carpenter", "plumber", "electrician", "mason",
        "driver", "cleaner", "factory worker", "farm worker",
        "helper", "warehouse worker", "kitchen helper",
        "security guard", "nurse", "caregiver"
    ]

    def suggest_job(user_input):
        for job in COMMON_JOBS:
            if user_input in job or job in user_input:
                return job
        return None

    if st.session_state.step == 1:

        def set_job():
            if st.session_state.job_input.strip():
                st.session_state.job = st.session_state.job_input
                st.session_state.step = 2

        st.markdown("👍 What job are you looking for?")
        st.text_input("Enter job", key="job_input", on_change=set_job)
        st.caption("Try: Welder, Driver, Factory Worker, Farm Worker")

    elif st.session_state.step == 2:

        with st.spinner("🤖 AI is typing..."):
            time.sleep(1)

        job_input = st.session_state.job.lower().strip()
        suggested = suggest_job(job_input)

        if not suggested:
            st.warning("⚠️ Not sure about that job")
            st.info("👉 Try: Welder, Mason, Driver, Factory Worker")

        industry_map = {
            "welder": "construction",
            "carpenter": "construction",
            "plumber": "construction",
            "electrician": "construction",
            "mason": "construction",
            "factory worker": "manufacturing",
            "farm worker": "agriculture",
            "driver": "logistics",
            "cleaner": "hospitality",
            "nurse": "healthcare",
            "helper": "general"
        }

        industry = "general"
        for key in industry_map:
            if key in job_input:
                industry = industry_map[key]

        salary_map = {
            "construction": "€900 – €1200",
            "manufacturing": "€800 – €1100",
            "agriculture": "€700 – €900",
            "logistics": "€800 – €1100",
            "hospitality": "€700 – €900",
            "healthcare": "€1000 – €1500",
            "general": "€700 – €1200"
        }

        salary = salary_map.get(industry)

        st.markdown(f"""
### 👍 {st.session_state.job.capitalize()} Jobs Available

🏭 Industry: **{industry.capitalize()}**

📍 Countries:
Croatia, Serbia, Bulgaria, North Macedonia  

💰 Salary:
{salary}

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

        st.markdown("### 🚀 Apply Now")

        st.markdown(f"""
<a href="tel:+919384747101" style="
display:block;width:100%;padding:16px;margin-bottom:12px;
background:linear-gradient(135deg,#4f46e5,#7c3aed);
color:white;text-align:center;border-radius:12px;
text-decoration:none;font-weight:600;">
📞 Call Now
</a>

<a href="https://wa.me/919384747101?text=Hello%20SIS%20Team,%20I%20am%20interested%20in%20{st.session_state.job}%20job" style="
display:block;width:100%;padding:16px;
background:linear-gradient(135deg,#25D366,#128C7E);
color:white;text-align:center;border-radius:12px;
text-decoration:none;font-weight:600;">
💬 WhatsApp Apply
</a>
""", unsafe_allow_html=True)

        if st.button("🔄 Start Again"):
            reset()
            st.rerun()
