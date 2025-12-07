import json



def add(params:str)-> int:
    params = json.loads(params)
    a = params.get('a')
    b = params.get('b')
    return a + b

