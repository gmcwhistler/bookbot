#!/usr/bin/env python3

def main():
    file_contents = ""

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # print(file_contents)
    _word_count = _count_words(file_contents)
    # print(_word_count)
    _char_count_dict = _count_characters(file_contents)
    # print(_char_count)

    _create_report(_word_count, _char_count_dict)


def _sort_on(dict):
    return dict["count"]


def _summarize_characters(_char_dict: dict):
    _char_list = []
    for _key in _char_dict:
        _temp = {}
        if _key.isalpha():
            _temp["character"] = _key
            _temp["count"] = _char_dict[_key]
            _char_list.append(_temp)
    _char_list.sort(reverse=True, key=_sort_on)
    return _char_list


def _create_report(_word_count: int, _char_count_dir: dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{_word_count} words found in the doucment\n")
    _char_list = _summarize_characters(_char_count_dir)
    for foo in _char_list:
        _character = foo["character"]
        _count = foo["count"]
        print(f"The {_character} character was found {_count} times")


def _count_words(_my_string: str):
    return len(_my_string.split())


def _count_characters(_my_string: str):
    _char_dict = {}
    for _char in _my_string:
        _lowered_char = _char.lower()
        if _lowered_char in _char_dict:
            _char_dict[_lowered_char] += 1
        else:
            _char_dict[_lowered_char] = 1

    return _char_dict


if __name__ == "__main__":
    main()
