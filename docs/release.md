# Release

Instructions for releasing a new `electivity` version.

1. `pipenv install -d` to install developer tools
2. `pipenv shell`
3. Commit all changes
4. `bumpversion {major, minor or patch}` to automatically update version numbers
   - The files that contain versions to be bumped are included in `.bumpversion.cfg`
   - Bump will be automatically commited
5. (Optional) Delete previous version binaries in `electivity/dist`.
6. `python setup.py sdist bdist_wheel` to create new version binaries.
7. `twine upload --skip-existing dist/*`.
8. Create a new release in the Github repository describing the changes.
