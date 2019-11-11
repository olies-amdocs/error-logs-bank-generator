from ErrorLog import ErrorLog
from ErrorObservation import ErrorObservation
import csv

def error_txt_to_csv(ms_name):
    
    with open('./error-logs/esb-' + ms_name + '-errors.txt', 'r', encoding='utf-8-sig') as csv_in_file:
        reader = csv.reader(csv_in_file, delimiter='|')
        print('Creating esb-'+ ms_name + '-errors.csv file...')
        print('Writing into esb-'+ ms_name + '-errors.csv file...')
        
        with open('./error-logs/esb-'+ ms_name + '-errors.csv', 'w',  newline='') as csv_out_file:
            writer = csv.writer(csv_out_file, delimiter=',')
            temp = ErrorLog()
            writer.writerow(temp.__dict__.keys())

            for row in reader:
                writer.writerow(get_error_log_from_txt(row))

        print('Finished processing esb-'+ ms_name + '-errors.csv file... \n')
    
def get_error_log_from_csv(ms_name):
    error_logs = []
    print('Reading /error-logs/esb-' + ms_name + '-errors.csv file...')
    with open('./error-logs/esb-' + ms_name + '-errors.csv', 'r', encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            error_logs.append(get_error_log_from_dict(row))

    print('Done retrieving data from /error-logs/esb-' + ms_name + '-errors.csv file... \n')
    return error_logs

def get_error_log_from_dict(data):
    error_log = ErrorLog()
    error_log.date = data['_date']
    error_log.log_level = data['_log_level']
    error_log.log_id = data['_log_id']
    error_log.log_event = data['_log_event']
    error_log.route = data['_route']
    error_log.transaction_id = data['_transaction_id']
    error_log.user_email = data['_user_email']
    error_log.package = data['_package']
    error_log.error_message = data['_error_message']
    return error_log

def get_error_log_from_txt(data):
    error_log = ErrorLog()
    error_log.date = data[0]
    error_log.log_level = data[1]
    error_log.log_id = data[2]
    error_log.log_event = data[3]
    error_log.route = data[4]
    error_log.transaction_id = data[6]
    error_log.user_email = data[9]
    error_log.package = data[13]
    error_log.error_message = data[14]
    return error_log

def get_error_observation_from_error_log(error_log):
    error_observation = ErrorObservation()
    error_observation.date = error_log.date
    error_observation.route = error_log.route
    error_observation.transaction_id = error_log.transaction_id
    error_observation.user_email = error_log.user_email
    error_observation.package = error_log.package
    error_observation.error_message = error_log.error_message
    return error_observation

def generate_error_observations(error_logs):
    
    error_observation_dict = {}

    print('Iterating through error_logs list...')
    for error_log in error_logs:
        if(error_log.package in error_observation_dict):
            error_observation = error_observation_dict[error_log.package]
            if(is_error_identical(error_observation.error_message, error_log.error_message)):
               error_observation.add_count()
            else:
                error_observation_dict[error_log.package] = get_error_observation_from_error_log(error_log)
        else:
            error_observation_dict[error_log.package] = get_error_observation_from_error_log(error_log)

    print('Done iterating through error_logs list... \n')
    return error_observation_dict.values()

def is_error_identical(error1, error2):
    if(len(common_words(error1, error2)) >= 5):
        return True
    return False

#https://www.geeksforgeeks.org/python-program-to-find-uncommon-words-from-two-strings
def common_words(A, B): 
  
    # count will contain all the word counts 
    count = {} 
      
    # insert words of string A to hash 
    for word in A.split(): 
        count[word] = count.get(word, 0) + 1
      
    # insert words of string B to hash 
    for word in B.split(): 
        count[word] = count.get(word, 0) + 1
  
    # return required list of words 
    return [word for word in count if count[word] > 1]

def write_error_observations(error_observations, ms_name):
    print('Writing into observation csv file...')
    with open('./error-logs/esb-' + ms_name + '-observations.csv', 'w',  newline='') as csv_out_file:
        writer = csv.writer(csv_out_file, delimiter=',')
        temp = ErrorObservation()
        writer.writerow(temp.__dict__.keys())
        for error_observation in error_observations:
            writer.writerow(error_observation)

    print('Finished writing into observation csv file... \n')
    
print('Start...')
print('Please enter MS/POD name..')
ms_name = input()
error_txt_to_csv('document')
write_error_observations(generate_error_observations(get_error_log_from_csv(ms_name)), ms_name)
print('Finished...')


