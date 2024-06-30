# MDRI-FILES
a flexible and powerful way to handle a wide variety of inputs, automatically formatting them into machine-dialogue-readable-input.
To create a new file extension for the diverse set of uses you described, we'll define a format that adheres to the MDRI specification. Let's call this new file extension `.mdri`.

### Example `.mdri` File

```
<SECTION>
** 
|*| Initialize variables 
|_|
    var x = 10;
    var y = 20;
** 

|*| Perform addition 
|_|
    var sum = x + y;
** 

|*| Output the result 
|_| 
    |=| "The sum of x and y is: " + sum;
** 

|+| Simulate variable changes 
|_|
    x = 15;
    y = 25;
** 

|(<::>^<::>)| Perform context-aware action 
|_|
    var difference = x - y;
    |=| "The difference between x and y is: " + difference;
** 

|-| Request user input 
|_|
    var userInput = prompt("Enter a value:");
    |=| "You entered: " + userInput;
** 

<END SECTION>
```

### Key Components of the `.mdri` File

- **`<SECTION>`**: Marks the beginning of a section.
- **`</SECTION>`**: Marks the end of a section.
- **`**`**: Begins and ends a block.
- **`|*|`**: Denotes an action.
- **`|_|`**: Denotes statements.
- **`|-|`**: Denotes requests.
- **`|(<::>^<::>)|`**: Denotes an AOT scan for context.
- **`| |`**: Denotes tasks.
- **`|+|`**: Denotes simulation.
- **`|=|`**: Denotes print.
- **`|^|`**: Denotes pass.
- **`|#|`**: Denotes placeholders.

### Automatic Reformatting and Execution Logic

To automatically reformat the input into MDRI, correct errors, compile on the fly, interpret JIT-style, and execute immediately, a processing engine will be required. This engine will read the `.mdri` file, parse its contents, perform the necessary transformations, and then execute the code.

### Example Python Script for Processing `.mdri` Files

Here's a simplified example of how you might implement a Python script to process `.mdri` files:

```python
import re

def parse_mdri(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    sections = re.findall(r'<SECTION>(.*?)</SECTION>', content, re.DOTALL)
    for section in sections:
        process_section(section)

def process_section(section):
    blocks = re.findall(r'\*\*(.*?)\*\*', section, re.DOTALL)
    for block in blocks:
        lines = block.strip().split('\n')
        action_type = lines[0].strip()

        if action_type.startswith('|*|'):
            process_action(lines[1:])
        elif action_type.startswith('|_|'):
            process_statements(lines[1:])
        elif action_type.startswith('|-|'):
            process_request(lines[1:])
        elif action_type.startswith('|(<::>^<::>)|'):
            process_aot_scan(lines[1:])
        elif action_type.startswith('|+|'):
            process_simulation(lines[1:])
        # Add more cases as needed

def process_action(lines):
    for line in lines:
        exec(line.strip())

def process_statements(lines):
    for line in lines:
        exec(line.strip())

def process_request(lines):
    for line in lines:
        exec(line.strip())

def process_aot_scan(lines):
    for line in lines:
        exec(line.strip())

def process_simulation(lines):
    for line in lines:
        exec(line.strip())

# Example usage
parse_mdri('example.mdri')
```

This script demonstrates how to parse a `.mdri` file and process each block according to its type. You would need to expand this script to handle error correction, context-aware processing, and other requirements specified by the MDRI format.

### Conclusion

The `.mdri` file extension provides a flexible and powerful way to handle a wide variety of inputs, automatically formatting them into machin-dialogue-readable-input. 
