import sys
import os
import re

# TODO: Step 3
def get_log_file_path_from_cmd_line(total_param):
    """gets the full path of a log file from the command line

    Args:
        total_param (int): Parameter number 

    Returns:
        str: full path of  the log file
    """
    total_param= len(sys.argv)-1
    if total_param>=total_param:
        log_file_path=sys.argv[1]
        if os.path.isfile(log_file_path):
            return os.path.abspath(log_file_path)
        else:
            print(f"Error: Log file does not exist.")
            sys.exit(1)
    else:
        print(f"Error: Missing log file.")
        sys.exit(1)


def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex.

    Args:
        log_file (str): Path of the log file
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.

    Returns:
        (list, list): List of records that match regex, List of tuples of captured data
    """

    records=[]
    captured_data=[]

    regex_flags=re.IGNORECASE if ignore_case else 0
    with open(log_file,'r') as file:
        for line in file:
            match=re.search(regex,line,regex_flags)
            if match:
                records.append(line)
                if match.lastindex:
                    captured_data.append(match.groups())

    if print_records is True:
        print(*records, sep='')
        
    if print_summary is True:
            print(f'The log file contains {len(records)} records that case-{"in" if ignore_case else""}sensitive match the regex "{regex}".')


    
    return records,captured_data