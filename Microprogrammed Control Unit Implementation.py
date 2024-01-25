class Processor:
    def __init__(self, implementation_type, num_registers, num_alu_functions, instruction):
        self.implementation_type = implementation_type  # Store the implementation type (Vertical or Horizontal)
        self.num_registers = num_registers  # Store the number of registers
        self.num_alu_functions = num_alu_functions  # Store the number of supported ALU functions
        self.instruction = instruction  # Store the instruction to execute
        self.num_buses = 3  # Default 3-bus organization

        self.microoperations = []  # List to store the sequence of microoperations
        self.control_word = ""  # String to store the final control word

    def set_num_buses(self, num_buses):
        self.num_buses = num_buses  # Set the number of buses chosen by the user

    def execute_instruction(self):
        for i in range(len(self.instruction)):
            microop = f"Microop {i+1}: {self.instruction[i]}"  # Generate each microoperation for the given instruction
            self.microoperations.append(microop)  # Add the microoperation to the list

        for microop in self.microoperations:
            self.control_word += "1" * len(microop) + "0"  # Generate the control word based on the microoperations

    def display_microoperations(self):
        print("Sequence of Microoperations:")
        for microop in self.microoperations:
            print(microop)  # Display each microoperation in the sequence

    def display_control_word(self):
        print("Control Word:")
        print(self.control_word)  # Display the final control word


def vertical_implementation():
    num_registers = int(input("Enter the number of registers: "))  # Prompt the user to enter the number of registers
    num_alu_functions = int(input("Enter the number of supported ALU functions: "))  # Prompt for the number of ALU functions
    instruction = input("Enter an instruction to execute: ")  # Prompt the user to enter the instruction

    processor = Processor("Vertical", num_registers, num_alu_functions, instruction)  # Create a Processor object with vertical implementation

    num_buses_choice = int(input("Select the number of buses (1, 2, or 3): "))  # Prompt for the number of buses
    processor.set_num_buses(num_buses_choice)  # Set the number of buses chosen by the user

    processor.execute_instruction()  # Execute the instruction and generate microoperations and control word

    processor.display_microoperations()  # Display the sequence of microoperations
    processor.display_control_word()  # Display the final control word
    processor.execute_instruction(num_buses_choice)


def horizontal_implementation():
    num_registers = int(input("Enter the number of registers: "))  # Prompt the user to enter the number of registers
    num_alu_functions = int(input("Enter the number of supported ALU functions: "))  # Prompt for the number of ALU functions
    instruction = input("Enter an instruction to execute: ")  # Prompt the user to enter the instruction

    processor = Processor("Horizontal", num_registers, num_alu_functions, instruction)  # Create a Processor object with horizontal implementation

    num_buses_choice = int(input("Select the number of buses (1, 2, or 3): "))  # Prompt for the number of buses
    processor.set_num_buses(num_buses_choice)  # Set the number of buses chosen by the user

    processor.execute_instruction()  # Execute the instruction and generate microoperations and control word

    processor.display_microoperations()  # Display the sequence of microoperations
    processor.display_control_word()  # Display the final control word


while True:
    print("Welcome to the Microprogrammed Control Simulator!")
    print("1. Vertical Implementation")
    print("2. Horizontal Implementation")
    print("3. Exit")

    choice = int(input("Enter your choice: "))  # Prompt the user to select an option

    if choice == 1:
        vertical_implementation()  # Call the function for vertical implementation
    elif choice == 2:
        horizontal_implementation()  # Call the function for horizontal implementation
    elif choice == 3:
        print("Thank you for using the program. Goodbye!")
        break  # Exit the program loop
    else:
        print("Invalid choice. Please try again.")  # Display an error message for an invalid choice1