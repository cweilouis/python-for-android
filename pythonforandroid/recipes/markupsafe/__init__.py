from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class MarkupsafeRecipe(CompiledComponentsPythonRecipe):
    version = '2.1.5'
    url = 'https://files.pythonhosted.org/packages/87/5b/aae44c6655f3801e81aa3eef09dbbf012431987ba564d7231722f68df02d/MarkupSafe-{version}.tar.gz'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False


recipe = MarkupsafeRecipe()