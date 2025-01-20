import os
import re
import argparse
from collections import defaultdict

class InMemorySearchEngine:
    def __init__(self):
        self.index = defaultdict(list)

    def crawl_directory(self, dir_path):
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.txt'):
                    self.index_file(os.path.join(root, file))

    def index_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, start=1):
                words = re.findall(r'\w+', line.lower())
                for word in words:
                    self.index[word].append((file_path, line_num, line.strip()))

    def search(self, query):
        required, optional = self.parse_query(query)
        results = self.find_matches(required, optional)
        self.print_results(results)

    def parse_query(self, query):
        required = re.findall(r'\+\w+', query)
        optional = re.findall(r'\w+', query)
        required = [word[1:] for word in required]
        optional = [word for word in optional if word not in required]
        return required, optional

    def find_matches(self, required, optional):
        matches = defaultdict(int)
        for word in required:
            if word in self.index:
                for file_path, line_num, line in self.index[word]:
                    matches[(file_path, line_num, line)] += 1

        for word in optional:
            if word in self.index:
                for file_path, line_num, line in self.index[word]:
                    if (file_path, line_num, line) in matches:
                        matches[(file_path, line_num, line)] += 1

        sorted_matches = sorted(matches.items(), key=lambda item: item[1], reverse=True)
        return sorted_matches

    def print_results(self, results):
        for (file_path, line_num, line), score in results:
            print(f"{file_path} {line_num} \"{line}\"")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='In-Memory Search Engine')
    parser.add_argument('--dir', required=True, help='Directory to crawl')
    args = parser.parse_args()

    search_engine = InMemorySearchEngine()
    search_engine.crawl_directory(args.dir)

    print("Indexing complete. Enter your search queries:")
    while True:
        query = input("> ")
        search_engine.search(query)