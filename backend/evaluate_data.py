import os
import json
from collections import defaultdict
from backend import load_spreadsheet
import prompts

response_prompt_filename = 'decision_tree/response_prompts.csv'
question_prompt_filename = 'decision_tree/question_prompts.csv'

def main():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/conversations"))
    filenames = os.listdir(file_path)
    filenames.remove('conversation_format.txt')
    response_prompts = load_spreadsheet('../data/' + response_prompt_filename, 'response')
    question_prompts = load_spreadsheet('../data/' + question_prompt_filename, 'response')
    cv_emotions = []
    reported_emotions = []
    happy_customers = 0
    unhappy_customers = 0
    questions_reached = defaultdict(int)
    for filename in filenames:
        read_file = open(os.path.join(file_path, filename), "r")
        convo_string = read_file.read()
        read_file.close()
        convo_list = json.loads(convo_string)
        cv_emotion = None
        reported_emotion = None
        for qid, rid in convo_list:
            if qid == 'Emotion':
                cv_emotion = rid
            elif qid == '23':
                if rid == '230':
                    happy_customers += 1
                if rid == '231':
                    unhappy_customers += 1
            elif qid == '24':
                reported_emotion = rid
            elif qid in question_prompts.keys():
                questions_reached[qid] = questions_reached[qid] + 1
            if cv_emotion and reported_emotion:
                cv_emotions.append(cv_emotion)
                reported_emotions.append(reported_emotion)

    question_popularity = sorted([(value, key) for key, value in questions_reached.items()], reverse=True)
    questions_to_display = [(question_prompts[id].get_text(), num) for num, id in question_popularity]
    print('Out of {} users, {} found this useful and {} did not'.format(happy_customers + unhappy_customers, happy_customers, unhappy_customers))
    print('Most popular questions:')
    print(questions_to_display)

    detectable_emotions = list(set(cv_emotions))
    reportable_emotions = list(set(reported_emotions))

    con_mat = [[0 for i in reportable_emotions] for j in detectable_emotions]
    for detected, reported in zip(cv_emotions, reported_emotions):
        con_mat[detectable_emotions.index(detected)][reportable_emotions.index(reported)]+=1

    print([response_prompts[id].get_text() for id in reportable_emotions])
    for i in range(len(detectable_emotions)):
        print(detectable_emotions[i], con_mat[i])




if __name__ == "__main__":
    main()