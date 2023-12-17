"""
https://leetcode.com/problems/design-a-food-rating-system/description/?envType=daily-question&envId=2023-12-17

Design a food rating system that can do the following:

Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:

FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.



Example 1:

Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".


Constraints:

1 <= n <= 2 * 104
n == foods.length == cuisines.length == ratings.length
1 <= foods[i].length, cuisines[i].length <= 10
foods[i], cuisines[i] consist of lowercase English letters.
1 <= ratings[i] <= 108
All the strings in foods are distinct.
food will be the name of a food item in the system across all calls to changeRating.
cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
At most 2 * 104 calls in total will be made to changeRating and highestRated.
"""
import heapq
from collections import defaultdict
from typing import List, Type

from sortedcontainers import SortedSet

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# Runtime
# 980
# ms
# Beats
# 26.19%
# of users with Python3
# Memory
# 51.90
# MB
# Beats
# 16.07%
# of users with Python3
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_ratings = defaultdict(lambda: SortedSet())
        self.food_cuisine = {}
        self.food_rating = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_cuisine[food] = cuisine
            self.food_rating[food] = rating
            self.cuisine_ratings[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        old_rating = self.food_rating[food]
        self.cuisine_ratings[cuisine].remove((-old_rating, food))
        self.cuisine_ratings[cuisine].add((-newRating, food))
        self.food_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        rating_neg, food = self.cuisine_ratings[cuisine][0]
        return food


# WRONG
# class FoodRatings:
#
#     def update_rating(self, cuisine, food, rating):
#         if cuisine not in self.cuisine_ratings or self.cuisine_ratings[cuisine][0] < rating or self.cuisine_ratings[cuisine][0] == rating and self.cuisine_ratings[cuisine][1] > food:
#             self.cuisine_ratings[cuisine] = [rating, food]
#
#     def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
#         self.cuisine_ratings = {}
#         self.food_cuisine = {}
#         for food, cuisine, rating in zip(foods, cuisines, ratings):
#             self.food_cuisine[food] = cuisine
#             self.update_rating(cuisine, food, rating)
#
#     def changeRating(self, food: str, newRating: int) -> None:
#         cuisine = self.food_cuisine[food]
#         self.update_rating(cuisine, food, newRating)
#
#     def highestRated(self, cuisine: str) -> str:
#         return self.cuisine_ratings[cuisine][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


tests = [
    [
        ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"],
        [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]],
        [null, "kimchi", "ramen", null, "sushi", null, "ramen"]
    ],
    [
        ["FoodRatings","changeRating","highestRated","changeRating","changeRating","changeRating","highestRated","highestRated"],
        [[
            ["emgqdbo","jmvfxjohq","qnvseohnoe","yhptazyko","ocqmvmwjq"],
            ["snaxol","snaxol","snaxol","fajbervsj","fajbervsj"],
            [2,6,18,6,5]],
            ["qnvseohnoe",11],["fajbervsj"],["emgqdbo",3],["jmvfxjohq",9],["emgqdbo",14],["fajbervsj"],["snaxol"]],
        [null,null,"yhptazyko",null,null,null,"yhptazyko","emgqdbo"]
    ],
    [
        ["FoodRatings",
         "changeRating","changeRating","changeRating","highestRated"],
        [[
            ["emgqdbo","jmvfxjohq","qnvseohnoe"],
            ["snaxol","snaxol","snaxol"],
            [2,6,18]],
            ["qnvseohnoe",11],["jmvfxjohq",9],["emgqdbo",14],["snaxol"]],
        [null,null,null,null,"emgqdbo"]
    ]
]

run_object_tests(tests, cls=FoodRatings)
