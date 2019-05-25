import os


def traverse_directory(suffix_extension_files, suffix, path):
    if os.path.isfile(path):
        if path.endswith(suffix):
            suffix_extension_files.append(path)
    else:
        for content in os.listdir(path):
            traverse_directory(suffix_extension_files, suffix, os.path.join(path, content))
    return suffix_extension_files

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    suffix_extension_files = []
    traverse_directory(suffix_extension_files, suffix, path)
    return suffix_extension_files


def test_cases():
    assert sorted(find_files('.c', './testdir')) == ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
    assert sorted(find_files('.h', './testdir')) == ['./testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h']
    assert sorted(find_files('.c', './testdir/subdir3/subsubdir1/b.h')) == []
    assert sorted(find_files('.h', './testdir/subdir3/subsubdir1/b.h')) == ['./testdir/subdir3/subsubdir1/b.h']
    return 'All test cases passed'

print(test_cases())
