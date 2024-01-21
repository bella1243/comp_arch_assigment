import random


class Cache:
    def __init__(self, size):
        self.size = size
        self.cache = [None] * size

    def visualize_cache(self):
        print("Cache Content:")
        for i, block in enumerate(self.cache):
            print(f"Set {i}:", block)
        print()

    def is_hit(self, word):
        for block in self.cache:
            if block and word in block:
                return True
        return False

    def replace_block(self, word):
        # In this simple example, we use a random replacement strategy
        index = random.randint(0, self.size - 1)
        self.cache[index] = [f"Block {index} Word {i}" for i in range(4)]  # Simulating a block of words
        print(f"Cache block {index} replaced.")

    def fetch_word(self, word):
        if self.is_hit(word):
            print(f"Cache hit! Word {word} is in the cache.")
        else:
            print(f"Cache miss! Fetching block containing word {word} from main memory.")
            self.replace_block(word)

        self.visualize_cache()
        print(f"Delivering word {word} to the processor register.\n")


def main():
    cache_size = 2  # Change this to adjust the cache size
    main_memory = [[f"Main Memory Block {i} Word {j}" for j in range(4)] for i in range(6)]

    cache = Cache(cache_size)

    for _ in range(5):  # Number of random word requests
        requested_word = random.choice(random.choice(main_memory))
        print(f"Processor requests word: {requested_word}")
        cache.fetch_word(requested_word)


if __name__ == "__main__":
    main()
