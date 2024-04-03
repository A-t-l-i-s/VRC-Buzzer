from engine.require import *

from .math import *
from .round import *
from .bitwise import *





__all__ = ("Components",)





class Components(RFT_Object):
	# ~~~~~~ Default Components ~~~~~~
	disabled = "disabled"


	components = RFT_Structure({
		disabled: None,

		"add": Components_add,
		"sub": Components_sub,
		"mul": Components_mul,
		"div": Components_div,
		"rdiv": Components_rdiv,

		"round": Components_round,
		"floor": Components_floor,
		"ceil": Components_ceil,

		"and": Components_and,
		"or": Components_or,
		"not": Components_not
	})

	componentsSingle = [
		None,
		"round",
		"floor",
		"ceil",
		"not"
	]
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



