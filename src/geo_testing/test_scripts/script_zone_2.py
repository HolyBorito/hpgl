#
#   Copyright 2009 HPGL Team
#   This file is part of HPGL (High Perfomance Geostatistics Library).
#   HPGL is free software: you can redistribute it and/or modify it under the terms of the BSD License.
#   You should have received a copy of the BSD License along with HPGL.
#

from geo import *
from sys import *

NI = 166
NJ = 141
NK = 5

print "Loading property..."
prop = load_gslib_ind_property("input_1_gslib.inc", -99, [0,1], NI, NJ, NK)
#write_property(prop, "input_eclipse.inc", "gslib_input", -99);
#del(prop)
#prop = load_cont_property("input_eclipse.inc", -99)
print "Done"

grid = SugarboxGrid(NI, NJ, NK)

ik_data =  [	{
			"cov_type": 0, 
			"ranges": (10, 10, 10),
			'sill': 0.4,
			"radiuses": (10, 10, 10),
			"max_neighbours": 12,
			"marginal_prob": 0.5,
			"value": 0
		},
		{
			"cov_type": 0, 
			"ranges": (10, 10, 10),
			"sill": 0.4,
			"radiuses": (10, 10, 10),
			"max_neighbours": 12,
			"marginal_prob": 0.5,
			"value": 1
		}]
prop2 = sis_simulation(prop, grid, ik_data, seed=3241347, use_vpc = False)
write_gslib_property(prop2, "zone_2_output.inc", "SK_2", -99, NI, NJ, NK)
#del(prop2)