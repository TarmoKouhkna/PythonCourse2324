#
# from tree import items_table
#
#
# def print_hierarchy(items, level=0):
#     """
#     Print the hierarchical structure of items with indentation.
#
#     Args:
#         items (list): List of dictionaries representing the items.
#         level (int): Current level of indentation.
#     """
#     for item in items:
#         print("  " * level + item["name"])
#         print_hierarchy(item["children"], level + 1)
#
#
# if __name__ == "__main__":
#     print_hierarchy(items_table)


from tree import items_table


def print_name_rec(item, sep="-"):
    print(f"{sep} {item['name']}")
    if len(item['children']):
        for child in item['children']:
            print_name_rec(child, sep=f"{sep} -")


for item in items_table:
    print_name_rec(item)
    