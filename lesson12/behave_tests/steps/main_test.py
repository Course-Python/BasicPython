import behave


@behave.given('{func} function')
def step_impl(context, func):
    import main
    context.scenario_func = getattr(main, func)  # main.args_sum; main.f_123

@behave.when('arguments are {args_list}')
def step_impl(context, args_list):
    context.args_list = map(int, args_list.split(' '))

@behave.then('function return {result}')
def step_impl(context, result):
	func_result = context.scenario_func(*context.args_list)
	assert func_result == int(result), '{} != {}'.format(func_result, result)
