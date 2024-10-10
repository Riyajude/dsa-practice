class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []         # To store repeat counts
        str_stack = []         # To store partial results
        current_str = ""       # Current decoded string
        num_str = ""           # Temporary string to store digits

        for char in s:
            if char.isdigit():
                num_str += char  # Collect digits as a string
            elif char == '[':
                num_stack.append(int(num_str))  # Convert collected digits to integer
                str_stack.append(current_str)   # Push the current string
                num_str = ""                    # Reset the number string
                current_str = ""                # Reset the current string
            elif char == ']':
                repeat_count = num_stack.pop()  # Get repeat count from stack
                current_str = str_stack.pop() + current_str * repeat_count  # Repeat the string
            else:
                current_str += char  # Build the current string

        return current_str  # Return the final decoded string
