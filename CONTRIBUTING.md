# Git Workflow For Contributors

> Thank you for wanting to help, please follow these guidelines. We only accept pull requests for current issues, as you will see in the documentation below you will need the issue# during your pull request.
> If you don't have git on your machine, [install it](https://help.github.com/articles/set-up-git/).

## First Steps

Please contact project manager for next assignement.
Assign yourself to the issue, make note of given issue#, you will need the issue# later.

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd app-in-a-day
```

Now create a branch using the `git checkout` command:

> Please make sure the branch-name is the issue#number
> For example:

```
git checkout -b issue#10
```

## Make necessary changes and commit those changes

Now open the code into your favorite editor and start making any changes you feel are needed to fix the issue.
Please commit your code frequently and keep within the scope of the issue. For example if your issue was fixing a bug with a form, don't go styling the navbar at the same time.

> follow these practices for commit messages: https://chris.beams.io/posts/git-commit/

## Push changes to GitHub

Push your changes using the command `git push`:

```
git push origin <add-your-branch-name>
```

replacing `<add-your-branch-name>` with the name of the branch you created earlier.

## Submit your changes for review

If you go to the repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.
Change the title and description to explain your changes. Please make sure to use one of the keywords in your description in order to link your pull request to the issue.

> Example:
```
- Title: [issue#112] Add create shopping list form
- Description: Added a new shopping list form that gives the user the ability to create and edit shopping list. This commit solves #10
- Click Create pull request.
```
Don't forget to use one of the linking keywords. You can learn more about linking pull requests at the [GitHub Docs](https://docs.github.com/en/github/managing-your-work-on-github/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword).

- PLEASE INFORM PROJECT MANAGER
- You and project manager will review current changes to ensure no bugs are found

## What To Do After Your Changes Get Approved

- checkout main branch
- delete issue branch
- pull latest code
```
git checkout main

git branch -d <branch-name>

git pull
```
> go ask for next assignement

## Style Guide
**Files & Routes**
- files and routes should be named with all lower case letters and underscores between words

**CSS**
- Please follow the BEM style guide for CSS
  - https://www.freecodecamp.org/news/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849/

**Jinja Style Guide**
```
<link rel="stylesheet" href="{{ url_for('static', filename='styles/main.css') }}">

{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    {% for category, message in messages %}
      <div class="alert alert-{{ category }}">
        <h1>{{ message }}</h1>
      </div>
    {% endfor %}
  {% endif %}
{% endwith %}

{% block content %}{% endblock %}
```

**Python**
- Classes start capitalized and use camelCasing
- functions/methods names use snake_casing
- Limit all lines to a maximum of 79 characters.
- Surround top-level function and class definitions with two blank lines.
- Method definitions inside a class are surrounded by a single blank line.
- leave an empy line at the bottom of the file

```


class Person:

    def method():
        pass


def greeting():
    return "Hello"


print(greeting())
```