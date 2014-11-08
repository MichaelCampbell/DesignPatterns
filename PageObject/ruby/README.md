Ruby Page Object pattern

The Page Object Pattern in Ruby will help prevent brittle tests as your test framework matures. There are simple things you should look out for, and hopefully this repository can help you along the way.

If you have any questions, please contact Russell Bradley (@rusbra) and i'll do my best to assist, but hopefully this repo will help.

Separation of Colors

It is important to keep your page logic within your Page Objects, your page locators in your Locators file, and tests/assertions in your Test Cases. Although this may take additional setting up when beginning to build your test framework, this is very important to avoid endless refactoring.

- Needed

explanation of modules
config file
locators
Testcases
Concept of BaseObjects
