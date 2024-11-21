import random

questions = [
    {
        "question": "Which of the following is a primary key in a database?",
        "choices": ["A. A unique identifier for a record", "B. A duplicate value", "C. A foreign key", "D. A column with NULL values"],
        "answer": "A"
    },
    {
        "question": "What is the time complexity of binary search on a sorted array?",
        "choices": ["A. O(n)", "B. O(log n)", "C. O(n^2)", "D. O(1)"],
        "answer": "B"
    },
    {
        "question": "Which data structure is used for implementing recursion?",
        "choices": ["A. Queue", "B. Stack", "C. Linked List", "D. Array"],
        "answer": "B"
    },
    {
        "question": "In SQL, which command is used to retrieve data from a table?",
        "choices": ["A. INSERT", "B. UPDATE", "C. DELETE", "D. SELECT"],
        "answer": "D"
    },
    {
        "question": "What is the output of the following code snippet in Python? \n```python\nprint(2 ** 3)\n```",
        "choices": ["A. 6", "B. 8", "C. 9", "D. 7"],
        "answer": "B"
    },
    {
        "question": "Which of the following is NOT a sorting algorithm?",
        "choices": ["A. Quick Sort", "B. Bubble Sort", "C. Depth First Search", "D. Merge Sort"],
        "answer": "C"
    },
    {
        "question": "Which SQL keyword is used to remove duplicate rows from a result set?",
        "choices": ["A. DISTINCT", "B. UNIQUE", "C. DELETE", "D. FILTER"],
        "answer": "A"
    },
    {
        "question": "What does the following C++ code snippet do? \n```cpp\nint arr[5] = {1, 2, 3, 4, 5};\ncout << arr[3];\n```",
        "choices": ["A. Prints 4", "B. Prints 5", "C. Prints 3", "D. Throws an error"],
        "answer": "A"
    },
    {
        "question": "Which data structure is commonly used to implement Dijkstra's algorithm?",
        "choices": ["A. Binary Search Tree", "B. Graph", "C. Priority Queue", "D. Stack"],
        "answer": "C"
    },
    {
        "question": "In Java, which keyword is used to create a subclass?",
        "choices": ["A. extends", "B. implements", "C. inherits", "D. super"],
        "answer": "A"
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
        
if __name__ == "__main__":
    main()