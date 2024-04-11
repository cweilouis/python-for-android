from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class HttptoolsRecipe(CompiledComponentsPythonRecipe):
    version = '0.6.1'
    #url = 'https://github.com/MagicStack/httptools/archive/refs/tags/v{version}.zip'
    url = 'https://files.pythonhosted.org/packages/67/1d/d77686502fced061b3ead1c35a2d70f6b281b5f723c4eff7a2277c04e4a2/httptools-{version}.tar.gz'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False


recipe = HttptoolsRecipe()
