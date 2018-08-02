import sys

import mock


class MyImporter(object):
    sys = sys
    mock = mock

    class MyMock(mock.Mock):
        def __getattr__(self, name):
            try:
                return super(mock.Mock, self).__getattr__(name)
            except AttributeError:
                # Mock fails on private attributes
                return self.mock.Mock()

    def __init__(self, *args, **kwargs):
        super(MyImporter, self).__init__(*args, **kwargs)
        self.known_modules = []

    def fake_module(self, module_name, **mock_args):
        if module_name in self.known_modules:
            return

        self.known_modules.append(module_name)

        module = self.MyMock(name=module_name, **mock_args)
        module.__package__ = module_name
        module.__file__ = module_name
        module.__path__ = module_name
        module.__loader__ = self

        current_global = globals().get('__loader__')
        if current_global is not self:
            globals().update(__loader__=self)

        if self not in sys.meta_path:
            sys.meta_path.append(self)

        sys.modules[module_name] = module

    def find_module(self, fullname, path):
        module_name = fullname.split('.', 1)[0]
        if module_name in self.known_modules:
            return self

    def load_module(self, fullname):
        module = self.sys.modules.get(fullname)
        if module:
            return module

        module = self.mock.Mock(name=fullname)
        # module = types.ModuleType(fullname)
        module.__loader__ = self
        module.__package__ = fullname.rsplit('.', 1)[0]

        self.sys.modules[fullname] = module
        return module


importer = MyImporter()
fake_module = importer.fake_module
