import random

class SetAssociativeCache:
    def __init__(self, num_sets, set_size):
        self.num_sets = num_sets
        self.set_size = set_size
        self.cache = [[None] * set_size for _ in range(num_sets)]

    def visualize_cache(self):
        print("Cache Content:")
        for i, cache_set in enumerate(self.cache):
            print(f"Set {i}:", cache_set)
        print()

    def is_hit(self, word):
        for cache_set in self.cache:
            if cache_set and word in cache_set:
                return True
        return False

    def replace_block(self, word):
        # In this simple example, we use a random replacement strategy within the selected set
        set_index = random.randint(0, self.num_sets - 1)
        block_index = random.randint(0, self.set_size - 1)
        self.cache[set_index][block_index] = [f"Block {set_index}-{block_index} Word {i}" for i in range(4)]
        print(f"Cache set {set_index} block {block_index} replaced.")

    def fetch_word(self, word):
        if self.is_hit(word):
            print(f"Cache hit! Word {word} is in the cache.")
        else:
            print(f"Cache miss! Fetching block containing word {word} from main memory.")
            self.replace_block(word)

        self.visualize_cache()
        print(f"Delivering word {word} to the processor register.\n")

def main():
    num_sets = 2  # Change this to adjust the number of sets
    set_size = 2  # Change this to adjust the set size
    main_memory = [[f"Main Memory Block {i} Word {j}" for j in range(4)] for i in range(6)]

    cache = SetAssociativeCache(num_sets, set_size)

    for _ in range(5):  # Number of random word requests
        requested_word = random.choice(random.choice(main_memory))
        print(f"Processor requests word: {requested_word}")
        cache.fetch_word(requested_word)

if __name__ == "__main__":
    main()
