import json


def create_family_tree():
    family_tree = []

    print("Enter 'done' at any time to finish.")

    # Function to recursively add family members
    def add_family_member(parent_name):
        children = []
        while True:
            child_name = input(f"Enter child of {parent_name} (or 'done' to finish): ")
            if child_name.lower() == 'done':
                break
            grandchildren = add_family_member(child_name)
            children.append(grandchildren)
        return {'name': parent_name, 'children': children}

    # Enter both parents
    for i in range(2):
        parent_name = input(f"Enter the name of parent {i + 1}: ")
        grandchildren = []
        while True:
            child_name = input(f"Enter child of {parent_name} (or 'done' to finish): ")
            if child_name.lower() == 'done':
                break
            grandchildren.append(add_family_member(child_name))
        family_tree.append({'name': parent_name, 'children': grandchildren})

    return family_tree


def save_progress(family_tree, file_name):
    with open(file_name, 'w') as f:
        json.dump(family_tree, f, indent=4)
    print("Family tree saved successfully as", file_name)


def load_progress(file_name):
    try:
        with open(file_name, 'r') as f:
            family_tree = json.load(f)
        print("Progress loaded successfully from", file_name)
        return family_tree
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("No valid progress found. Starting a new session.")
        return None


def main():
    file_name = "family_tree_progress.json"
    family_tree = load_progress(file_name)

    if not family_tree:
        print("Welcome to the Family Tree Creator!")
        family_tree = create_family_tree()
        save_progress(family_tree, file_name)
    else:
        print("Resuming from previous session.")

    print("Exiting program.")


if __name__ == "__main__":
    main()
