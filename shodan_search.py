import shodan
import csv
import os

# ANSI escape code for red text
RED = "\033[1m\033[91m"  # Bold + Red
ENDC = "\033[0m"  # Reset to default color

# Initialize the Shodan API with your provided API key
api_key = os.getenv('SHODAN_API_KEY')
if not api_key:
    raise EnvironmentError("SHODAN_API_KEY environment variable not set.")

api = shodan.Shodan(api_key)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Shodan Search Script')
parser.add_argument('-l', '--list', required=True, help='File containing list of IP addresses')
parser.add_argument('-o', '--output', required=True, help='Output CSV file name')
args = parser.parse_args()


# Path to the file containing IP addresses
file_path = args.list

# Path to the output CSV file
output_csv_path = args.output

# Function to write data to CSV
def write_to_csv(ip, info, csvwriter):
    for item in info['data']:
        port = item['port']
        service = item.get('product', 'n/a')
        version = item.get('version', 'n/a')
        item_os = item.get('os', 'n/a')
        csvwriter.writerow([ip, info.get('org', 'n/a'), info.get('os', 'n/a'), port, service, version, item_os])

# Prepare CSV file for writing
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Writing headers to the CSV file
    headers = ['IP', 'Organization', 'Operating System', 'Port', 'Service', 'Version', 'OS']
    csvwriter.writerow(headers)

    # Read IP addresses from the file and process
    with open(file_path, 'r') as file:
        ip_addresses = [line.strip() for line in file if line.strip()]

    for ip in ip_addresses:
        try:
            # Get information for each IP address
            info = api.host(ip)

            # Display the IP address and other information
            print(f"{RED}IP:{ENDC} {info['ip_str']}")
            print(f"{RED}Organization:{ENDC} {info.get('org', 'n/a')}")
            print(f"{RED}Operating System:{ENDC} {info.get('os', 'n/a')}")

            # Display open ports and associated service information
            print(f"{RED}Open Ports and Services:{ENDC}")
            for item in info['data']:
                port_info = f"{RED}Port:{ENDC} {item['port']}"
                if 'product' in item:
                    port_info += f", {RED}Service:{ENDC} {item['product']}"
                if 'version' in item:
                    port_info += f", {RED}Version:{ENDC} {item['version']}"
                if 'os' in item:
                    port_info += f", {RED}OS:{ENDC} {item['os']}"
                print(port_info)

            print("\n")  # Separate each IP result with an empty line

            # Write to CSV
            write_to_csv(ip, info, csvwriter)

        except shodan.APIError as e:
            print(f"Error for IP {ip}: {e}")

# This script reads IP addresses from a file, displays detailed information about each one,
# separates the results for each IP address with an empty line, and writes the results to a CSV file.
