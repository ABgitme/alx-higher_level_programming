#!/usr/bin/python3
def search_replace(my_list, search_element, replace_element):
    replaced = list(map(lambda element: replace_element
                        if element == search_element else element, my_list))
    return replaced
