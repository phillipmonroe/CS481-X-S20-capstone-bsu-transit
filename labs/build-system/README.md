# Build system documentation

You will need someway to build or run your code from the terminal. Building your code is dependent on the language and technologies used. For example if you project is written in C then your build system could use [cmake](https://cmake.org/). If you are using Java then you may use [ant](https://ant.apache.org/) or [maven](https://maven.apache.org/). You must use **some sort** of build system it is not acceptable to compile your code by hand.

Your task is to setup an example build system and document how to compile/run a simple **hello world** type of application **from the terminal**. If your language has a package manager such as [NPM](https://www.npmjs.com/) **DO NOT** commit your dependencies to this repository.

Here is an example using cmake:

```bash
mkdir build
cd build
cmake ..
make
```

TODO: Write your documentation here

## Setup .gitignore

 At this point you have enough information to add a .gitignore for your language, frameworks, package manager etc. to this repository. This is an easy step there are a collection of [gitignore's](https://github.com/github/gitignore) already configured for you to use out of the box!

## Submission

All files for this lab should be added to **this** directory. Remember that [30% of your grade](../../docs/syllabus.md#grading) is dependent on individual effort! So you **MUST** document what you worked on for this lab. If you spent the entire lab doing research then you must upload a summary of your research. Any work that is not documented by some sort of artifact (source code, documentation, etc.) will not be counted towards your final grade.

This lab is due on the date specified in the root level [README.md](../../README.md).
