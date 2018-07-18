dictionaryIs = {'key1':'value','key2':[{'key3':'value','key4':'value'}]}

list(find('key3', dictionaryIs))

def find(key, dictionary):
    for k, v in dictionary.iteritems():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, dict):
                    for result in find(key, d):
                        yield result
 
'''you can refer this points ------
1.return a list
2.allow a list of documents to be passed
3.added a wild mode for case insensitive key substring lookups
4.added 100% test coverage
5.open sourced / and put it into public domain
6.gave it a name
7.added it to pypi
https://pypi.python.org/pypi/nested-lookup
 '''
