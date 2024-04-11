from pythonforandroid.recipe import PythonRecipe

class UvloopRecipe(PythonRecipe):
    # 0.19.0
    version = '0.19.0'
    url = 'https://files.pythonhosted.org/packages/9c/16/728cc5dde368e6eddb299c5aec4d10eaf25335a5af04e8c0abd68e2e9d32/uvloop-{version}.tar.gz'
    depends = ['cython', 'setuptools', 'librt', 'libpthread']
    call_hostpython_via_targetpython = False

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env["LIBUV_CONFIGURE_HOST"] = arch.command_prefix
        env["PLATFORM"] = "android"
        return env


recipe = UvloopRecipe()
