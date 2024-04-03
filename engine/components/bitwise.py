from engine.require import *





__all__ = ("Components_and", "Components_or", "Components_not")





def Components_and(value, constant, swap):
	if (swap):
		return constant and value

	else:
		return value and constant



def Components_or(value, constant, swap):
	if (swap):
		return constant or value

	else:
		return value or constant



def Components_not(value, constant, swap):
	return not value






