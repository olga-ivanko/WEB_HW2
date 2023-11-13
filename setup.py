from setuptools import setup, find_packages
setup(
    name='ins',
    version='0.1.0',
    description='some text',
    author='Name',
    py_modules=['group2.addressbook', 'group2.birthday_functions', 'group2.main', 'group2.notebook', 
    'group2.service_addressbook', 'group2.servicenote', 'group2.sort', 'group2.terminal_tips','group2.help_func'],
    install_requires=['prompt_toolkit'],
    entry_points={
        'console_scripts': [
            'pj1=group2.main:main',
        ],
    },
    exclude_package_data={'': ['*.bin']},
    package_data={'': ['*.md']}

)
