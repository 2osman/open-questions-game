

import random

# List of topics
topics = ["Technology", "History", "Travel", "Sports", "Science", "Music", "Business", "Movies", "Psychology", "Education"]

# Function to check if a question is open-ended
def is_open_question(question):
    closed_keywords = ["do", "does", "is", "are", "can", "will", "should", "could", "would", "have", "has"]
    words = question.lower().split()
    return not any(word in words for word in closed_keywords)

def play_game():
    topic = random.choice(topics)  # Randomly choose a topic
    print(f"🎯 Your topic is: **{topic}**")
    print("Ask 10 open-ended questions about this topic. If you ask a closed question, you restart at 0.")

    count = 0

    while count < 10:
        question = input(f"Question {count + 1}: ")

        if is_open_question(question):
            count += 1
            print("✅ Good question! Keep going.")
        else:
            count = 0
            print("❌ That was a closed question! Restarting at 0.")

    print(f"🎉 Congratulations! You asked 10 open-ended questions about **{topic}**.")

if __name__ == "__main__":
    play_game()
