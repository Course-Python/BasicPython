Feature: check main functions

  Scenario: check args_sum function
     Given args_sum function
      when arguments are 1 2 3 4
      then function return 10

  Scenario: check args_sum function with 2 param
     Given args_sum function
      when arguments are 50 2
      then function return 52

  Scenario: check my_func function
     Given my_func function
      when arguments are 1 2 3 4
      then function return 15
