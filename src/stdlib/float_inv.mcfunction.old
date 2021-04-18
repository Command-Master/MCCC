# magic inverse cheats
# input: $aval

scoreboard players operation $org namespace = $aval namespace

# magic inverse constant
scoreboard players set $bval namespace 2129950676
scoreboard players operation $bval namespace -= $aval namespace
scoreboard players operation $aval namespace = $bval namespace
# tellraw @a ["div: ", {"score": {"name": "$aval", "objective": "namespace"}}]
# tellraw @a ["div: ", {"score": {"name": "$bval", "objective": "namespace"}}]
scoreboard players operation $x namespace = $bval namespace
function namespace:float_mul
scoreboard players operation $aval namespace = $out namespace
scoreboard players operation $bval namespace = $org namespace
function namespace:float_mul
scoreboard players operation $bval namespace = $out namespace
scoreboard players operation $aval namespace = $x namespace
scoreboard players add $aval namespace 8388608
function namespace:float_sub
scoreboard players operation $x namespace = $out namespace

scoreboard players operation $aval namespace = $x namespace
scoreboard players operation $bval namespace = $x namespace
function namespace:float_mul
scoreboard players operation $aval namespace = $out namespace
scoreboard players operation $bval namespace = $org namespace
function namespace:float_mul
scoreboard players operation $bval namespace = $out namespace
scoreboard players operation $aval namespace = $x namespace
scoreboard players add $aval namespace 8388608
function namespace:float_sub
# tellraw @a ["div: ", {"score": {"name": "$out", "objective": "namespace"}}]