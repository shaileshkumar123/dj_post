# dj_post
<p align="center">
    Django Post Test
</p>

---

A template to create testcase file for django.

## To Install

```
# Activate from https://pub.dev
dart pub global activate mason_cli

# Or install from https://brew.sh
brew tap felangel/mason
brew install mason
```

## Documentation

```sh

# 🚀 Initialize mason
mason init

# Inside your mason.yaml file, add the brick name(dj_post) and the GitHub repository link like below.
bricks:
  dj_post:
      git:
        url: https://github.com/shaileshkumar123/dj_post
        path: 

Then run mason get to register that brick to generate a new file. Now you can use the greeting bricks like normal in your projects.

# To check list of bricks
mason ls

# Once a brick is added it can be used via the mason make command:
mason make <BRICK_NAME>
```
