def my_import(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


dictionary = {
    "contact": ['ContactUs', 'ContactUsSerializer'],
    "app-data": ['AppClassData', 'AppDataSerializer'],
    "domain": ['Domain', 'DomainSerializer'],
}


def get_data(models, page, rows, field="key", order="1", column=None, val=None, types=None):
    # pagination rows and columns
    val1 = rows * (page - 1)
    val2 = (val1 + rows)

    if models in dictionary:
        model = my_import('nivid.nividapp.src.models'+dictionary[models][0])
        print(model)
        return "Working on the Get Request"

def post_data(model, data):
    pass