[![Python applications test with Github Actions](https://github.com/azizhamza-code/best-practices/actions/workflows/main.yml/badge.svg)](https://github.com/azizhamza-code/best-practices/actions/workflows/main.yml)


# best-practices

## Packaging Tool :  Pipenv = pip + venv

### Problems that Pipenv solves :

* Dependency management with requiremnt.txt

1. the build with requirement.txt isn't deterministic 
2. thinking of using pip freeze may solve the probleme , but now you are responsible of keeping the sub-dependencies up-to-date even they're sub-dependencies 

these two problemes lead as to ask : How do you allow for deterministic builds for your Python project without gaining the responsibility of updating versions of sub-dependencies

* pipenv has virtual envirenment management built-in

* and is smart enough to install packages that meet all the requirements without you explicitly specifying sub-dependency versions

* by contrast to poetry pipenv avoids making assumptions that the application being worked on will support distribution as a pip-installable Python package.

## Project scaffold for python

* using a makefile  to keep track of commands used

* runing a test and linthing our code

* using virtual envirenment

## Using CI/CD:
![image](https://user-images.githubusercontent.com/66756919/193797076-c9720766-ea44-40b8-bed8-30786722b60a.png)

