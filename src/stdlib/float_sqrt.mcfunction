scoreboard players operation $org namespace = $cval namespace
scoreboard players operation $half namespace = $cval namespace
scoreboard players remove $half namespace 8388608
scoreboard players set $val namespace 1597463007
# can assume positive
scoreboard players operation $cval namespace /= $2 namespace
scoreboard players operation $val namespace -= $cval namespace

# newton iter:
scoreboard players operation $aval namespace = $val namespace
scoreboard players operation $bval namespace = $val namespace
function namespace:float_mul
scoreboard players operation $aval namespace = $out namespace
scoreboard players operation $bval namespace = $half namespace
function namespace:float_mul
# 1.5 in floating point
scoreboard players set $aval namespace 1069547520
scoreboard players operation $bval namespace = $out namespace
function namespace:float_sub
scoreboard players operation $aval namespace = $out namespace
scoreboard players operation $bval namespace = $val namespace
function namespace:float_mul
scoreboard players operation $val namespace = $out namespace

# newton iter:
scoreboard players operation $aval namespace = $val namespace
scoreboard players operation $bval namespace = $val namespace
function namespace:float_mul
scoreboard players operation $aval namespace = $out namespace
scoreboard players operation $bval namespace = $half namespace
function namespace:float_mul
# 1.5 in floating point
scoreboard players set $aval namespace 1069547520
scoreboard players operation $bval namespace = $out namespace
function namespace:float_sub
scoreboard players operation $aval namespace = $out namespace
scoreboard players operation $bval namespace = $val namespace
function namespace:float_mul
scoreboard players operation $val namespace = $out namespace

# end:
scoreboard players operation $aval namespace = $val namespace
scoreboard players operation $bval namespace = $org namespace
function namespace:float_mul