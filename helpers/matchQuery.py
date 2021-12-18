from difflib import SequenceMatcher


def matchQuery(query:str, queryList:list, exact:bool=False):
    if(exact):
        if(query in queryList):
            return True
        else:
            return False
    for q in queryList:
        if SequenceMatcher(None, query, q.lower()).ratio() > 0.8:
            return True
    return False