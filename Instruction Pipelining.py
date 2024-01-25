class Instruction:
    def __init__(self, opcode, operand):
        self.opcode = opcode
        self.operand = operand


class Pipeline:
    def __init__(self):
        self.fetch_stage = None
        self.decode_stage = None
        self.execute_stage = None
        self.memory_stage = None
        self.writeback_stage = None

    def fetch(self, opcode, operand):
        self.fetch_stage = Instruction(opcode, operand)

    def decode(self):
        self.decode_stage = self.fetch_stage

    def execute(self):
        self.execute_stage = self.decode_stage

    def memory(self):
        self.memory_stage = self.execute_stage

    def writeback(self):
        self.writeback_stage = self.memory_stage

    def display_pipeline(self):
        print("Pipeline stages:")
        print(f"Fetch Stage: {self.fetch_stage.opcode} {self.fetch_stage.operand}")
        print(f"Decode Stage: {self.decode_stage.opcode} {self.decode_stage.operand}")
        print(f"Execute Stage: {self.execute_stage.opcode} {self.execute_stage.operand}")
        print(f"Memory Stage: {self.memory_stage.opcode} {self.memory_stage.operand}")
        print(f"Writeback Stage: {self.writeback_stage.opcode} {self.writeback_stage.operand}")


# Example usage of the Pipeline class
pipeline = Pipeline()

print("Welcome to the Instruction Pipeline Simulator!")
print("Enter instructions in the format 'opcode operand'. Enter 'done' to finish.")

while True:
    user_input = input("Enter an instruction: ")

    if user_input == "done":
        break

    opcode, operand = user_input.split()

    pipeline.fetch(opcode, operand)
    pipeline.decode()
    pipeline.execute()
    pipeline.memory()
    pipeline.writeback()

# Displaying the pipeline stages after executing instructions
pipeline.display_pipeline()

# Additional instructions
pipeline.fetch("ADD", "R1, R2")
pipeline.decode()
pipeline.execute()
pipeline.memory()
pipeline.writeback()

pipeline.fetch("SUB", "R3, R4")
pipeline.decode()
pipeline.execute()
pipeline.memory()
pipeline.writeback()

# Displaying the pipeline stages after executing additional instructions
pipeline.display_pipeline()