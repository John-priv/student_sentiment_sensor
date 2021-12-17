'''
Script to analyze the data
'''

import os
import csv


def get_solutions():
    '''
    Loads solution_prompt text into a dict, where [key = solution_text], [value = 0]
    '''
    solution_p = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/decision_tree/solution_prompts.csv"))
    solutions = {}
    with open(solution_p, 'r') as opened_file:
        csv_file = csv.reader(opened_file)
        next(csv_file)  # Skips header line
        for row in csv_file:
            solution_entry = {}
            try:
                solution_id = row[0]
                text = row[1]
                solution_entry['Counter'] = 0
                solution_entry['Text'] = text
                solutions[solution_id] = solution_entry
            except Exception as e:
                print('Error in get_solutions: {} --> {}'.format(row, e))

    return solutions


def get_file_list(stored_data_dir):
    '''
    Gets u_id from student_sentiment_sensor/data/stored_user_data
        - u_id is used to track runs. Used to create log data in "u_id.dat" files

    Outputs:
        u_id (int): highest u_id currently stored in student_sentiment_sensor/data/stored_user_data/"u_id.dat"
    '''
    file_list = [f for f in os.listdir(stored_data_dir) if os.path.isfile(os.path.join(stored_data_dir, f))]
    file_list.sort()    # Sort the list for funsies
    if '0.dat' in file_list:
        file_list.remove('0.dat')
    return file_list


def get_file_data(stored_data_dir, file_list):
    '''
    Extracts relevant data from the log file directory.
        - Takes in an abs_path to a logging directory, and a list of files in that directory to open
        - Currently only grabs data that is deemed "useful" for the late capstone stage
    '''
    extracted_data = {}
    for file_name in file_list:
        file_data = {}
        file_path = os.path.abspath(stored_data_dir + '/' + file_name)
        with open(file_path, 'r') as opened_file:
            file_read = opened_file.read().split('\n')
            for line in file_read:
                try:
                    fields = line.split('|')
                    if fields[0] == 'Emotion_CV':
                        file_data['Emotion_CV'] = fields[-1]
                    if fields[0] == 'Question':
                        if '23' in fields:
                            file_data['Helpful'] = fields[-1]
                        if '24' in fields:
                            file_data['Emotion_User_Input'] = fields[-1]
                    elif fields[0] == 'Solution':
                        file_data['Solution'] = fields[-2]
                        file_data['Solution_ID'] = fields[1]
                except Exception as e:
                    print('Error in get_file_data: {} --> {}'.format(line, e))

        if file_data != {}:
            extracted_data[file_name] = file_data

    return extracted_data


def calculate_stats(file_data, solutions):
    '''
    Get statistics and stuff from the file data
    '''
    stats = {}
    counter = {}
    total_responses = 0
    yes_count = 0
    no_count = 0

    for data_dict in file_data.values():
        # print(data_dict)
        try:
            solutions[data_dict['Solution_ID']]['Counter'] += 1     # Count number of times response was chosen
            total_responses += 1
        except Exception as e:
            print('Error in calculate_stats: {} --> {} --> {}'.format(data_dict, type(e), e))

    total_percent = 0
    duplicate_array = []    # Literally useless; just for personal testing
    for data_dict in file_data.values():
        try:
            solution_id = data_dict['Solution_ID']
            counter[solution_id] = {}
            counter[solution_id]['Counter'] = solutions[data_dict['Solution_ID']]['Counter']
            counter[solution_id]['Percent'] = counter[solution_id]['Counter'] / total_responses
            counter[solution_id]['Text'] = data_dict['Solution']
            counter[solution_id]['Emotion_User_Input'] = data_dict['Emotion_User_Input']
            counter[solution_id]['Emotion_CV'] = data_dict['Emotion_CV']
            counter[solution_id]['Helpful'] = data_dict['Helpful']
            if data_dict['Helpful'] == 'Yes':
                yes_count += 1
            else:
                no_count += 1

            if solution_id not in duplicate_array:
                total_percent += counter[solution_id]['Percent']
                duplicate_array.append(solution_id)
                # print('total_percent = {}'.format(total_percent))   # Math check line
        except Exception as e:
            print('Error in calculate_stats: {} --> {} --> {}'.format(data_dict, type(e), e))

    stats['Solutions'] = solutions
    stats['Counters'] = counter
    stats['Helpful_Y'] = yes_count
    stats['Helpful_N'] = no_count
    stats['Helpful_Percent'] = 100 * (yes_count / (yes_count + no_count))

    return stats


def analyze_stats(stats, options):
    if 'count_solution' in options:
        for element in stats['Counters']:
            print('Count: {}         Percent: {}         Solution: {}'.format(stats['Counters'][element]['Counter'],
                                                                              stats['Counters'][element]['Percent'],
                                                                              stats['Counters'][element]['Text']))
    if 'count_id' in options:
        for element in stats['Counters']:
            print('Count: {}         Percent: {}         Solution: {}'.format(stats['Counters'][element]['Counter'],
                                                                              stats['Counters'][element]['Percent'],
                                                                              element))

    if 'helpful' in options:
        print('yes_count = {}     no_count = {}     percent_helpful = {}'.format(stats['Helpful_Y'],
                                                                                 stats['Helpful_N'],
                                                                                 stats['Helpful_Percent']))


def analyze():
    '''
    Main function; analyzes the stored data
    '''
    options = ['count_id', 'helpful']

    stored_data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/stored_user_data/"))
    file_list = get_file_list(stored_data_dir)
    file_data = get_file_data(stored_data_dir, file_list)
    solutions = get_solutions()
    stats = calculate_stats(file_data, solutions)
    analyze_stats(stats, options)


if __name__ == "__main__":
    analyze()
