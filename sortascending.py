import os
import heapq

input_file = 'or4.txt'
output_file = 'sorted_or4.txt'

# Define chunk size (adjust according to your system's memory)
CHUNK_SIZE = 1000000  # e.g., 1 million integers per chunk


def sort_chunk(chunk):
    # Sorts a chunk in memory
    chunk.sort()
    return chunk


def merge_files(sorted_files):
    # Merges sorted chunks into a single sorted file
    with open(output_file, 'w') as out_file:
        heap = []

        # Open all sorted chunk files
        for file_name in sorted_files:
            file = open(file_name, 'r')
            number = int(file.readline().strip())
            heapq.heappush(heap, (number, file))

        # Merge chunks using heapq
        while heap:
            number, file = heapq.heappop(heap)
            out_file.write(str(number) + '\n')
            next_number = file.readline().strip()
            if next_number:
                heapq.heappush(heap, (int(next_number), file))
            else:
                file.close()
                os.remove(file.name)


# Read numbers from the input file and sort them in chunks
sorted_files = []
with open(input_file, 'r') as f:
    chunk = []
    file_count = 0
    for line in f:
        chunk.append(int(line.strip()))
        if len(chunk) == CHUNK_SIZE:
            chunk = sort_chunk(chunk)
            sorted_chunk_file = f'sorted_chunk_{file_count}.txt'
            with open(sorted_chunk_file, 'w') as chunk_file:
                chunk_file.write('\n'.join(map(str, chunk)))
            sorted_files.append(sorted_chunk_file)
            chunk = []
            file_count += 1

    # Sort the last chunk
    if chunk:
        chunk = sort_chunk(chunk)
        sorted_chunk_file = f'sorted_chunk_{file_count}.txt'
        with open(sorted_chunk_file, 'w') as chunk_file:
            chunk_file.write('\n'.join(map(str, chunk)))
        sorted_files.append(sorted_chunk_file)

# Merge sorted chunks into the final sorted file
merge_files(sorted_files)

print("Numbers have been sorted and written to", output_file)
