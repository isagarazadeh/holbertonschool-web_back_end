#!/usr/bin/env python3
"""Simple function"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets pages"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        pages = index_range(page, page_size)
        out_list = []
        with open(self.DATA_FILE) as file_obj:
            reader_obj = csv.reader(file_obj)
            for i in range(0, pages[0] + 1):
                try:
                    next(reader_obj)
                except Exception:
                    break
            for j in range(0, page_size):
                try:
                    out_list.append(next(reader_obj))
                except Exception:
                    out_list = []
                    break
        return out_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Gets pages and returns dict"""
        data = self.get_page(page, page_size)
        next_page_data = self.get_page(page + 1, page_size)
        next_page = None if len(next_page_data) == 0 else page + 1
        prev_page = page - 1 if page > 1 else None
        total_page = math.ceil(len(self.dataset()) / page_size)
        dictionary = {'page_size': page_size, 'page': page, 'data': data,
                      'next_page': next_page, 'prev_page': prev_page,
                      'total_pages': total_page}
        return dictionary
