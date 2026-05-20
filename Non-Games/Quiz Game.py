# Imports #
import tkinter as tk
from tkinter import messagebox
import json
import random

# Loading Questions #
def load_questions():
    try:
        with open("questions.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

questions = load_questions()

# Questions (WARNING : Don't Open) #
if not questions:
    questions = [
    {"question": "Who proposed the theory of relativity?",
     "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Niels Bohr"],
     "answer": "Albert Einstein"},

    {"question": "Which Mughal emperor built the Taj Mahal?",
     "options": ["Akbar", "Shah Jahan", "Aurangzeb", "Babur"],
     "answer": "Shah Jahan"},

    {"question": "What is the SI unit of force?",
     "options": ["Newton", "Joule", "Pascal", "Watt"],
     "answer": "Newton"},

    {"question": "Which river is known as the 'Sorrow of Bihar'?",
     "options": ["Ganga", "Kosi", "Yamuna", "Brahmaputra"],
     "answer": "Kosi"},

    {"question": "Who was the first woman Prime Minister of India?",
     "options": ["Indira Gandhi", "Sarojini Naidu", "Pratibha Patil", "Sonia Gandhi"],
     "answer": "Indira Gandhi"},

    {"question": "Which planet is known as the 'Red Planet'?",
     "options": ["Mars", "Venus", "Mercury", "Saturn"],
     "answer": "Mars"},

    {"question": "What is the chemical formula of common salt?",
     "options": ["NaCl", "KCl", "CaCO3", "Na2SO4"],
     "answer": "NaCl"},

    {"question": "Who discovered penicillin?",
     "options": ["Louis Pasteur", "Alexander Fleming", "Joseph Lister", "Robert Koch"],
     "answer": "Alexander Fleming"},

    {"question": "Which battle in 1757 marked the beginning of British rule in India?",
     "options": ["Battle of Panipat", "Battle of Plassey", "Battle of Buxar", "Battle of Haldighati"],
     "answer": "Battle of Plassey"},

    {"question": "Which gas is most abundant in Earth's atmosphere?",
     "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
     "answer": "Nitrogen"},

    {"question": "Who invented the World Wide Web?",
     "options": ["Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Charles Babbage"],
     "answer": "Tim Berners-Lee"},

    {"question": "Which Indian state is known as the 'Spice Garden of India'?",
     "options": ["Kerala", "Goa", "Tamil Nadu", "Assam"],
     "answer": "Kerala"},

    {"question": "Which organelle is called the 'powerhouse of the cell'?",
     "options": ["Nucleus", "Mitochondria", "Ribosome", "Chloroplast"],
     "answer": "Mitochondria"},

    {"question": "Who wrote the Indian national anthem?",
     "options": ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Mahatma Gandhi"],
     "answer": "Rabindranath Tagore"},

    {"question": "Which element has the chemical symbol 'Fe'?",
     "options": ["Lead", "Iron", "Silver", "Copper"],
     "answer": "Iron"},

    {"question": "Which Indian mathematician gave the concept of zero?",
     "options": ["Aryabhata", "Ramanujan", "Bhaskara", "Euclid"],
     "answer": "Aryabhata"},

    {"question": "Which is the largest gland in the human body?",
     "options": ["Pancreas", "Liver", "Thyroid", "Kidney"],
     "answer": "Liver"},

    {"question": "Which Indian leader is known as the 'Iron Man of India'?",
     "options": ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Subhash Chandra Bose", "Bhagat Singh"],
     "answer": "Sardar Vallabhbhai Patel"},

    {"question": "Which blood group is called the universal donor?",
     "options": ["A", "B", "AB", "O negative"],
     "answer": "O negative"},

    {"question": "Which Indian scientist is known as the 'Missile Man of India'?",
     "options": ["Homi Bhabha", "Vikram Sarabhai", "A.P.J. Abdul Kalam", "C.V. Raman"],
     "answer": "A.P.J. Abdul Kalam"},

    {"question": "Which is the longest bone in the human body?",
     "options": ["Femur", "Tibia", "Humerus", "Fibula"],
     "answer": "Femur"},

    {"question": "Which Indian state is famous for the Sun Temple at Konark?",
     "options": ["Odisha", "Rajasthan", "Madhya Pradesh", "Gujarat"],
     "answer": "Odisha"},

    {"question": "Which Mughal emperor introduced the Din-i-Ilahi religion?",
     "options": ["Akbar", "Aurangzeb", "Humayun", "Babur"],
     "answer": "Akbar"},

    {"question": "Which Indian physicist won the Nobel Prize for scattering of light?",
     "options": ["C.V. Raman", "Homi Bhabha", "Meghnad Saha", "Satyendra Nath Bose"],
     "answer": "C.V. Raman"},

    {"question": "Which Indian freedom fighter gave the slogan 'Give me blood and I will give you freedom'?",
     "options": ["Mahatma Gandhi", "Bhagat Singh", "Subhash Chandra Bose", "Bal Gangadhar Tilak"],
     "answer": "Subhash Chandra Bose"},

    {"question": "What is the chemical symbol of Sodium?",
     "options": ["So", "Na", "S", "Sn"],
     "answer": "Na"},

    {"question": "Who discovered gravity after observing a falling apple?",
     "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"],
     "answer": "Isaac Newton"},

    {"question": "What is the largest planet in our solar system?",
     "options": ["Earth", "Saturn", "Jupiter", "Mars"],
     "answer": "Jupiter"},

    {"question": "Who was the first President of independent India?",
     "options": ["Jawaharlal Nehru", "Dr. Rajendra Prasad", "Sardar Patel", "B. R. Ambedkar"],
     "answer": "Dr. Rajendra Prasad"},

    {"question": "What is the process by which plants make their food?",
     "options": ["Respiration", "Transpiration", "Photosynthesis", "Digestion"],
     "answer": "Photosynthesis"},

    {"question": "Which gas is most abundant in the Earth's atmosphere?",
     "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
     "answer": "Nitrogen"},

    {"question": "Who wrote the Indian National Anthem?",
     "options": ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarojini Naidu", "Subhash Chandra Bose"],
     "answer": "Rabindranath Tagore"},

    {"question": "What is the boiling point of water at sea level in Celsius?",
     "options": ["90°C", "95°C", "100°C", "110°C"],
     "answer": "100°C"},

    {"question": "Which Mughal emperor built the Taj Mahal?",
     "options": ["Akbar", "Babur", "Shah Jahan", "Aurangzeb"],
     "answer": "Shah Jahan"},

    {"question": "What is the unit of electric current?",
     "options": ["Volt", "Watt", "Ampere", "Ohm"],
     "answer": "Ampere"},

    {"question": "Which planet is known as the Red Planet?",
     "options": ["Venus", "Mars", "Mercury", "Saturn"],
     "answer": "Mars"},

    {"question": "Who is known as the Father of the Nation in India?",
     "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Bhagat Singh", "Lal Bahadur Shastri"],
     "answer": "Mahatma Gandhi"},

    {"question": "What type of energy is stored in food?",
     "options": ["Kinetic Energy", "Chemical Energy", "Solar Energy", "Nuclear Energy"],
     "answer": "Chemical Energy"},

    {"question": "Which freedom movement was launched in 1942?",
     "options": ["Non-Cooperation Movement", "Civil Disobedience Movement", "Quit India Movement", "Swadeshi Movement"],
     "answer": "Quit India Movement"},

    {"question": "What is the hardest natural substance on Earth?",
     "options": ["Gold", "Iron", "Diamond", "Quartz"],
     "answer": "Diamond"},

    {"question": "Which river is known as the longest river in the world?",
     "options": ["Amazon", "Ganga", "Nile", "Yangtze"],
     "answer": "Nile"},

    {"question": "Who invented the telephone?",
     "options": ["Thomas Edison", "Alexander Graham Bell", "James Watt", "Michael Faraday"],
     "answer": "Alexander Graham Bell"},

    {"question": "What is the main function of red blood cells?",
     "options": ["Fight infection", "Clot blood", "Carry oxygen", "Produce hormones"],
     "answer": "Carry oxygen"},

    {"question": "Which continent is the Sahara Desert located in?",
     "options": ["Asia", "Africa", "Australia", "South America"],
     "answer": "Africa"},

    {"question": "Who was the first woman Prime Minister of India?",
     "options": ["Sarojini Naidu", "Indira Gandhi", "Pratibha Patil", "Sushma Swaraj"],
     "answer": "Indira Gandhi"},

    {"question": "What is the SI unit of force?",
     "options": ["Joule", "Newton", "Pascal", "Watt"],
     "answer": "Newton"},

    {"question": "Which organ purifies blood in the human body?",
     "options": ["Heart", "Lungs", "Kidney", "Liver"],
     "answer": "Kidney"},

    {"question": "Which is the smallest state in India by area?",
     "options": ["Sikkim", "Tripura", "Goa", "Nagaland"],
     "answer": "Goa"},

    {"question": "Which scientist proposed the three laws of motion?",
     "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Johannes Kepler"],
     "answer": "Isaac Newton"},

    {"question": "What is the capital of Japan?",
     "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
     "answer": "Tokyo"}
    ]

