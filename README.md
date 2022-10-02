# best-practices

## Packaging Tool :  Pipenv = pip + venv

### Problems that Pipenv solves :

* Dependency management with requiremnt.txt

1. the build with requirement.txt isn't deterministic 
2. thinking of using pip freeze may solve the probleme , but now you are responsible of keeping the sub-dependencies up-to-date even they're sub-dependencies 

these two problemes lead as to ask : How do you allow for deterministic builds for your Python project without gaining the responsibility of updating versions of sub-dependencies

* pipenv has virtual envireent management built-in

* and is smart enough to install packages that meet all the requirements without you explicitly specifying sub-dependency versions

* by contrast to poetry pipenv avoids making assumptions that the application being worked on will support distribution as a pip-installable Python package.
