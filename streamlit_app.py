#streamlit run roadmap_streamlit.py  == run 
import streamlit as st

# ============================================
# 🌟 DATA ANALYST ROADMAP - STREAMLIT APP 🌟
# ============================================

# ---------- ROADMAP DATA ----------
ROADMAP = {
    1: {
        1: "Python basics (variables, loops)",
        2: "Lists, dictionaries",
        3: "Functions + file handling",
        4: "NumPy arrays & operations",
        5: "NumPy aggregations",
        6: "Practice + mini CSV task",
        7: "Revision + interview questions"
    },
    2: {
        1: "Pandas DataFrames",
        2: "Data cleaning (nulls, duplicates)",
        3: "Filtering, sorting",
        4: "groupby(), aggregations",
        5: "merge(), concat()",
        6: "Matplotlib & Seaborn",
        7: "Mini project (CSV -> insights)"
    },
    3: {
        1: "SELECT, WHERE, ORDER BY",
        2: "GROUP BY, HAVING",
        3: "Aggregate functions",
        4: "INNER & LEFT JOIN",
        5: "RIGHT & FULL JOIN",
        6: "Practice queries",
        7: "SQL interview questions"
    },
    4: {
        1: "Subqueries",
        2: "CTE (WITH clause)",
        3: "Window functions (ROW_NUMBER)",
        4: "RANK, DENSE_RANK",
        5: "Date functions",
        6: "SQL case study",
        7: "Full SQL revision"
    },
    5: {
        1: "Power BI interface",
        2: "Data import + Power Query",
        3: "Data modeling",
        4: "Charts & visuals",
        5: "Filters & slicers",
        6: "KPI cards",
        7: "Mini dashboard"
    },
    6: {
        1: "DAX basics",
        2: "CALCULATE(), FILTER()",
        3: "Time intelligence",
        4: "Sales dashboard",
        5: "Customer dashboard",
        6: "Dashboard polishing",
        7: "Publish + LinkedIn post"
    },
    7: {
        1: "Sales Performance Analysis",
        2: "Sales project continuation",
        3: "Customer Churn Analysis",
        4: "Churn insights & visuals",
        5: "HR Analytics Dashboard",
        6: "Dashboard polishing",
        7: "GitHub upload & documentation"
    },
    8: {
        1: "ATS resume building",
        2: "SQL interview practice",
        3: "Mock technical interview",
        4: "Mock HR interview",
        5: "Apply 10–15 jobs",
        6: "LinkedIn optimization",
        7: "Final revision"
    }
}

TOTAL_TASKS = 56
PROGRESS_FILE = "progress.txt"

# ---------- PROGRESS HANDLING ----------
def load_progress():
    progress = set()
    try:
        with open(PROGRESS_FILE, "r") as f:
            for line in f:
                week, day = line.strip().split(",")
                progress.add((int(week), int(day)))
    except:
        pass
    return progress


def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        for week, day in sorted(progress):
            f.write(f"{week},{day}\n")


# ---------- APP STATE ----------
if "progress" not in st.session_state:
    st.session_state.progress = load_progress()

# ---------- UI ----------
st.set_page_config(page_title="Data Analyst Roadmap", page_icon="🚀")
st.title("🌟 Data Analyst Roadmap Tracker")
st.caption("Stay consistent. Job-ready in 2–3 months 🚀")

st.divider()

# ---------- SELECTION ----------
col1, col2 = st.columns(2)

with col1:
    week = st.selectbox("📅 Select Week", list(ROADMAP.keys()))

with col2:
    day = st.selectbox("📘 Select Day", list(ROADMAP[week].keys()))

topic = ROADMAP[week][day]
is_done = (week, day) in st.session_state.progress

st.subheader("📌 Today's Topic")
st.info(topic)

status_text = "✅ DONE" if is_done else "⏳ NOT DONE"
st.write(f"**Status:** {status_text}")

# ---------- ACTION BUTTONS ----------
col3, col4, col5 = st.columns(3)

with col3:
    if st.button("✅ Mark as Done"):
        st.session_state.progress.add((week, day))
        save_progress(st.session_state.progress)
        st.success("Great job! Task marked as DONE 🎉")

with col4:
    if st.button("🗑️ Delete Task"):
        if (week, day) in st.session_state.progress:
            st.session_state.progress.remove((week, day))
            save_progress(st.session_state.progress)
            st.warning("Task removed. You can revisit it anytime.")
        else:
            st.info("Task was not marked as done.")

with col5:
    if st.button("🔄 Reset All Progress"):
        st.session_state.progress.clear()
        save_progress(st.session_state.progress)
        st.error("All progress reset. Fresh start! 💪")

st.divider()

# ---------- PROGRESS SUMMARY ----------
completed = len(st.session_state.progress)
percent = (completed / TOTAL_TASKS) * 100

st.subheader("📊 Progress Summary")
st.progress(percent / 100)
st.write(f"**Completed:** {completed} / {TOTAL_TASKS}")
st.write(f"**Progress:** {percent:.2f}%")

if percent >= 75:
    st.success("🔥 Amazing pace! You are almost job-ready!")
elif percent >= 40:
    st.info("💪 Strong momentum. Keep going!")
else:
    st.warning("🌱 Every step counts. Stay consistent!")

st.divider()

st.caption("Built with ❤️ using Python & Streamlit")
