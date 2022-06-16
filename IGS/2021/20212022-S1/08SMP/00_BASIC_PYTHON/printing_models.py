
def print_models(unprinted_design, completed_models):
	while unprinted_design:
		current_design = unprinted_design.pop()
		completed_models.append(current_design)
		print(f"{current_design.upper()} has been printed and completed.")

def show_models(completed_models):
	for model in completed_models:
		print(f"{model.title()} is ready to sent to client.")

unprinted_design = ['phone case', 'motor livery', 'robot pendant']
completed_models = []

print_models(unprinted_design, completed_models)
show_models(completed_models)

print(unprinted_design)