import streamlit as st

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

# ---------------- RESET ----------------
def reset():
    st.session_state.role = None
    st.session_state.step = 0
    st.session_state.job = ""
    st.session_state.count = ""

# ---------------- COMMON JOBS ----------------
COMMON_JOBS = [
    "welder", "carpenter", "plumber", "electrician",
    "driver", "cleaner", "factory worker", "farm worker",
    "helper", "warehouse worker", "kitchen helper",
    "security guard", "nurse", "caregiver"
]

def suggest_job(user_input):
    user_input = user_input.lower()
    for job in COMMON_JOBS:
        if user_input in job or job in user_input:
            return job
    return None

# ---------------- STYLE ----------------
st.markdown("""
<style>
body {background:#0b0f1a; color:white;}
.badge {
    background:#16a34a;
    padding:10px;
    border-radius:10px;
    margin-bottom:10px;
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

# ---------------- ROLE SELECT ----------------
if st.session_state.role is None:
    col1, col2 = st.columns(2)

    if col1.button("🏢 Hire Workers"):
        st.session_state.role = "employer"
        st.session_state.step = 1

    if col2.button("👷 Get Job"):
        st.session_state.role = "candidate"
        st.session_state.step = 1

# ---------------- AFTER SELECT ----------------
if st.session_state.role:
    st.markdown(f"""
    <div class="badge">
    Selected: {st.session_state.role.capitalize()}
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# ================= EMPLOYER FLOW ==========================
# =========================================================
if st.session_state.role == "employer":

    if st.session_state.step == 1:
        st.markdown("👋 Welcome Employer!")
        job = st.text_input("What workers do you need?")

        if job:
            st.session_state.job = job
            st.session_state.step = 2

    elif st.session_state.step == 2:
        count = st.text_input("How many workers?")

        if count:
            if count.isdigit():
                st.session_state.count = count
                st.session_state.step = 3
            else:
                st.warning("⚠️ Enter valid number (Example: 5, 10)")

    elif st.session_state.step == 3:
        st.markdown(f"""
👷 Job Role: {st.session_state.job}  
🔢 Workers Needed: {st.session_state.count}  

📍 Countries: Croatia, Serbia, Bulgaria  
        """)

        st.markdown("### 🚀 Contact Our Team")

        st.markdown(f"""
<a href="tel:+385993665624" style="
display:block;width:100%;padding:15px;margin-bottom:10px;
background:linear-gradient(45deg,#4f46e5,#6a5cff);
color:white;text-align:center;border-radius:10px;text-decoration:none;">
📞 Call Now
</a>

<a href="https://wa.me/385993665624?text=Need {st.session_state.count} {st.session_state.job} workers" style="
display:block;width:100%;padding:15px;
background:linear-gradient(45deg,#25D366,#128C7E);
color:white;text-align:center;border-radius:10px;text-decoration:none;">
💬 WhatsApp
</a>
""", unsafe_allow_html=True)

        if st.button("🔄 Start Again"):
            reset()

# =========================================================
# ================= CANDIDATE FLOW =========================
# =========================================================
if st.session_state.role == "candidate":

    if st.session_state.step == 1:
        st.markdown("👍 What job are you looking for?")
        job = st.text_input("Enter job")

        if job:
            st.session_state.job = job
            st.session_state.step = 2

    elif st.session_state.step == 2:

        job_input = st.session_state.job.lower().replace("-", " ").strip()

        suggested = suggest_job(job_input)

        if suggested:
            job_input = suggested
        else:
            st.warning("⚠️ Not sure about that job")

            st.info("""
👉 Try:
Welder | Driver | Factory Worker | Farm Worker | Cleaner
""")

        # INDUSTRY MAP
        industry_map = {
            "welder": "construction",
            "carpenter": "construction",
            "plumber": "construction",
            "electrician": "construction",
            "factory worker": "manufacturing",
            "farm worker": "agriculture",
            "driver": "logistics",
            "cleaner": "hospitality",
            "nurse": "healthcare",
            "helper": "general"
        }

        industry = "general"
        for key, value in industry_map.items():
            if key in job_input:
                industry = value
                break

        # SALARY
        salary_map = {
            "construction": "€900 – €1200",
            "manufacturing": "€800 – €1100",
            "agriculture": "€700 – €900",
            "logistics": "€800 – €1100",
            "hospitality": "€700 – €900",
            "healthcare": "€1000 – €1500",
            "general": "€700 – €1200"
        }

        salary = salary_map.get(industry, "€700 – €1200")

        st.markdown(f"""
👍 {job_input.capitalize()} jobs available!

🏭 Industry: {industry.capitalize()}

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
<a href="tel:+919994562962" style="
display:block;width:100%;padding:15px;margin-bottom:10px;
background:linear-gradient(45deg,#4f46e5,#6a5cff);
color:white;text-align:center;border-radius:10px;text-decoration:none;">
📞 Call Now
</a>

<a href="https://wa.me/919994562962?text=Interested in {job_input} job" style="
display:block;width:100%;padding:15px;
background:linear-gradient(45deg,#25D366,#128C7E);
color:white;text-align:center;border-radius:10px;text-decoration:none;">
💬 WhatsApp Apply
</a>
""", unsafe_allow_html=True)

        if st.button("🔄 Start Again"):
            reset()
