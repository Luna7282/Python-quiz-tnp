import random

questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "What is 2 + 2?",
        "choices": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["A. H2O", "B. CO2", "C. O2", "D. H2"],
        "answer": "A"
    },
    {
        "question": "What is the speed of light?",
        "choices": ["A. 300,000 km/s", "B. 150,000 km/s", "C. 450,000 km/s", "D. 600,000 km/s"],
        "answer": "A"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "choices": ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"],
        "answer": "C"
    },
    {
        "question": "Who discovered penicillin?",
        "choices": ["A. Marie Curie", "B. Alexander Fleming", "C. Louis Pasteur", "D. Isaac Newton"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the square root of 64?",
        "choices": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Who wrote '1984'?",
        "choices": ["A. George Orwell", "B. Aldous Huxley", "C. F. Scott Fitzgerald", "D. J.D. Salinger"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Canada?",
        "choices": ["A. Toronto", "B. Vancouver", "C. Ottawa", "D. Montreal"],
        "answer": "C"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": ["A. Gold", "B. Iron", "C. Diamond", "D. Platinum"],
        "answer": "C"
    },
    {
        "question": "Who developed the theory of relativity?",
        "choices": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Australia?",
        "choices": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal?",
        "choices": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "choices": ["A. Tomato", "B. Onion", "C. Avocado", "D. Pepper"],
        "answer": "C"
    },
    {
        "question": "Who was the first president of the United States?",
        "choices": ["A. Abraham Lincoln", "B. Thomas Jefferson", "C. George Washington", "D. John Adams"],
        "answer": "C"
    }
]

random.shuffle(questions)
def main():
    languages = ["C++", "Java", "Python"]
    print("Choose a language:")
    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang}")
    
    choice = int(input("Enter the number of your choice: "))
    if choice not in range(1, 4):
        print("Invalid choice. Exiting.")
        return
    
    selected_language = languages[choice -1]
    print(f"You selected {selected_language}. Here are your questions:\n")
    
    score = 0
    for i, q in enumerate(questions[:5], 1):
        print(f"Q{i}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        answer = input("Your answer: ").strip().upper()
        if answer == q['answer']:
            score += 1
    
    print(f"Your score: {score}/5")
        
if __name__ == "_main_":
    main()