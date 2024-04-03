from engine.require import *





__all__ = ("Components_round", "Components_floor", "Components_ceil")





def Components_round(value, constant, swap):
	return round(
		value
	)



def Components_floor(value, constant, swap):
	return math.floor(value)



def Components_ceil(value, constant, swap):
	return math.ceil(value)





