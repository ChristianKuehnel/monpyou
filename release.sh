
#!/bin/bash
# release current branch to pypi

echo Releasing version:
grep __version__ monpyou/const.py
read -n1 -r -p "Press any key to continue..." key

rm -r dist
python3 setup.py sdist
venv/bin/twine upload dist/*
