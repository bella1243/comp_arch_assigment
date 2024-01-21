import random

def visualize_cache(cache):
    print("Cache Content:")
    for i, cache_set in enumerate(cache):
        print(f"Set {i}:", cache_set)
    print()

def is_hit(cache, word):
    for cache_set in cache:
        if cache_set and word in cache_set:
            return True
    return False

def replace_block(cache, word):
    set_index = random.randint(0, len(cache) - 1)
    block_index = random.randint(0, len(cache[set_index]) - 1)
    cache[set_index][block_index] = [f"Block {set_index}-{block_index} Word {i}" for i in range(4)]
    print(f"Cache set {set_index} block {block_index} replaced.")

def fetch_word(cache, word):
    if is_hit(cache, word):
        print(f"Cache hit! Word {word} is in the cache.")
    else:
        print(f"Cache miss! Fetching block containing word {word} from main memory.")
        replace_block(cache, word)

    visualize_cache(cache)
    print(f"Delivering word {word} to the processor register.\n")

def main():
    num_sets = 2  # Change this to adjust the number of sets
    set_size = 2  # Change this to adjust the set size
    main_memory = [[f"Main Memory Block {i} Word {j}" for j in range(4)] for i in range(6)]

    cache = [[None] * set_size for _ in range(num_sets)]

    for _ in range(5):  # Number of random word requests
        requested_word = random.choice(random.choice(main_memory))
        print(f"Processor requests word: {requested_word}")
        fetch_word(cache, requested_word)

if __name__ == "__main__":
    main()
