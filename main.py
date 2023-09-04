from quiz import Quiz
import random
import time

problems = []
question_set_one = [
    {
        'question': 'How many hours are there in a day?',
        'answers': '18, 24, 12, 06',
        'correct_answer': '24',
        'correct_answer_no': '2'
    },

    {
        'question': 'How many letters are there in the English alphabet?',
        'answers': '25, 27, 26, 28',
        'correct_answer': '26',
        'correct_answer_no': '3'
    },

    {
        'question': 'Name the house made of ice?',
        'answers': 'Cave, Home, Igloo, Apartment',
        'correct_answer': 'Igloo',
        'correct_answer_no': '3'
    },

    {
        'question': 'Name the largest mammal?',
        'answers': 'Blue Whale, Human, Gorilla, Bat',
        'correct_answer': 'Blue Whale',
        'correct_answer_no': '1'
    },

    {
        'question': 'When then world war II ended?',
        'answers': '1945, 1946, 1947, 1948',
        'correct_answer': '1947',
        'correct_answer_no': '3'
    },
]
question_set_two = [
    {
        'question': 'Who is the current president of USA?',
        'answers': 'John F Kennedy, Donald Trump, Barak Obama, Joe Biden',
        'correct_answer': 'Joe Biden',
        'correct_answer_no': '4'
    },

    {
        'question': 'How many planets in our solar system?',
        'answers': '5, 8, 9, 7',
        'correct_answer': '8',
        'correct_answer_no': '2'
    },

    {
        'question': 'Who invented the AC current?',
        'answers': 'Edison, Einstein, Babbage, Tesla',
        'correct_answer': 'Tesla',
        'correct_answer_no': '4'
    },

    {
        'question': 'Who is the founder of Facebook?',
        'answers': 'Elon Musk, Mark Zuckerberg, Steve Jobs, Bill Gates',
        'correct_answer': 'Mark Zuckerberg',
        'correct_answer_no': '2'
    },

    {
        'question': 'Can we support LGBTQ+ community?',
        'answers': 'Yes! We do., No! Be a Sigma MF.',
        'correct_answer': 'No! Be a Sigma MF.',
        'correct_answer_no': '2'
    },
]

problems.append(question_set_one)
problems.append(question_set_two)

# Create an Object
quiz = Quiz()

for problem in random.choice(problems):
    # Setting up the variables
    answers = problem['answers'].split(", ")

    # Asking for answer
    given_answer = quiz.ask_answer(problem['question'], answers)

    # Check for the result
    try:
        quiz.check_answer(given_answer, problem['correct_answer'].lower(), problem['correct_answer_no'])

    except ValueError:
        print("Invalid Answer. \n")
        time.sleep(1)

    except:
        print("Something went wrong 😑! \n")
        time.sleep(1)

else:
    # Showing results and grades
    quiz.show_result()
