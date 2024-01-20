import random

def visualize_cache(cache):
    print("Cache Content:")
    for i, block in enumerate(cache):
        print(f"Block {i}: {block}")
    print()

def fetch_word(cache, main_memory, address, cache_size, block_size):
    block_number, word_offset = divmod(address, block_size)
    block_index = block_number % cache_size

    if cache[block_index] is not None and cache[block_index]['block_number'] == block_number:
        print(f"Cache Hit! Word at address {address} is {cache[block_index]['data'][word_offset]}")
    else:
        print(f"Cache Miss! Fetching block {block_number} from main memory.")
        cache[block_index] = {
            'block_number': block_number,
            'data': [random.randint(1, 100) for _ in range(block_size)]
        }
        print(f"Fetched block {block_number} into cache. Word at address {address} is {cache[block_index]['data'][word_offset]}")

def main():
    cache_size = int(input("Enter the cache size: "))
    block_size = int(input("Enter the block size: "))
    main_memory_size = int(input("Enter the main memory size: "))

    cache = [None] * cache_size

    # Fill main memory with random data
    main_memory = [
        [random.randint(1, 100) for _ in range(block_size)] for _ in range(main_memory_size)
    ]

    while True:
        visualize_cache(cache)
        address = int(input(f"Enter the memory address to access (0-{main_memory_size * block_size - 1}), or -1 to exit: "))

        if address == -1:
            break

        if 0 <= address < main_memory_size * block_size:
            fetch_word(cache, main_memory, address, cache_size, block_size)
        else:
            print("Invalid memory address. Please enter a valid address.")

if __name__ == "__main__":
    main()
