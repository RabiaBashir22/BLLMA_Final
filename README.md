# 📚 StudyPlanner - AI-Powered Personalized Study Planning

StudyPlanner is an AI-based Gradio web application designed to help students prepare effectively for exams by generating customized study plans, managing tasks, creating flashcards, and more. Powered by intelligent agents and tools, the app provides an all-in-one study companion.

---

## 🚀 Features

* **📘 Study Plan Generator**: Create detailed, 7-day study plans based on subject, topics, exam date, and study preferences.
* **📆 Calendar Agenda Tool**: Align study sessions with your personal calendar.
* **✅ Task Manager Tool**: Break down study goals into manageable tasks.
* **🎯 Goal Setting & Tracking Tool**: Set academic goals and track progress.
* **🧠 Flashcard & Quiz Maker Tool**: Generate flashcards and quizzes from key topics.
* **🔁 Revision Planner Tool**: Plan optimal review sessions leading up to the exam.

---

## 🛠️ Technologies Used

* **Python**
* **Gradio** – UI framework for quick interface creation
* **DateTime** – For parsing and scheduling dates
* **Custom Tool Classes** – Modular tools for each planner functionality

---

## 📂 Project Structure

```
studyplanner/
├── app.py                    # Gradio interface with integrated tabs
├── tool_base_classes.py      # Base classes for tools (Tool, LLMTool)
├── study_planner_tool.py     # StudyPlanGenerator implementation
├── calendar_agenda_tool.py   # CalendarAgendaTool logic
├── task_manager_tool.py      # TaskManagerTool logic
├── goal_tracker_tool.py      # GoalSettingTrackingTool logic
├── flashcard_tool.py         # FlashcardQuizMakerTool logic
├── revision_tool.py          # RevisionPlannerTool logic
├── orchestrator_agent.py     # Orchestrator class managing tool calls
└── README.md                 # Project documentation
```

---



## 📌 Example Use Case

* **Input**:

  * Subject: Chemistry
  * Exam Date: 2025-07-10
  * Topics: Organic Chemistry, Acids & Bases, Stoichiometry
  * Study Time: 5-6 hrs/day

* **Output**:

  * A markdown-formatted daily study plan
  * Flashcards and quizzes
  * Scheduled revision sessions

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo, make your changes, and submit a pull request.

---

## 📄 License

MIT License. See `LICENSE` file for details.

---

## 💡 Future Enhancements

* Add calendar sync with Google Calendar
* Export study plans to PDF
* Add user authentication and save progress

---


