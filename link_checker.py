import csv
import os

import requests

def link_checker(file):
    """Iterate over a list of of URLS and return their status codes
    Args:
        - files (string): the path of the file we're scanning
    """
    
    csv_rows = []
    with open(file) as f:
        # read the data from the csv
        reader = csv.reader(f)
        
        for row in reader:
            if reader.line_num == 1:
                # skip the first row
                continue  
              
            # url = row[10]
            url = row[8]
            print(f"link_checker: Checking link: {url}")
            
            try:
                r = requests.get(url)
            except print(0):
                pass
            
            csv_rows.append([r.status_code, url])
            print(r.status_code)
            
    # Write out the csv file
    with open(os.path.join(os.getcwd(), 'files', 'results.csv'), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in csv_rows:
            writer.writerow(row)
            

link_checker("./files/PublicationsNew.csv")
