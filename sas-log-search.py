import os
import re
import time

current_dt = time.strftime('%Y-%m-%d_%H-%M-%S')
log_dir = '/some/dir/with/SAS/logs'
results_file = '/some/dir/to/write/results/results_{_dt}.txt'.format(_dt = current_dt)


issue_list = ['ERROR', 'WARNING', 'NOTE']
note_inclusion_list = ['initialized', 'Missing values']
warning_exclusion_list = ['Unable to copy SASUSER']


with open(results_file, 'w') as outfile:
    for fn in sorted(os.listdir(log_dir)):
        match = re.search('\w+\.log', fn)
        if os.path.isfile(os.path.join(log_dir, fn)) and match:
            outfile.write('%s\r\n' % fn)
            issue_flag = 0
            line_num = 0
            with open(os.path.join(log_dir, fn), 'r') as infile:
                try:
                    for line in infile:
                        line_num += 1
                        # if find ERROR, WARNING, or NOTE
                        if any(x in line for x in issue_list):
                            # only if NOTE includes values from note_inclusion_list
                            if ('NOTE' in line and not(any(x in line for x in note_inclusion_list))) or ('WARNING' in line and any(x in line for x in warning_exclusion_list)):
                                pass
                            else:
                                outfile.write('    line %d reads ==> %s\r\n' % (line_num, line))
                                issue_flag = 1
                finally:
                    if issue_flag == 0:
                        outfile.write('    no issues\r\n')
                    outfile.write('\r\n')
