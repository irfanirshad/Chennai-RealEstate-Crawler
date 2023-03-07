"""
Strategy Design Pattern : An Interface to choose which type of service driver needs for scraping.
Services  include:
    1) MagicBricksService
    2) NinetyNineService
"""
from abc import ABC, abstractmethod

class ScrapingStrategy(ABC):
    @abstractmethod
    def print_strategy(self):
        pass