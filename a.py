# Diabetes
import tkinter as tk
from tkinter import ttk, scrolledtext
import random

class ElderlyCarePrototype:
    def __init__(self, name, age, health_conditions):
        self.name = name
        self.age = age
        self.health_conditions = health_conditions
        self.nutrition_plan = {}
        self.exercise_routine = {}

    def create_nutrition_plan(self):
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        random.shuffle(days_of_week)

        self.nutrition_plan = {day: self.generate_random_meals() for day in days_of_week}

    def generate_random_meals(self):
        meals = ['Oatmeal with fruits', 'Grilled chicken salad', 'Quinoa and vegetables',
                 'Greek yogurt with nuts', 'Lentil soup', 'Baked fish with sweet potatoes',
                 'Whole grain toast with avocado', 'Vegetable stir-fry', 'Brown rice with beans',
                 'Smoothie with spinach and berries', 'Turkey sandwich with whole grain bread',
                 'Quinoa and roasted vegetables', 'Scrambled eggs with spinach', 'Chickpea curry',
                 'Baked chicken with broccoli', 'Cottage cheese with pineapple',
                 'Spinach and feta omelet', 'Grilled shrimp with quinoa', 'Whole grain pancakes with berries', 'Minestrone soup']

        random.shuffle(meals)
        return meals[:3]  # Selecting only the first three meals for brevity

    def create_exercise_routine(self):
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        random.shuffle(days_of_week)

        self.exercise_routine = {day: self.generate_random_exercises() for day in days_of_week}

    def generate_random_exercises(self):
        exercises = ['30 minutes of brisk walking', '20 minutes of strength training (bodyweight exercises)',
                     'Yoga or stretching exercises for 30 minutes', '45 minutes of moderate-intensity cardio (cycling or swimming)',
                     '20 minutes of light aerobic exercises (walking or low-impact aerobics)', 'Rest day or gentle activities like gardening',
                     'Outdoor activity like hiking or gardening']

        random.shuffle(exercises)
        return exercises[:2]  # Selecting only the first two exercises for brevity


class ElderlyCareGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Elderly Care Prototype")
        self.geometry("800x400")

        self.label = tk.Label(self, text="Enter Information for Elderly Care:")
        self.label.pack(pady=10)

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        self.age_label = tk.Label(self, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack(pady=5)

        self.conditions_label = tk.Label(self, text="Health Conditions (comma-separated):")
        self.conditions_label.pack()
        self.conditions_entry = tk.Entry(self)
        self.conditions_entry.pack(pady=5)

        self.generate_button = tk.Button(self, text="Generate Plan", command=self.generate_plan)
        self.generate_button.pack(pady=10)

        self.result_treeview = ttk.Treeview(self, columns=('Day', 'Exercise Plan', 'Nutrition Plan'), show='headings')
        self.result_treeview.heading('Day', text='Day')
        self.result_treeview.heading('Exercise Plan', text='Exercise Plan')
        self.result_treeview.heading('Nutrition Plan', text='Nutrition Plan')
        self.result_treeview.pack(pady=10, padx=10, fill='both', expand=True)

    def generate_plan(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        conditions = [condition.strip() for condition in self.conditions_entry.get().split(',')]

        sunita = ElderlyCarePrototype(name=name, age=age, health_conditions=conditions)
        sunita.create_nutrition_plan()
        sunita.create_exercise_routine()

        for day, (exercise_plan, nutrition_plan) in zip(sunita.exercise_routine.keys(), zip(sunita.exercise_routine.values(), sunita.nutrition_plan.values())):
            self.result_treeview.insert('', 'end', values=(day, '\n'.join(exercise_plan), '\n'.join(nutrition_plan)))


if __name__ == "__main__":
    app = ElderlyCareGUI()
    app.mainloop()
