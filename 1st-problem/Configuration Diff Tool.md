Objective
Given two configuration strings, config1 and config2, each containing multiple lines of key-value pairs in the format key=value, write a function to compare these configurations.
Your task is to identify which keys have been added, removed, or modified from config1 to config2. The function should return a dictionary with three keys: added, removed, and modified.

added: A list of key-value pairs that are present in config2 but not in config1.
removed: A list of key-value pairs that are present in config1 but not in config2.
modified: A list of dictionaries, each containing the old key-value pair from config1 and the new key-value pair from config2 for keys that exist in both configurations but have different values.

So, this problem is about comparing two configuration strings that contain key-value pairs. You know how configuration files often have settings like "hostname=server1" or "timeout=30", right? 
You're being asked to identify what changes occurred between two versions of these configurations.


Let's break down what you need to do:
First, you'll parse these configuration strings. Each string has multiple lines, with each line having a key-value pair separated by an equals sign. The '\n' character separates different lines.
Then, you need to compare the two sets of configurations and categorize the differences:


If a key exists in config2 but not in config1, it's been "added"
If a key exists in config1 but not in config2, it's been "removed"
If a key exists in both, but the values are different, it's been "modified"


For example, in the sample input, you have:
config1: "host=localhost\nport=8080\ndb=mysql"
config2: "host=localhost\nport=9000\ndb=mysql"


Breaking this down:
"host=localhost" is in both configs with the same value
"port" is in both configs, but in config1 it's "port=8080" and in config2 it's "port=9000", so it's modified
"db=mysql" is in both configs with the same value


So the output shows no additions or removals, but one modification where "port=8080" changed to "port=9000"
Your task is to write a function that performs this comparison and returns the results in the specific dictionary format shown.
The tricky part might be parsing the strings correctly and then organizing the changes into the right categories.

diagram

Code
def compare_configs(config1: str, config2: str) -> dict:
    lines1 = config1.strip().split('\n')
    lines2 = config2.strip().split('\n')
    # Initialize results
    diff = {
        'added': [],
        'removed': [],
        'modified': []
    }
    # Your code here
    
    return diff
Additional information
Input Format:

config1 and config2 are non-empty strings containing multiple lines.
Each line in the strings follows the format key=value without any additional spaces.
Output Format:

A dictionary with three keys: added, removed, and modified.
added and removed contain lists of strings representing the key-value pairs.
modified contains a list of dictionaries, each with old and new keys representing the changes.
Constraints:

The number of lines in each configuration string does not exceed 10⁴.
Keys consist of alphanumeric characters and are case-sensitive.
Values can be any string without newline characters.
Clarifications:

If a key exists in both configurations with the same value, it is not included in any of the added, removed, or modified lists.
The order of key-value pairs in the output lists does not matter.
Examples
Example 1:
Input: host=localhost\nport=8080\ndb=mysql, host=localhost\nport=9000\ndb=mysql
Output: {"added":[],"modified":[{"new":"port=9000","old":"port=8080"}],"removed":[]}
Example 2:
Input: host=localhost\nport=8080, host=localhost\nport=8080\ndb=mysql
Output: {"added":["db=mysql"],"modified":[],"removed":[]}
Example 3:
Input: host=localhost\nport=8080\ndb=mysql, host=127.0.0.1\nport=8080
Output: {"added":[],"modified":[{"new":"host=127.0.0.1","old":"host=localhost"}],"removed":["db=mysql"]}
