0x11. Python - Network #1
This repository contains Python scripts that demonstrate the use of networking-related concepts, focusing on fetching internet resources, making HTTP requests, handling responses, and interacting with web APIs.

Learning Objectives
By completing this project, you should be able to:

Fetch internet resources with the Python package urllib.
Decode urllib body response.
Use the Python package requests for making HTTP requests.
Make HTTP GET requests.
Make HTTP POST/PUT/etc. requests.
Fetch JSON resources.
Manipulate data from an external service.
Requirements
General
Allowed editors: vi, vim, emacs.
All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
All files should end with a new line.
The first line of all your files should be exactly #!/usr/bin/python3.
A README.md file at the root of the repo, containing a description of the repository.
Your code should use the pycodestyle (version 2.8.*).
All your files must be executable.
The length of your files will be tested using wc.
All your modules should have documentation (use python3 -c 'print(__import__("my_module").__doc__)').
You must use get to access dictionary values by key (it won’t throw an exception if the key doesn’t exist in the dictionary).
A documentation is not a simple word; it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified).
Your code should not be executed when imported (by using if __name__ == "__main__":).
Tasks
0. What's my status? #0
Write a Python script that fetches https://alx-intranet.hbtn.io/status.

You must use the urllib package.
You are not allowed to import any packages other than urllib.
The body of the response must be displayed in the following format:
plaintext
Copy code
Body response:
    - type: <class 'bytes'>
    - content: b'OK'
    - utf8 content: OK
1. Response header value #0
Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the X-Request-Id variable found in the header of the response.

You must use the packages urllib and sys.
You are not allowed to import packages other than urllib and sys.
The value of the X-Request-Id variable is different for each request.
2. POST an email #0
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8).

The email must be sent in the email variable.
You must use the packages urllib and sys.
You are not allowed to import packages other than urllib and sys.
3. Error code #0
Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions and print: Error code:, followed by the HTTP status code.
You must use the packages urllib and sys.
You are not allowed to import other packages than urllib and sys.
4. What's my status? #1
Write a Python script that fetches https://alx-intranet.hbtn.io/status.

You must use the requests package.
You are not allowed to import packages other than requests.
The body of the response must be displayed in the following format:
plaintext
Copy code
Body response:
    - type: <class 'str'>
    - content: OK
5. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header.

You must use the packages requests and sys.
You are not allowed to import other packages than requests and sys.
The value of this variable is different for each request.
6. POST an email #1
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

The email must be sent in the variable email.
You must use the packages requests and sys.
You are not allowed to import packages other than requests and sys.
7. Error code #1
Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response.

If the HTTP status code is greater than or equal to 400, print: Error code:, followed by the value of the HTTP status code.
You must use the packages requests and sys.
You are not allowed to import packages other than requests and sys.
8. Search API
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q.
If no argument is given, set q="".
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>.
Otherwise:
Display Not a valid JSON if the JSON is invalid.
Display No result if the JSON is empty.
You must use the packages requests and sys.
You are not allowed to import packages other than requests and sys.
9. My GitHub!
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.

You must use Basic Authentication with a personal access token as the password to access your information (only read:user permission is needed).
The first argument will be your username.
The second argument will be your password (in your case, a personal access token as the password).
You must use the packages requests and sys.
You are not allowed to import packages other than requests and sys.
You don’t need to check arguments passed to the script (number or type).
