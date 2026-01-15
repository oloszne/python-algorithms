from utils import open_test_file, close_test_file, get_line
from solve import sort_hotels_by_rating 

TEST_FILE = "test1.txt"  # e.g., "test1.txt" para debug local

def parse_input(source):
    line = get_line(source)
    n = int(line.strip())
    hotels = []
    
    for _ in range(n):
        line = get_line(source)
        name, rating, reviews = line.strip().split()
        rating_val = int(rating)
        reviews_val = int(reviews)
        hotels.append((name, rating_val, reviews_val))

    return hotels


inp = open_test_file(TEST_FILE)
hotels = parse_input(inp)

sorted_hotels = sort_hotels_by_rating(hotels)

names = [name for name, _, _ in sorted_hotels]
print("[" + ", ".join(names) + "]")

close_test_file(TEST_FILE, inp)
