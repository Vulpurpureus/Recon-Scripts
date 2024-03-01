In the **passive** reconnaissance stage of a penetration test, this script is used when I'm not ready to scan the target directly but still want to determine which ports are open.

The script reads IP addresses from a file, displays detailed information about each one, separates the results for each IP address with an empty line, and writes the results to a CSV file.


## Usage:

1. Depending on what shell you are using, set your Shodan API key as an environment variable in the `~/.zshrc` or `~/.bashrc` file:
    ```bash
    export SHODAN_API_KEY="your_api_key_here"
    ```

    If you're uncertain about which shell you're currently using, you can easily find out by executing the following command:
    ```bash
    echo $SHELL
    ```
   
2. Run the following command to apply the changes:

   For Zsh:
    ```bash
    source ~/.zshrc
    ```
   
   For Bash:
    ```bash
    source ~/.bashrc
    ```

4. Run the script:
    ```bash
    python3 shodan_search.py -l [ips_file.txt] -o [results_file.csv]
    ```


## Help

To display the help menu:
```bash
python3 shodan_search.py -h
```

Here are all the switches it supports:
```bash
optional arguments:
  -h, --help            show this help message and exit
  -l LIST, --list LIST  File containing list of IP addresses
  -o OUTPUT, --output OUTPUT Output CSV file name
```
