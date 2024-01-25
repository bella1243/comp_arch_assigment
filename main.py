import random
from collections import deque


class Cache:
    def __init__(self, cache_size, block_size, main_memory_size):
        self.cache_size = cache_size
        self.block_size = block_size
        self.main_memory_size = main_memory_size

        self.num_blocks_cache = cache_size // block_size
        self.num_blocks_memory = main_memory_size // block_size

        self.cache = [None] * self.num_blocks_cache
        self.main_memory = [None] * self.num_blocks_memory

        for i in range(self.num_blocks_memory):
            self.main_memory[i] = [f"Word {j}" for j in range(block_size)]

    def display_cache(self):
        print("Cache Content:")
        for i in range(self.num_blocks_cache):
            print(f"line {i}:", self.cache[i])
        print()

    def request_word(self, address):
        block_index = address // self.block_size % self.num_blocks_cache

        if self.cache[block_index] is not None:
            print(f"Cache Hit! Block {block_index} is in the cache.")
        else:
            print(f"Cache Miss! Block {block_index} is not in the cache.")
            self.load_block_to_cache(block_index)

        word_index = address % self.block_size
        print(f"Delivering Word: {self.cache[block_index][word_index]}")

    def load_block_to_cache(self, block_index):
        self.cache[block_index] = self.main_memory[block_index % self.num_blocks_memory].copy()

    def run_simulation(self):
        while True:
            self.display_cache()

            word_address = random.randint(0, self.main_memory_size - 1)
            print(f"Processor requests word at address {word_address}")

            self.request_word(word_address)

            user_input = input("Continue simulation? (y/n): ")
            if user_input.lower() != 'y':
                break


def main_direct_mapping():
    cache_size = int(input("enter the size of cache "))
    block_size = int(input("enter the size of block "))
    main_memory_size = int(input("enter the size of main memory  "))

    cache = Cache(cache_size, block_size, main_memory_size)

    cache.run_simulation()


