class User:
    def __init__(self, username):
        self.username = username
        self.permissions = set()
        self.permissions_history = []

    def grant_permission(self, permission):
        if permission not in self.permissions:
            self.permissions.add(permission)
            self.permissions_history.append((permission, 'granted'))
            print(f"Permission '{permission}' granted to user '{self.username}'.")

    def revoke_permission(self, permission):
        if permission in self.permissions:
            self.permissions.remove(permission)
            self.permissions_history.append((permission, 'revoked'))
            print(f"Permission '{permission}' revoked from user '{self.username}'.")

    def get_first_permissions_change(self):
        if self.permissions_history:
            return self.permissions_history[0]
        else:
            return None

    def get_permissions_change_history(self):
        return self.permissions_history


# Example usage:
if __name__ == "__main__":
    user1 = User("Alice")
    user1.grant_permission("read")
    user1.grant_permission("write")
    user1.revoke_permission("read")

    print("First permissions change:", user1.get_first_permissions_change())
    print("Permissions change history:", user1.get_permissions_change_history())
