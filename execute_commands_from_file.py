ss# Global variable to keep track of orders
orders = {}

# Define the functions as described in the file
def createOrder(order_id, time, amount, priority):
    orders[order_id] = {'time': time, 'amount': amount, 'priority': priority}
    with open(output_file_path, 'a') as f:
        f.write(f"Creating order {order_id} at time {time} with amount {amount} and priority {priority}\n")

def getRankOfOrder(order_id):
    # Simplified example, implement your own logic
    with open(output_file_path, 'a') as f:
        f.write(f"Getting rank of order {order_id}\n")

def cancelOrder(order_id, time):
    if order_id in orders:
        del orders[order_id]
    with open(output_file_path, 'a') as f:
        f.write(f"Cancelling order {order_id} at time {time}\n")

def updateTime(order_id, new_time, priority):
    if order_id in orders:
        orders[order_id]['time'] = new_time
        orders[order_id]['priority'] = priority
    with open(output_file_path, 'a') as f:
        f.write(f"Updating time of order {order_id} to {new_time} with priority {priority}\n")

def custom_print(arg1, arg2):
    with open(output_file_path, 'a') as f:
        f.write(f"Custom Print called with arguments {arg1} and {arg2}\n")

def Quit():
    with open(output_file_path, 'a') as f:
        for order_id, details in orders.items():
            f.write(f"Delivery details of order {order_id}: Time {details['time']}, Amount {details['amount']}, Priority {details['priority']}\n")
        f.write("Quitting the program\n")
    exit(0)
def log(message):
    """Writes a message to the output file."""
    with open(output_file_path, 'a') as f:
        f.write(message + "\n")


# Main function to read and execute commands from the file
def execute_commands_from_file(file_path):
    """Reads and executes commands from the specified file."""
    global output_file_path
    output_file_name = file_path.rsplit('.', 1)[0] + "_output_file.txt"
    output_file_path = output_file_name

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if '(' in line:
                parts = line.split('(')
                func_name = parts[0]
                args_str = parts[1].rstrip(')')
                # Ensure args is always a tuple, even for a single argument
                if ',' in args_str or not args_str.isdigit():
                    args = eval(f"({args_str})")
                else:
                    args = (eval(args_str),)
            else:
                func_name = line
                args = ()
            
            if func_name in globals():
                globals()[func_name](*args)
            else:
                log(f"No function found for {func_name}")


# Assuming the filepath to your file
file_path = "C:\\Users\\yasha\\Desktop\\ads project\\test1.txt"

# Global variable for the output file path
output_file_path = "C:\\Users\\yasha\\Desktop\\ads project\\test1_output_file.txt"

# Execute commands from the specified file
execute_commands_from_file(file_path)



