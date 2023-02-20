from log_analysis import get_log_file_path_from_cmd_line,filter_log_by_regex
import pandas as pd  
import re

def main():
    log_file = get_log_file_path_from_cmd_line(1)
    #records=filter_log_by_regex(log_file,'SRC=(.*?) DST=(.*?) LEN=(.*?) ' ,print_summary=True, print_records=True)
    dpt_tally= tally_port_traffic(log_file)
    invalid_user=generate_invalid_user_report(log_file)
    ip_log=generate_source_ip_log(log_file, "220.195.35.40")

    for dpt,count in dpt_tally.items():
        if count > 100:
            generate_port_traffic_report(log_file,dpt)
    pass



# TODO: Step 8
def tally_port_traffic(log_file): 
    des_port_logs=filter_log_by_regex(log_file,'DPT=(.+?) ' )[1]
    dpt_tally={}
    for dpt_tuple in des_port_logs:
        dpt_num=dpt_tuple[0]
        dpt_tally[dpt_num]=dpt_tally.get(dpt_num,0)+1
    return dpt_tally

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    regex=r"^(.{6}) (.{8}).*SRC=(.+?) DST=(.+?) .*SPT=(.+?) DPT=(.+?) "
    
    captured_data=filter_log_by_regex(log_file,regex)[1]
    
    report_df=pd.DataFrame(captured_data)
    report_header=('Date','Time','Source IP Address','Destination IP address','Source Port','Destination Port')
    report_df.to_csv(f"destination_port_{port_number}_report.csv",index=False,header=report_header)
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    regex = r"(.{6}) (.{8}) .*user(.+) .*from(.+)"
    captured_data = filter_log_by_regex(log_file, regex)[1]
    report_df = pd.DataFrame(captured_data)
    report_df.to_csv('invalid_users.csv', index=False)
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    
    regex = r'Jan 29.*kernel:.*'+f'SRC=({ip_address})'+r'.*'
    captured_data  = filter_log_by_regex(log_file, regex)[0]
    report_df = pd.DataFrame(captured_data)
    ip_underscore = re.sub( '_', ip_address)
    report_df.to_csv(f"source_ip_{ip_underscore}.log", index=False)
    
    return 

if __name__ == '__main__':
    main()