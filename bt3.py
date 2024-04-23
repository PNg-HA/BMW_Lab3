import csv
import socket

def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.error:
        return "Resolution Failed"

def read_domains(input_filename):
    with open(input_filename, newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header if present
        return [row[0] for row in reader]

def write_results(output_filename, results):
    with open(output_filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Domain", "IP Address"])
        for domain, ip in results:
            writer.writerow([domain, ip])

def main():
    input_filename = 'bt1.csv'
    output_filename = 'bt3.csv'
    
    # Read domains from the input CSV file
    domains = read_domains(input_filename)
    
    # Resolve each domain to an IP
    results = [(domain, resolve_domain(domain)) for domain in domains]
    
    # Write the results to the output CSV file
    write_results(output_filename, results)
    print("DNS resolution completed. Results saved to", output_filename)

if __name__ == '__main__':
    main()
