import sys
import random


def main():
    # TODO: your code here

    # 1. Get the command line arguments via sys.argv

    # 2. Open the correct file open(rf'questions\<filename>.txt)'

    # 3. Iterate over the file

    #       3.1. Parse the line (use s.split())
    #       3.2 Create a list of options
    #       3.3 random.shuffle(l)
    pass
    sys.argv
    proffesion=sys.argv[1]
    num_questions=int(sys.argv[2])

    def view_question(text):
        text=text.strip()
        text=text.split(';')
        question=text[0]
        correct_answer=text[1]
        options=(f'{text[2]},{text[1]}')
        options=options.split(',')
        random.shuffle(options)
        return (question, options,correct_answer)
    
    questions=[]
    good_ans=0
    with open(rf'questions\{proffesion}.txt', mode='r') as file:
        for line in file:
            questions.append(view_question(line))

        random.shuffle(questions)
        for i in range(num_questions):
            print(questions[i][0])
            for j, answer in enumerate(questions[i][1]):
                print(f'{j+1}. {answer}')

            print("enter the correct answer")

            a=int(input())
            if questions[i][1][a-1]==questions[i][2]:
                good_ans+=1
        
        print(f'number of correct answers is {good_ans}/{num_questions}')


if __name__ == '__main__':
    main()
