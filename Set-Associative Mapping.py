import random

class Cache:
    def __init__(self, cache_size, block_size, main_memory_size, associativity):
        self.cache_size = cache_size
        self.block_size = block_size
        self.main_memory_size = main_memory_size
        self.associativity = associativity

        # Calculate the number of sets and blocks per set
        self.num_sets = cache_size // (block_size * associativity)
        self.blocks_per_set = associativity

        # Initialize cache and main memory
        self.cache = [[None] * block_size for _ in range(self.cache_size)]
        self.main_memory = [None] * main_memory_size

        # Generate random content for main memory
        for i in range(main_memory_size):
            self.main_memory[i] = [f"Word {j}" for j in range(block_size)]

    def display_cache(self):
        print("Cache Content:")
        for set_index in range(self.num_sets):
            print(f"Set {set_index}:")
            for i in range(self.blocks_per_set):
                block_index = set_index * self.blocks_per_set + i
                print(f"  Block {i}:", self.cache[block_index])
        print()

    def request_word(self, address):
        # Calculate set index in cache
        set_index = address // (self.block_size * self.associativity)

        # Check if the requested block is in the cache (hit)
        for i in range(set_index * self.blocks_per_set, (set_index + 1) * self.blocks_per_set):
            if i < self.cache_size and self.cache[i] is not None and self.cache[i][0] == address // self.block_size:
                print(f"Cache Hit! Set {set_index}, Block {i % self.blocks_per_set} is in the cache.")
                # Deliver the word to the processor (in this case, just print it)
                word_index = address % self.block_size
                print(f"Delivering Word: {self.cache[i][1][word_index]}")
                return

        print(f"Cache Miss! Set {set_index} is not in the cache.")
        self.load_block_to_cache(address, set_index)

    def load_block_to_cache(self, address, set_index):
        # Find an empty slot or use a replacement policy (round-robin in this case)
        for i in range(set_index * self.blocks_per_set, (set_index + 1) * self.blocks_per_set):
            if i < self.cache_size and self.cache[i] is None:
                self.cache[i] = [address // self.block_size, self.main_memory[address // self.block_size].copy()]
                return

        # Use a simple round-robin replacement policy
        self.cache[set_index * self.blocks_per_set] = [address // self.block_size,
                                                       self.main_memory[address // self.block_size].copy()]

    def run_simulation(self):
        while True:
            self.display_cache()

            # Get a random word address requested by the processor
            word_address = random.randint(0, self.main_memory_size - 1)
            print(f"Processor requests word at address {word_address}")

            # Simulate the cache operation for the requested word
            self.request_word(word_address)

            # Ask the user if they want to continue or exit
            user_input = input("Continue simulation? (y/n): ")
            if user_input.lower() != 'y':
                break


def main():
    # Define cache parameters
    cache_size = 16  # Size of the cache in words
    block_size = 4   # Size of a block in words
    main_memory_size = 32  # Size of main memory in words
    associativity = 2  # Set associativity

    # Create a cache object
    cache = Cache(cache_size, block_size, main_memory_size, associativity)

    # Run the cache simulation
    cache.run_simulation()


if __name__ == "__main__":
    main()
