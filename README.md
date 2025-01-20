This project implements an in-memory search engine in Python. It crawls through a specified directory, indexes text files, and allows users to search for specific terms within those files. The search engine supports complex queries with required and optional terms, and returns results sorted by relevance.

Features:
1. Directory Crawling: Recursively reads .txt files from the specified directory.
2. In-Memory Indexing: Builds an efficient in-memory index of words from the text files.
3. Complex Queries: Supports queries with required (+term) and optional terms, including logical OR groups.
4. Relevance Sorting: Results are sorted by the number of matching terms.
