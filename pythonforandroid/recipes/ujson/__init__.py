from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class UJsonRecipe(CompiledComponentsPythonRecipe):
    version = '5.9.0'
    url = 'https://files.pythonhosted.org/packages/6e/54/6f2bdac7117e89a47de4511c9f01732a283457ab1bf856e1e51aa861619e/ujson-{version}.tar.gz'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False
    


recipe = UJsonRecipe()
