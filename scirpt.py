from urllib.parse import urlparse
import os
import re
dom=input(("what's the web to scan "))
list=input(("what's the directory to use for subdomain ? "))
directory=input("what's the directory to use for directory ")
domain = urlparse(dom).netloc
mydomain = '.'.join(domain.split('.')[-2:])
#print(mydomain)
os.system(f"cd ~/Desktop && ffuf -u http://FUZZ.{mydomain} -w {list} > domain.txt")
os.system(f"cd ~/Desktop && ffuf -u http://www.{mydomain}/FUZZ -w {list} >> domain.txt")
def generate_domains(lines):
    domains = []
    for line in lines:
        match = re.search(r'2K(\w+)', line)
        if match:
            subdomain = match.group(1)
            domains.append(f'{subdomain}.' + mydomain)

    return domains
input_file_path = r'~/Desktop/domain.txt'
with open("domain.txt", 'r') as file:
    lines = file.readlines()

output_domains = generate_domains(lines)
print(output_domains)

with open('output.txt', 'a') as f:
    for domain in output_domains:
        f.write(domain + "\n")
os.system("cat ~/Desktop/output.txt | httprobe > file1.txt ")
os.system("cat ~/Desktop/file1.txt | aquatone >final.txt")