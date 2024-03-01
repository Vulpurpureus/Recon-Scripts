In the **passive** reconnaissance stage of a penetration test, this script is used when I'm not ready to scan the target directly but still want to determine which ports are open.

The script reads IP addresses from a file, displays detailed information about each one, separates the results for each IP address with an empty line, and writes the results to a CSV file.

Instructions:
1. Depending on what shell you are using, set your Shodan API key as an enviornment variable in in the ~/.zshrc or ~/.bashrc file:
export SHODAN_API_KEY="your_api_key_here"
2. Run source ~/.zshrc or source ~/.bashrc
3. Create a file of IP addresses names ips.txt
4. Run python3 shodan_search.py
   
