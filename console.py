#!/usr/bin/python3
import cmd
import models
from models.basemodel import BaseModel
from models.city import City
from models.touristsite import TouristSite
from models.description import Description

classes = {
        'BaseModel': BaseModel,
        'City': City,
        'TouristSite': TouristSite,
        'Description': Description
        }

class Console(cmd.Cmd):

    def do_all(self, arg):
        if arg:
            if arg in classes:
                for k, i in models.storage.all(arg).items():
                    print(i.to_dict())
            else:
                print("***Invalid Class***")
        else:
            for i in models.storage.all().values():
                print(i.to_dict())

    
    def do_quit(self, arg):
        print()
        return True

    
    def do_create(self, arg):
        if arg:
            args = arg.split(" ")
            if args[0] in classes:
                if args[0] == 'TouristSite':
                    try:
                        new = TouristSite()
                        new.city_id = args[1]
                        new.save()
                        print(new.id)
                    except Exception as e:
                        print("***", e)
                else:
                    try:
                        new = eval(args[0])()
                        new.save()
                        print(new.id)
                    except Exception as e:
                        print("***", e)
            else:
                print("***INvalid Class***")

    def do_update(self, arg):
        argl = arg.split(" ")
        if argl[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        objdict = models.storage.all()
        if "{}.{}".format(argl[0], argl[1]) not in objdict:
                print("** no instance found **")
                return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                value = argl[3].replace("_", " ")
                obj.__dict__[argl[2]] = valtype(value)
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        models.storage.save()

    
    def do_delete(self, arg):
        argl = arg.split(" ")
        if argl[0]:
            if argl[1]:
                for k, v in models.storage.all().items():
                    if v.to_dict().get('name') == argl[1]:
                        models.storage.delete(k)
        models.storage.save()
    

if __name__ == '__main__':
    Console().cmdloop()
