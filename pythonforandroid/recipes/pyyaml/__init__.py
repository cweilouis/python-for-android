import re
from pythonforandroid.logger import info
from pythonforandroid.recipe import CythonRecipe


class PyyamlRecipe(CythonRecipe):
    version = '6.0.1'
    url = 'https://files.pythonhosted.org/packages/cd/e5/af35f7ea75cf72f2cd079c95ee16797de7cd71f29ea7c68ae5ce7be1eda0/PyYAML-{version}.tar.gz'
    depends = ['setuptools']

#    def get_recipe_env(self, arch=None, with_flags_in_cc=True):
#        """
#        - Moves all -I<inc> -D<macro> from CFLAGS to CPPFLAGS environment.
#        - Moves all -l<lib> from LDFLAGS to LIBS environment.
#        - Copies all -l<lib> from LDLIBS to LIBS environment.
#        - Fixes linker name (use cross compiler)  and flags (appends LIBS)
#        """
#        env = super().get_recipe_env(arch, with_flags_in_cc)
#        # CFLAGS may only be used to specify C compiler flags, for macro definitions use CPPFLAGS
#        regex = re.compile(r'(?:\s|^)-[DI][\S]+')
#        env['CPPFLAGS'] = ''.join(re.findall(regex, env['CFLAGS'])).strip()
#        env['CFLAGS'] = re.sub(regex, '', env['CFLAGS'])
#        info('Moved "{}" from CFLAGS to CPPFLAGS.'.format(env['CPPFLAGS']))
#        # LDFLAGS may only be used to specify linker flags, for libraries use LIBS
#        regex = re.compile(r'(?:\s|^)-l[\w\.]+')
#        env['LIBS'] = ''.join(re.findall(regex, env['LDFLAGS'])).strip()
#        env['LIBS'] += ' {}'.format(''.join(re.findall(regex, env['LDLIBS'])).strip())
#        env['LDFLAGS'] = re.sub(regex, '', env['LDFLAGS'])
#        info('Moved "{}" from LDFLAGS to LIBS.'.format(env['LIBS']))
#        return env


recipe = PyyamlRecipe()
