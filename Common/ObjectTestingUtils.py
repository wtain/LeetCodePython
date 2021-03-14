
def call_method(o, name, *args, **kwargs):
    # print("*** Calling " + name + " with " + str(args) + " and " + str(kwargs))
    return getattr(o, name)(*args, **kwargs)


def create_object(class_name, *args, **kwargs):
    return globals()[class_name](*args, **kwargs)
