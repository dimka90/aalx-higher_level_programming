Project 0x10 - Python - Network #0
Description
This project focuses on learning and understanding networking concepts and tools in Python and Bash scripting. It covers topics such as HTTP, cURL, and network requests.

Learning Objectives
Upon completion of this project, you should be able to:

Understand what a URL is and how to read it.
Have a solid understanding of HTTP (HyperText Transfer Protocol).
Know how to define various components in a URL, such as the scheme, domain name, sub-domain, port number, and query string.
Understand what an HTTP request and response are, including their components like headers and the message body.
Recognize HTTP request methods and response status codes.
Learn about HTTP Cookies and their role in web communication.
Know how to make requests using cURL and understand what happens when a URL is entered in a web browser.
Requirements
All scripts should be written in Bash and Python.
Scripts will be tested on Ubuntu 20.04 LTS.
Bash scripts should be exactly 3 lines long, ending with a new line, and executable.
Python scripts should use #!/usr/bin/python3 as the shebang.
Code should adhere to PEP8 style using pycodestyle.
All modules, classes, and functions should be documented.
Plagiarism is strictly forbidden.
Scripts Overview
0-body_size.sh
Usage: ./0-body_size.sh <URL>
Displays the size of the response body in bytes using cURL.
Example:
bash
Copy code
./0-body_size.sh 0.0.0.0:5000
# Output: 10
1-body.sh
Usage: ./1-body.sh <URL>
Displays the body of the response for a URL, but only for a 200 status code.
Example:
bash
Copy code
./1-body.sh 0.0.0.0:5000/route_1
# Output: Route 2
2-delete.sh
Usage: ./2-delete.sh <URL>
Sends a DELETE request to the URL and displays the body of the response.
Example:
bash
Copy code
./2-delete.sh 0.0.0.0:5000/route_3
# Output: I'm a DELETE request
3-methods.sh
Usage: ./3-methods.sh <URL>
Displays all HTTP methods the server will accept for a given URL.
Example:
bash
Copy code
./3-methods.sh 0.0.0.0:5000/route_4
# Output: OPTIONS, HEAD, PUT
4-header.sh
Usage: ./4-header.sh <URL>
Sends a GET request to the URL with a specific header and displays the body of the response.
Example:
bash
Copy code
./4-header.sh 0.0.0.0:5000/route_5
# Output: Hello School!
5-post_params.sh
Usage: ./5-post_params.sh <URL>
Sends a POST request to the URL with specific parameters and displays the body of the response.
Example:
bash
Copy code
./5-post_params.sh 0.0.0.0:5000/route_6
# Output: POST params: email: test@gmail.com, subject: I will always be here for PLD
6-peak.py
Finds a peak in a list of unsorted integers using a specified algorithm.
Prototype: def find_peak(list_of_integers).
Complexity of the algorithm: O(log(n)), O(n), O(nlog(n)), or O(n2).
Example:
python
Copy code
print(find_peak([1, 2, 4, 6, 3]))  # Output: 6
print(find_peak([4, 2, 1, 2, 3, 1]))  # Output: 3
print(find_peak([2, 2, 2]))  # Output: 2
print(find_peak([]))  # Output: None
print(find_peak([-2, -4, 2, 1]))  # Output: 2
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4
Conclusion
This project provides a solid foundation for understanding network protocols, HTTP, and the usage of cURL in both Bash and Python scripting. Completing the tasks will enhance your skills in making HTTP requests, handling responses, and working with different methods and headers.
