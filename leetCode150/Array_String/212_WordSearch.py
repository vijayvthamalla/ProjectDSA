"""
212. Word Search II
Hard

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea",
"eat","rain"] Output: ["eat","oath"] Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    words_found = []
    for word in words:
        temp = word[0]
        starting_points = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == temp:
                    starting_points.append((i, j))
        for i in starting_points:
            prev = []
            res = graph_search(board, word[1:], i, prev)
            if res == "found":
                words_found.append(word)
                break
    return words_found


def find_next_points(m, n, start, prev):
    next_points = []
    i, j = start
    i_prev = i - 1
    i_next = i + 1
    j_prev = j - 1
    j_next = j + 1
    if i_prev in range(m):
        if (i_prev, j) not in prev:
            next_points.append((i_prev, j))
    if i_next in range(m):
        if (i_next, j) not in prev:
            next_points.append((i_next, j))
    if j_prev in range(n):
        if (i, j_prev) not in prev:
            next_points.append((i, j_prev))
    if j_next in range(n):
        if (i, j_next) not in prev:
            next_points.append((i, j_next))
    return next_points


def find_valid_points(board, word, points):
    valid_points = []
    for i in points:
        idx, idy = i
        if board[idx][idy] == word[0]:
            valid_points.append(i)
    return valid_points


def graph_search(board, word, starting_point, prev):
    if word == '':
        return "found"
    next_points = find_next_points(len(board), len(board[0]), starting_point, prev)
    valid_points = find_valid_points(board, word, next_points)
    if len(valid_points) > 0:
        prev.append(starting_point)
        for i in valid_points:
            res = graph_search(board, word[1:], i, prev)
            if res == "found":
                return "found"
    else:
        return "Not Found"
