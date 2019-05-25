class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.users:
        return True

    for group in group.groups:
        return is_user_in_group(user, group)
    return False

parent = Group("parent")
child = Group("child")
sibling = Group("sibling")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_sibling_user = "sub_sibling_user"
sub_child.add_user(sub_child_user)
sibling.add_user(sub_sibling_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(sibling)


def test_cases():
    assert is_user_in_group(sub_child_user, parent) == True
    assert is_user_in_group(sub_child_user, child) == True
    assert is_user_in_group(sub_child_user, sub_child) == True
    assert is_user_in_group(sibling, sub_child) == False
    assert is_user_in_group(sub_sibling_user, sibling) == True
    print("All the test cases passed")

test_cases()
