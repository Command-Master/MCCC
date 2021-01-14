# input: $a0, $a1
# output: $r0
#say cabs
scoreboard players operation $aval namespace = $l0 namespace
scoreboard players operation $bval namespace = $l1 namespace
function namespace:float_mul
scoreboard players operation $val1 namespace = $out namespace
scoreboard players operation $aval namespace = $l0 namespace
scoreboard players operation $bval namespace = $l1 namespace
function namespace:float_mul
scoreboard players operation $aval namespace = $out namespace
scoreboard players operation $bval namespace = $val1 namespace
function namespace:float_add
scoreboard players operation $cval namespace = $out namespace
#say sqrt here
execute unless score $cval namespace matches 0 run function namespace:float_sqrt
#say sqrt end
scoreboard players operation $r0 namespace = $out namespace