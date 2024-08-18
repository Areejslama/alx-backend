#!/usr/bin/env python3
"""this script define a function"""
import csv
import math
from typing import List, Tuple, Any


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Calculate start and end indices for pagination
        """
        start = (page - 1) * page_size
        end = start + page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data from the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        if self.dataset is None:
            return []

        start, end = self.index_range(page, page_size)

        dataset = self.dataset()
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        data = self.get_page(page, page_size)
        Set = self.dataset()
        total_count = len(Set) if Set else 0
        total_pages = math.ceil(total_count / page_size) if Set else 0
        size = len(data) if data else 0

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        media = {
                "page_size": size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
        return media
