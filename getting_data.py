# 'r' means read-only, it's assumed if you leave it out
# file_for_reading = open('reading_file.txt', 'r')
# file_for_reading2 = open('reading_file.txt')

# 'w' is write
# file_for_writting = open('writting_file.txt', 'w')

# 'a' is append -- for adding to the end of the file
# file_for_appending = open('appending_file.txt', 'a')

# don't forget to close the files when you are done
# file_for_writting.close()

# with open(filename) as f:
#     data = function_that_gets_data_from(f)
# At this point f has already been closed, so don't try to use it

from collections import Counter


def get_domain(email_address: str) -> str:
    """Split on '@' ans return the last piece"""
    return email_address.lower().split('@')[-1]

# A couple of tests
assert get_domain('joelgrus@gmail.com') == 'gmail.com'
assert get_domain('joel@m.datasciencester.com') == 'm.datasciencester.com'

with open('email_address.txt', 'r') as f:
    domail_counts = Counter(get_domain(line.strip()) for line in f if "@" in line)
