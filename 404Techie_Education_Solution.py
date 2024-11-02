import tkinter as tk
from tkinter import messagebox
import random

# Data for career paths and required skills
career_paths = {
    "data_scientist": ["python", "statistics", "machine learning", "data visualization"],
    "web_developer": ["HTML", "CSS", "JavaScript", "React"],
    "digital_marketer": ["SEO", "content writing", "analytics", "social media"],
}

# Course recommendations based on skills
course_catalog = {
    "python": "Learn Python Programming on Coursera",
    "statistics": "Statistics Fundamentals on Udemy",
    "machine learning": "Machine Learning with Python on edX",
    "data visualization": "Data Visualization with Python on Udemy",
    "HTML": "HTML Basics on Codecademy",
    "CSS": "CSS Essentials on Udemy",
    "JavaScript": "JavaScript for Beginners on Coursera",
    "React": "React Fundamentals on edX",
    "SEO": "SEO Training on LinkedIn Learning",
    "content writing": "Content Writing Essentials on Coursera",
    "analytics": "Google Analytics Certification",
    "social media": "Social Media Marketing on Udacity",
}

# Skill Gap Analysis
def identify_skill_gaps(current_skills, career_goal):
    required_skills = career_paths.get(career_goal, [])
    skill_gaps = [skill for skill in required_skills if skill not in current_skills]
    return skill_gaps

# Recommend Courses
def recommend_courses(skill_gaps):
    return [course_catalog[skill] for skill in skill_gaps if skill in course_catalog]

# Simulate Feedback
def simulate_assessment(skill_gaps):
    feedback = {skill: random.choice(["Needs Improvement", "Satisfactory", "Excellent"]) for skill in skill_gaps}
    return feedback

# Generate Learning Path and Display
def generate_learning_path():
    name = name_entry.get()
    career_goal = career_goal_var.get()
    current_skills = skills_entry.get().split(", ")

    # Identify skill gaps and recommend courses
    skill_gaps = identify_skill_gaps(current_skills, career_goal)
    if not skill_gaps:
        messagebox.showinfo("Results", f"{name} already has all the skills required for {career_goal}.")
        return

    recommended_courses = recommend_courses(skill_gaps)
    feedback = simulate_assessment(skill_gaps)

    # Display Recommendations and Feedback
    recommendations_text = f"\nRecommended Learning Path for {name}:\n" + "\n".join(f"- {course}" for course in recommended_courses)
    feedback_text = "\n\nProgress Feedback:\n" + "\n".join(f"{skill}: {progress}" for skill, progress in feedback.items())

    result_text.set(recommendations_text + feedback_text)

# Tkinter GUI Setup
root = tk.Tk()
root.title("AI-Powered Skill Development Platform")
root.geometry("500x500")

# Input Fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Career Goal:").pack()
career_goal_var = tk.StringVar(root)
career_goal_var.set("data_scientist")  # Default value
career_goal_dropdown = tk.OptionMenu(root, career_goal_var, *career_paths.keys())
career_goal_dropdown.pack()

tk.Label(root, text="Current Skills (comma separated):").pack()
skills_entry = tk.Entry(root, width=50)
skills_entry.pack()

# Button to generate recommendations
recommend_button = tk.Button(root, text="Get Recommendations", command=generate_learning_path)
recommend_button.pack(pady=10)

# Output Display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=450, justify="left", anchor="w")
result_label.pack(pady=10)

# Run the application
root.mainloop()


