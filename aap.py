import gradio as gr
from datetime import datetime

# Placeholder: import your actual tool classes
# from your_modules import (StudyPlanGenerator, CalendarAgendaTool, TaskManagerTool,
#                           GoalSettingTrackingTool, FlashcardQuizMakerTool, RevisionPlannerTool)

# Mock implementations for this example
def generate_study_plan(subject, exam_date, hours_per_day, topics, review_frequency):
    return f"""### 📘 7-Day Study Plan for {subject}
**Exam Date:** {exam_date}
**Daily Study Time:** {hours_per_day} hrs/day
**Key Topics:** {topics}
**Review Every:** {review_frequency} days

Day 1: Introduction to {topics.split(',')[0].strip()}
...

Day 7: Final Review + Flashcards + Mock Test"""

def generate_calendar_agenda():
    return "### 📆 Calendar Agenda\nStudy sessions mapped to your calendar."

def generate_tasks(topics):
    return f"### ✅ Tasks\nBreakdown of tasks for topics: {topics}\n- Create notes\n- Solve 10 practice problems each\n- Summarize in flashcards"

def track_goals():
    return "### 🎯 Goal Tracking\nTrack progress of weekly and daily learning objectives."

def generate_flashcards(topics):
    return f"### 🧠 Flashcards\nGenerated flashcards for: {topics}\n- Q1: What is...?\n- Q2: Explain..."

def plan_revisions(exam_date):
    return f"### 🔁 Revision Plan\nRevision scheduled on: {exam_date} - 3, {exam_date} - 1"

# Gradio UI
def full_study_plan(subject, exam_date_str, hours_per_day, topics, review_frequency):
    try:
        exam_date = datetime.strptime(exam_date_str, "%Y-%m-%d")
    except ValueError:
        return "❌ Invalid date format. Please use YYYY-MM-DD."

    return generate_study_plan(subject, exam_date_str, hours_per_day, topics, review_frequency)

def full_tasks(topics):
    return generate_tasks(topics)

def full_flashcards(topics):
    return generate_flashcards(topics)

def full_revisions(exam_date_str):
    return plan_revisions(exam_date_str)

def full_agenda():
    return generate_calendar_agenda()

def full_goals():
    return track_goals()

with gr.Blocks(title="AI Study Planner") as demo:
    gr.Markdown("# 🎓 AI-Powered Study Planner\nEnter your exam details and get personalized study resources.")

    with gr.Tabs():
        with gr.TabItem("📘 Study Plan"):
            with gr.Row():
                subject = gr.Textbox(label="Subject", placeholder="e.g., Chemistry")
                exam_date = gr.Textbox(label="Exam Date (YYYY-MM-DD)", placeholder="2025-07-10")
            with gr.Row():
                hours_per_day = gr.Slider(1, 10, value=5, label="Study Hours per Day")
                topics = gr.Textbox(label="Key Topics (comma-separated)", placeholder="Organic Chemistry, Acids & Bases, Stoichiometry")
            review_frequency = gr.Slider(1, 3, value=2, label="Review Session Frequency (in days)")
            plan_output = gr.Markdown("### Output will appear here...")
            generate_btn = gr.Button("Generate Study Plan")
            generate_btn.click(fn=full_study_plan, inputs=[subject, exam_date, hours_per_day, topics, review_frequency], outputs=[plan_output])

        with gr.TabItem("📆 Calendar Agenda"):
            agenda_output = gr.Markdown("### Calendar will appear here...")
            agenda_btn = gr.Button("Generate Calendar Agenda")
            agenda_btn.click(fn=full_agenda, inputs=[], outputs=[agenda_output])

        with gr.TabItem("✅ Task Manager"):
            task_input = gr.Textbox(label="Topics for Tasks", placeholder="Enter topics")
            task_output = gr.Markdown("### Task breakdown will appear here...")
            task_btn = gr.Button("Generate Tasks")
            task_btn.click(fn=full_tasks, inputs=[task_input], outputs=[task_output])

        with gr.TabItem("🎯 Goal Tracking"):
            goal_output = gr.Markdown("### Goal tracking details will appear here...")
            goal_btn = gr.Button("Show Goal Tracker")
            goal_btn.click(fn=full_goals, inputs=[], outputs=[goal_output])

        with gr.TabItem("🧠 Flashcards & Quiz"):
            flashcard_input = gr.Textbox(label="Topics for Flashcards", placeholder="Enter topics")
            flashcard_output = gr.Markdown("### Flashcards will appear here...")
            flashcard_btn = gr.Button("Generate Flashcards")
            flashcard_btn.click(fn=full_flashcards, inputs=[flashcard_input], outputs=[flashcard_output])

        with gr.TabItem("🔁 Revision Planner"):
            revision_input = gr.Textbox(label="Exam Date (YYYY-MM-DD)", placeholder="2025-07-10")
            revision_output = gr.Markdown("### Revision plan will appear here...")
            revision_btn = gr.Button("Generate Revision Plan")
            revision_btn.click(fn=full_revisions, inputs=[revision_input], outputs=[revision_output])

if __name__ == "__main__":
    demo.launch()
