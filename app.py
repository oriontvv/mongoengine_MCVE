from flask import Flask, jsonify
from models import EntityChange
from mongoengine.base.datastructures import BaseDict

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'test'}


def test():
    data = {u'int_id': 100500, u'_cls': 'BuildingKind'}
    instance = EntityChange()
    instance.new_data = data

    print('isinstance(instance.new_data, BaseDict): ',
          isinstance(instance.new_data, BaseDict))

    print('type(instance.new_data)', type(instance.new_data))

    print('instance.new_data', instance.new_data)


test()


@app.route('/')
def todo():
    test()
    return jsonify({'ok': True})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