class CacheAssociative:
    def __init__(self, cache_size, block_size, main_memory_size):
        self.cache_size = cache_size
        self.block_size = block_size
        self.main_memory_size = main_memory_size

        self.num_blocks_cache = cache_size // block_size
        self.num_blocks_memory = main_memory_size // block_size

        self.cache = [None] * self.num_blocks_cache
        self.main_memory = [None] * self.num_blocks_memory

        for i in range(self.num_blocks_memory):
            self.main_memory[i] = [f"Word {j}" for j in range(block_size)]

    def display_cache(self):
        print("Cache Content:")
        for i in range(self.num_blocks_cache):
            print(f"line {i}:", self.cache[i])
        print()

    def request_word(self, address):
        for i in range(self.num_blocks_cache):
            if self.cache[i] is not None and self.cache[i][0] == address // self.block_size:
                print(f"Cache Hit! Block {i} is in the cache.")
                # Deliver the word to the processor (in this case, just print it)
                word_index = address % self.block_size
                print(f"Delivering Word: {self.cache[i][1][word_index]}")
                return

        print(f"Cache Miss! The requested block is not in the cache.")
        self.load_block_to_cache(address)

    def load_block_to_cache(self, address):
        for i in range(self.num_blocks_cache):
            if self.cache[i] is None:
                self.cache[i] = [address // self.block_size, self.main_memory[address // self.block_size].copy()]
                return

        i = 0
        self.cache[i] = [address // self.block_size, self.main_memory[address // self.block_size].copy()]

    def run_simulation(self):
        while True:
            self.display_cache()

            word_address = random.randint(0, self.main_memory_size - 1)
            print(f"Processor requests word at address {word_address}")

            self.request_word(word_address)

            user_input = input("Continue simulation? (y/n): ")
            if user_input.lower() != 'y':
                break

    def load_block_to_cache(self, address):
        for i in range(self.num_blocks_cache):
            if self.cache[i] is None:
                self.cache[i] = [address // self.block_size, self.main_memory[address // self.block_size].copy()]
                return

        # If cache is full, ask the user to choose a replacement policy
        print("Cache is full. Choose a replacement policy:")
        print("1. Replace the first block")
        print("2. Replace the block with the least recently used (LRU)")
        choice = input("Select the replacement policy (1/2): ")

        # Use the chosen replacement policy
        if choice == '1':
            i = 0
        elif choice == '2':
            class CacheLRU:
                def __init__(self, cache_size, block_size, main_memory_size):
                    self.cache_size = cache_size
                    self.block_size = block_size
                    self.main_memory_size = main_memory_size

                    # Calculate the number of blocks in cache and main memory
                    self.num_blocks_cache = cache_size // block_size
                    self.num_blocks_memory = main_memory_size // block_size

                    # Initialize cache and main memory
                    self.cache = [None] * self.num_blocks_cache
                    self.main_memory = [None] * self.num_blocks_memory

                    # Initialize LRU tracking using a deque
                    self.lru_order = deque()

                    # Generate random content for main memory
                    for i in range(self.num_blocks_memory):
                        self.main_memory[i] = [f"Word {j}" for j in range(block_size)]

                def display_cache(self):
                    print("Cache Content:")
                    for i in range(self.num_blocks_cache):
                        print(f"Block {i}:", self.cache[i])
                    print()

                def request_word(self, address):
                    # Check if the requested block is in the cache (hit)
                    for i in range(self.num_blocks_cache):
                        if self.cache[i] is not None and self.cache[i][0] == address // self.block_size:
                            print(f"Cache Hit! Block {i} is in the cache.")
                            # Update LRU order
                            self.lru_order.remove(i)
                            self.lru_order.append(i)
                            # Deliver the word to the processor (in this case, just print it)
                            word_index = address % self.block_size
                            print(f"Delivering Word: {self.cache[i][1][word_index]}")
                            return

                    print(f"Cache Miss! The requested block is not in the cache.")
                    self.load_block_to_cache(address)

                def load_block_to_cache(self, address):
                    # Find an empty slot or use the LRU replacement policy
                    for i in range(self.num_blocks_cache):
                        if self.cache[i] is None:
                            self.cache[i] = [address // self.block_size,
                                             self.main_memory[address // self.block_size].copy()]
                            self.lru_order.append(i)
                            return

                    # Use LRU replacement policy
                    lru_block_index = self.lru_order.popleft()
                    self.cache[lru_block_index] = [address // self.block_size,
                                                   self.main_memory[address // self.block_size].copy()]
                    self.lru_order.append(lru_block_index)

            i = 0
        else:
            print("Invalid choice. Using default replacement policy (replace the first block).")

        self.cache[i] = [address // self.block_size, self.main_memory[address // self.block_size].copy()]


def main_associative_mapping():
    # Define cache parameters
    cache_size = int(input("enter the size of cache "))
    block_size = int(input("enter the size of block  "))
    main_memory_size = int(input("enter the size of memory "))

    cache = CacheAssociative(cache_size, block_size, main_memory_size)

    cache.run_simulation()


class CacheSetAssociative:
    def __init__(self, cache_size, block_size, main_memory_size, associativity):
        self.cache_size = cache_size
        self.block_size = block_size
        self.main_memory_size = main_memory_size
        self.associativity = associativity

        self.num_sets = cache_size // (block_size * associativity)
        self.blocks_per_set = associativity

        self.cache = [[None] * block_size for _ in range(self.cache_size)]
        self.main_memory = [None] * main_memory_size

        for i in range(main_memory_size):
            self.main_memory[i] = [f"Word {j}" for j in range(block_size)]

    def display_cache(self):
        print("Cache Content:")
        for set_index in range(self.num_sets):
            print(f"Set {set_index}:")
            for i in range(self.blocks_per_set):
                block_index = set_index * self.blocks_per_set + i
                print(f"  line {i}:", self.cache[block_index])
        print()

    def request_word(self, address):

        set_index = address // (self.block_size * self.associativity)

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

        for i in range(set_index * self.blocks_per_set, (set_index + 1) * self.blocks_per_set):
            if i < self.cache_size and self.cache[i] is None:
                self.cache[i] = [address // self.block_size, self.main_memory[address // self.block_size].copy()]
                return

        # Use a simple round-robin replacement policy
        self.cache[set_index * self.blocks_per_set] = [address // self.block_size,
                                                       self.main_memory[address // self.block_size].copy()]

        def load_block_to_cache(self, address, set_index):
            # Find an empty slot or use a replacement policy (round-robin in this case)
            global i
            for i in range(set_index * self.blocks_per_set, (set_index + 1) * self.blocks_per_set):
                if i < self.cache_size and self.cache[i] is None:
                    self.cache[i] = [address // self.block_size, self.main_memory[address // self.block_size].copy()]
                    return

            # If cache is full, ask the user to choose a replacement policy
            print("Cache is full. Choose a replacement policy:")
            print("1. Replace the first block in the set")
            print("2. Replace the block with the least recently used (LRU) in the set")
            choice = input("Select the replacement policy (1/2): ")

            if choice == '1':
                i = 0
            elif choice == '2':
                class CacheLRU:
                    def __init__(self, cache_size, block_size, main_memory_size):
                        self.cache_size = cache_size
                        self.block_size = block_size
                        self.main_memory_size = main_memory_size

                        # Calculate the number of blocks in cache and main memory
                        self.num_blocks_cache = cache_size // block_size
                        self.num_blocks_memory = main_memory_size // block_size

                        # Initialize cache and main memory
                        self.cache = [None] * self.num_blocks_cache
                        self.main_memory = [None] * self.num_blocks_memory

                        # Initialize LRU tracking using a deque
                        self.lru_order = deque()

                        # Generate random content for main memory
                        for i in range(self.num_blocks_memory):
                            self.main_memory[i] = [f"Word {j}" for j in range(block_size)]

                    def display_cache(self):
                        print("Cache Content:")
                        for i in range(self.num_blocks_cache):
                            print(f"Block {i}:", self.cache[i])
                        print()

                    def request_word(self, address):
                        # Check if the requested block is in the cache (hit)
                        for i in range(self.num_blocks_cache):
                            if self.cache[i] is not None and self.cache[i][0] == address // self.block_size:
                                print(f"Cache Hit! Block {i} is in the cache.")
                                # Update LRU order
                                self.lru_order.remove(i)
                                self.lru_order.append(i)
                                # Deliver the word to the processor (in this case, just print it)
                                word_index = address % self.block_size
                                print(f"Delivering Word: {self.cache[i][1][word_index]}")
                                return

                        print(f"Cache Miss! The requested block is not in the cache.")
                        self.load_block_to_cache(address)

                    def load_block_to_cache(self, address):
                        # Find an empty slot or use the LRU replacement policy
                        for i in range(self.num_blocks_cache):
                            if self.cache[i] is None:
                                self.cache[i] = [address // self.block_size,
                                                 self.main_memory[address // self.block_size].copy()]
                                self.lru_order.append(i)
                                return

                        # Use LRU replacement policy
                        lru_block_index = self.lru_order.popleft()
                        self.cache[lru_block_index] = [address // self.block_size,
                                                       self.main_memory[address // self.block_size].copy()]
                        self.lru_order.append(lru_block_index)

                i = 0
            else:
                print("Invalid choice. Using default replacement policy (replace the first block in the set).")

            self.cache[i] = [address // self.block_size, self.main_memory[address // self.block_size].copy()]

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


def main_set_associative_mapping():
    # Define cache parameters
    cache_size = int(input("enter the size of cache "))
    block_size = int(input("enter the size of block "))
    main_memory_size = int(input("enter the size of memory  "))
    associativity = int(input("enter the set associativity which is the power of 2  "))

    cache = CacheSetAssociative(cache_size, block_size, main_memory_size, associativity)

    cache.run_simulation()


def main():
    while True:
        print("==================================")

        print("Cache Mapping Techniques:")

        print("==================================")
        print("select cache mapping techniques")
        print("1. Associative  Mapping")
        print("2. Direct Mapping")
        print("3. Set Associative Mapping")
        choice = input("---> : ")

        if choice == '1':
            main_direct_mapping()
        elif choice == '2':
            main_associative_mapping()
        elif choice == '3':
            main_set_associative_mapping()
        else:
            print("Invalid choice. Please select again.")

        user_input = input("Do you want to simulate another mapping technique? (y/n): ")
        if user_input.lower() != 'y':
            break


if __name__ == "__main__":
    main()
