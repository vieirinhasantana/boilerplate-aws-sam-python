from __future__ import print_function

TERMINATOR = "\x1b[0m"
INFO = "\x1b[1;33m [INFO]: "
SUCCESS = "\x1b[1;32m [SUCCESS]: "
HINT = "\x1b[3;33m"


def main():

    project_name = '{{ cookiecutter.project_name }}'

    print(f"{SUCCESS} Project initialized successfully! You can now jump to {project_name} folder. {TERMINATOR}")
    print(f"{INFO} {project_name}/README.md contains instructions on how to proceed. {TERMINATOR}")


if __name__ == '__main__':
    main()
