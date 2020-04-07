import sys
import random
import string
import json


"""
{ "index" : {"_id" : "1" } }
{ "name" : "RANDOM_NAME", "mobile": "RANDOM_NUMER" }
{ "index" : {"_id" : "2" } }
{ "name" : "RANDOM_NAME", "mobile": "RANDOM_NUMER" }
"""

OUT_FILE = 'es_data.json'


def _generate_random_string(min_len=5, max_len=15):
    n = random.randint(min_len, max_len)
    return ''.join(random.choices(string.ascii_letters, k=n))


def _generate_random_number(n=11):
    return ''.join(random.choices(string.digits, k=n))


def _generate_data_file(data):
    with open(f"{OUT_FILE}", 'w+') as fp:
        json.dump(data, fp)
        # fp.write(data)


def generate_es_data(doc_len=5, add_to_file=False):
    data = ''
    doc_len = int(doc_len)

    for _id in range(1, doc_len+1):
        data += "{'index': {'_id': '%s'}}\n" % _id
        data += "{'name': '%s', 'mobile': '%s'}\n" % (_generate_random_string(), _generate_random_number())

        if add_to_file:
            _generate_data_file(data)

    return data


if __name__ == "__main__":

    args = sys.argv

    doc_len = 5
    add_to_file = False
    if len(args) > 1:
        try:
            doc_len = args[1]
            add_to_file = args[2]
        except IndexError:
            add_to_file = False

    d = generate_es_data(doc_len=doc_len, add_to_file=add_to_file)

    if add_to_file:
        print(f'Added File: {OUT_FILE}')
    else:
        print(d)