# Shuffeling Question #
random.shuffle(questions)

# Tk Window Setup #
root = tk.Tk()
root.title("Quiz Game")

# Questions & Answers Window #
current_question = 0
score = 0

question_label = tk.Label(root, text="")
question_label.pack(pady=10)

options_frame = tk.Frame(root)
options_frame.pack()

options_frame = tk.Frame(root)
options_frame.pack(pady=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

used_hint = False
hint_count = 0
score = 0
current_question = 0

used_hint = False
hint_count = 0
score = 0
current_question = 0

# Defined Fucnctions #
def show_question():
    question_label.config(text=questions[current_question]["question"])
    for widget in options_frame.winfo_children():
        widget.destroy()
    for option in questions[current_question]["options"]:
        tk.Button(options_frame, text=option,
                  command=lambda opt=option: check_answer(opt)).pack(side=tk.LEFT, padx=5, pady=5)

def update_hint_label():
    hint_label.config(text=f"Hints left: {5 - hint_count}")

def hint():
    global used_hint, hint_count
    if hint_count >= 5:
        messagebox.showwarning("Hint Limit", "You've used all 5 hints.")
        return
    used_hint = True
    hint_count += 1
    correct = questions[current_question]["answer"]
    hint_text = f"The correct answer starts with: {correct[0]}"
    messagebox.showinfo("Hint", hint_text)
    hint_button.config(state="disabled")
    update_hint_label()

def check_answer(selected):
    global current_question, score, used_hint
    correct = questions[current_question]["answer"]

    if selected == correct:
        if used_hint:
            score += 0.5
            messagebox.showinfo("Correct!", "You used a hint. Half point awarded.")
        else:
            score += 1
            messagebox.showinfo("Correct!", "Well done!")
    else:
        messagebox.showerror("Wrong!", f"Correct answer was: {correct}")

    score_message = f"Current Score: {score}/{len(questions)}"
    messagebox.showinfo("Score Update", score_message)

    used_hint = False
    if hint_count >= 5:
        hint_button.config(state="disabled")
    else:
        hint_button.config(state="normal")
    update_hint_label()

    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        messagebox.showinfo("Game Over", f"Your score: {score}/{len(questions)}")

def quit_game():
    messagebox.showinfo("Quiz Over", f"Your score: {score}/{len(questions)}")
    root.quit()

# Buttons #
hint_button = tk.Button(bottom_frame, text="Hint", command=hint)
hint_button.pack(side=tk.LEFT, padx=10)

hint_label = tk.Label(bottom_frame, text="Hints left: 5")
hint_label.pack(side=tk.LEFT)

tk.Button(bottom_frame, text="Quit", command=quit_game).pack(side=tk.LEFT, padx=10)

show_question()
root.mainloop()
