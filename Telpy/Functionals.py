from __future__ import annotations
from typing import List, Union

import requests

class OptionalKwargs():
    def __init__(self,kwargs):
        self.dictionary = {i:kwargs[i] for i in kwargs if kwargs[i]!=None}

    def __getitem__(self,key)->str:
        if key in self.dictionary.keys():
            return self.dictionary[key]
        return None

class InvalidArgument(Exception):
    pass

class MissingArgument(Exception):
    pass

def SimpleRequestHandler(BASE,http_type,path,return_type,params=None,json=None,debug=False):

    parson = dict()
    if params != None:
        parson["params"] = params
    if json != None:
        parson["json"] = json

    if http_type == "get":
        r = requests.get(BASE+path,**parson)
    elif http_type == "post":
        r = requests.post(BASE+path,**parson)
    if r.ok and r.json()["ok"]:
        if return_type == bool:
            return True
        else:
            return return_type(**r.json()["result"])
    else:
        try:
            tele_error = r.json()['result']
        except:
            tele_error = None
        raise InvalidArgument(f"An Error Occured accessing < {BASE+path} >\nReason:\tHTTP Error Message:\n{r.reason}\n\nTelegram API Error Message:\n{tele_error}\n\nRaw Eror: {r.text}")

def CleanObject(object):
    if object == None:
        return {}
    elif type(object) == dict:
        new_dict = {}
        for i in object:
            if i == "self":
                continue
            if object[i] != None:
                new_dict[i] = object[i]
        # print(object,"\n===============\n",new_dict,"\n<>")
        return new_dict

    else:
        to_delete = [i for i in dir(object) if getattr(object,i) == None and not i.startswith("_")]
        for i in to_delete:
            del object.__dict__[i]
        return object
