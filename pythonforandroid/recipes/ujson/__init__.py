from typing import List
from pythonforandroid.recipe import CppCompiledComponentsPythonRecipe


class UJsonRecipe(CppCompiledComponentsPythonRecipe):
    version = "5.9.0"
    url = "https://files.pythonhosted.org/packages/6e/54/6f2bdac7117e89a47de4511c9f01732a283457ab1bf856e1e51aa861619e/ujson-{version}.tar.gz"
    name = "ujson"
    depends: List[str] = ["setuptools"]
    call_hostpython_via_targetpython = False
    install_in_hostpython = True

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['LDFLAGS'] += ' -lc++_shared'
        return env


recipe = UJsonRecipe()