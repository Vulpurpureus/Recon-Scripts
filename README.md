In the **passive** reconnaissance stage of a penetration test, this script is used when I'm not ready to scan the target directly but still want to determine which ports are open.

The script reads IP addresses from a file, displays detailed information about each one, separates the results for each IP address with an empty line, and writes the results to a CSV file.


## Usage:

1. Depending on what shell you are using, set your Shodan API key as an environment variable in the `~/.zshrc` or `~/.bashrc` file:
   
    ```bash
   export SHODAN_API_KEY="your_api_key_here"
   
3. Run the following command to apply the changes:
For Zsh:
```source ~/.zshrc # for Zsh```
OR for Bash: 
```source ~/.bashrc # for Bash```

5. Create a file of IP addresses named ```ips.txt```
6. Run the script:
```python3 shodan_search.py```
