from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Pacote estatística ADS'
LONG_DESCRIPTION = 'Módulos de estatística desenvolvidos no curso de Análise e Desenvolvimento de Sistemas 2022-2025'

# Setting up
setup(
    # 'name' deve corresponder ao nome da pasta referente
    name="mod_03_estatistica_descritiva",
    version=VERSION,
    author="Matheus Gomes",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # adicione outros pacotes que precisem ser instalados com o seu pacote. Ex.: 'caer'
    keywords=['python', 'first packege'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
