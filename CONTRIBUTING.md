# Contributing to Inversify

## Setup

1 - Create virtual environment

```sh
virtualenv venv
```

2 - Clone your fork of the repository:

```sh
git clone https://github.com/{YOUR_USERNAME}/django_telegram_bot.git
```

3 - Install dependencies:

```sh
pip install -r requirements.txt
```

## Guidelines

- Please try to [combine multiple commits before pushing](http://stackoverflow.com/questions/6934752/combining-multiple-commits-before-pushing-in-git)

- Please use `TDD` when fixing bugs. This means that you should write a unit test that fails because it reproduces the issue, then fix the issue finally run the test to ensure that the issue has been resolved. This helps us to prevent fixed bugs from happening again in the future.

- Please keep the test coverage at 100%. Write additional unit test if necessary

- Please create an issue before sending a PR ff your it is going to change the public interface of InversifyJS or it includes significant architecture changes.

- Feel free to ask for help from other members of the InversifyJS team via the chat / mailing list or github issues.
