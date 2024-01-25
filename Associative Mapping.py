import random

class Cache:
    def __init__(self, size, block_size):
        self.size = size
        self.block_size = block_size
        self.cache = [None] * size

    def visualize_cache(self):
        print("Cache Content:")
        for i, block in enumerate(self.cache):
            print(f"Block {i}: {block}")
        print()

    def generate_memory(self, memory_size):
        return [random.randint(0, 100) for _ in range(memory_size)]

    def access_memory(self, address):
        block_index = address // self.block_size
        block_offset = address % self.block_size

        if self.cache[block_index] is not None:
            print(f"Cache Hit! Block {block_index} is already in the cache.")
            data = self.cache[block_index][block_offset]
        else:
            print(f"Cache Miss! Loading Block {block_index} into the cache.")
            self.cache[block_index] = self.memory[block_index * self.block_size: (block_index + 1) * self.block_size]
            data = self.cache[block_index][block_offset]

        return data

    def fetch_word(self, processor_address):
        word = self.access_memory(processor_address)
        print(f"Processor Register: {word}\n")

if __name__ == "__main__":
    cache_size = 4
    block_size = 4
    memory_size = 16

    cache = Cache(cache_size, block_size)
    cache.memory = cache.generate_memory(memory_size)

    # Example Accesses
    cache.fetch_word(5)
    cache.visualize_cache()

    cache.fetch_word(8)
    cache.visualize_cache()

    cache.fetch_word(2)
    cache.visualize_cache()

    cache.fetch_word(12)
    cache.visualize_cache()
