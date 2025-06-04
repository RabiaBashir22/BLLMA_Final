import gradio as gr
from study_planner_tool import StudyPlanGenerator
from calendar_agenda_tool import CalendarAgendaTool
from task_manager_tool import TaskManagerTool
from goal_tracker_tool import GoalSettingTrackingTool
from flashcard_tool import FlashcardQuizMakerTool
from revision_tool import RevisionPlannerTool

# Instantiate all tools
study_plan_tool = StudyPlanGenerator()
calendar_tool = CalendarAgendaTool()
task_manager_tool = TaskManagerTool()
goal_tracker_tool = GoalSettingTrackingTool()
flashcard_tool = FlashcardQuizMakerTool()
revision_tool = RevisionPlannerTool()

# Create Gradio interfaces for each tool
def generate_study_plan(subject, exam_date, hours_per_day, key_topics):
    return study_plan_tool.generate_plan(subject, exam_date, hours_per_day, key_topics)

def generate_calendar_agenda(study_plan):
    return calendar_tool.create_agenda(study_plan)

def manage_tasks(task_description):
    return task_manager_tool.manage(task_description)

def set_and_track_goals(goal):
    return goal_tracker_tool.track(goal)

def create_flashcards(topic):
    return flashcard_tool.create(topic)

def plan_revision(subject, exam_date):
    return revision_tool.plan(subject, exam_date)

with gr.Blocks() as demo:
    with gr.Tab("📘 Study Plan"):
        subject = gr.Textbox(label="Subject")
        exam_date = gr.Textbox(label="Exam Date (YYYY-MM-DD)")
        hours_per_day = gr.Slider(1, 10, label="Study Hours per Day")
        key_topics = gr.Textbox(label="Key Topics (comma-separated)")
        output = gr.Textbox(label="Study Plan Output")
        btn = gr.Button("Generate Study Plan")
        btn.click(generate_study_plan, inputs=[subject, exam_date, hours_per_day, key_topics], outputs=output)

    with gr.Tab("📆 Calendar Agenda"):
        study_plan_input = gr.Textbox(label="Paste Study Plan")
        calendar_output = gr.Textbox(label="Calendar Agenda Output")
        gr.Button("Create Agenda").click(generate_calendar_agenda, inputs=study_plan_input, outputs=calendar_output)

    with gr.Tab("✅ Task Manager"):
        task_input = gr.Textbox(label="Task Description")
        task_output = gr.Textbox(label="Task Output")
        gr.Button("Manage Task").click(manage_tasks, inputs=task_input, outputs=task_output)

    with gr.Tab("🎯 Goal Tracking"):
        goal_input = gr.Textbox(label="Goal Description")
        goal_output = gr.Textbox(label="Goal Tracker Output")
        gr.Button("Track Goal").click(set_and_track_goals, inputs=goal_input, outputs=goal_output)

    with gr.Tab("🧠 Flashcards & Quiz"):
        topic_input = gr.Textbox(label="Topic for Flashcards")
        flashcard_output = gr.Textbox(label="Flashcards Output")
        gr.Button("Generate Flashcards").click(create_flashcards, inputs=topic_input, outputs=flashcard_output)

    with gr.Tab("🔁 Revision Planner"):
        rev_subject = gr.Textbox(label="Subject")
        rev_date = gr.Textbox(label="Exam Date (YYYY-MM-DD)")
        rev_output = gr.Textbox(label="Revision Plan Output")
        gr.Button("Plan Revision").click(plan_revision, inputs=[rev_subject, rev_date], outputs=rev_output)

if __name__ == "__main__":
    demo.launch()
