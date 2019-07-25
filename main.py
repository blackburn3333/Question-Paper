import random

words = ["Apple", "Banana", "Mango", "Blueberries", "Cherries", "Kiwi", "Orange", "Olive", "Limes"]

questions = [
    "How many letters does the word contain?",
    "How many vowels does the word contain?",
    "How many consonants does the word contain?",
    "What is letter # of the word? "
]

def find_vowels_and_consonants_count(word):
    consonants_count = 0
    vowels_count = 0
    word = word.lower()
    for i in word:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowels_count = vowels_count + 1
        else:
            consonants_count = consonants_count + 1
    return [vowels_count, consonants_count]


def how_man_letters_in_word(word):
    letter_count = 0
    for i in word:
        letter_count = letter_count + 1
    return letter_count


def pick_what_is_the_letter(word, question):
    word_length = 0
    for x in word:
        word_length = word_length + 1
    letter_position = random.randint(1, word_length)
    generated_quiz = question.replace('#', str(letter_position))
    answer = word[letter_position - 1]
    return [generated_quiz, answer]


def select_random_five_words(words_list):
    return random.sample(words_list, 5)


def select_questions(question_list):
    select_question_from_fifth = [question_list[random.randint(1, 3)]]
    selected_random_questions = random.sample(question_list, 4)
    return sorted(select_question_from_fifth + selected_random_questions)


def make_question_paper(selected_words_list, selected_questions_list):
    prepared_paper = []

    for x in range(5):
        if selected_questions_list[x] == questions[2]:
            answer = find_vowels_and_consonants_count(selected_words_list[x])
            prepared_paper.insert(x, [str(selected_questions_list[x]), str(selected_words_list[x]), answer[1]])

        elif selected_questions_list[x] == questions[1]:
            answer = find_vowels_and_consonants_count(selected_words_list[x])
            prepared_paper.insert(x, [str(selected_questions_list[x]), str(selected_words_list[x]), answer[0]])

        elif selected_questions_list[x] == questions[0]:
            answer = how_man_letters_in_word(selected_words_list[x])
            prepared_paper.insert(x, [str(selected_questions_list[x]), str(selected_words_list[x]), answer])

        elif selected_questions_list[x] == questions[3]:
            generated = pick_what_is_the_letter(selected_words_list[x], selected_questions_list[x])
            prepared_paper.insert(x, [str(generated[0]), str(selected_words_list[x]), generated[1]])

    return prepared_paper

print("Welcome to English Test Pro !")

selected_words = select_random_five_words(words)
selected_questions = select_questions(questions)
generated_paper = make_question_paper(selected_words, selected_questions)

score = 0
quiz_no = 0


for x in generated_paper:
    print("Word " + str(quiz_no + 1) + "/5: " + generated_paper[quiz_no][1])
    print(generated_paper[quiz_no][0])
    user_answer = input()
    if str(user_answer) == str(generated_paper[quiz_no][2]):
        score = score + 1
        print("Correct !")
    else:
        print("Incorrect ! Correct answer was " + str(generated_paper[quiz_no][2]))
    quiz_no = quiz_no + 1

print("Game Over. Your score is " + str(score) + "/5")
