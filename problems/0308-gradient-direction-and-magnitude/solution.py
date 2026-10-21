import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	grad  = np.array(gradient, dtype = float)

	#Calculating L2 norm (magnitude)
	magnitude = float(np.linalg.norm(grad))

	#Handling zero vector edge case
	if magnitude == 0:
		direction = np.zeros_like(grad).tolist()
		descent_direction = np.zeros_like(grad).tolist()
	else :
		direction = (grad/magnitude).tolist()
		descent_direction = (-grad/magnitude).tolist()

	return {
		"magnitude" : magnitude,
		"direction" : direction,
		"descent_direction" : descent_direction
 	}		
	pass