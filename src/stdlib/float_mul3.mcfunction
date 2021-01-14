#tellraw @a [{"score": {"name": "$siga", "objective": "namespace"}}]
#tellraw @a [{"score": {"name": "$sigb", "objective": "namespace"}}]
scoreboard players operation $exp namespace = $expa namespace
scoreboard players operation $exp namespace += $expb namespace
scoreboard players remove $exp namespace 127

scoreboard players operation $temp namespace = $siga namespace
scoreboard players operation $temp namespace /= $8388608 namespace
scoreboard players operation $temp namespace %= $2 namespace
execute if score $temp namespace matches 0 run scoreboard players add $siga namespace 8388608
scoreboard players operation $siga namespace *= $128 namespace

scoreboard players operation $temp namespace = $sigb namespace
scoreboard players operation $temp namespace /= $8388608 namespace
scoreboard players operation $temp namespace %= $2 namespace
execute if score $temp namespace matches 0 run scoreboard players add $sigb namespace 8388608
scoreboard players operation $sigb namespace *= $256 namespace

#tellraw @a [{"score": {"name": "$siga", "objective": "namespace"}}]
#tellraw @a [{"score": {"name": "$sigb", "objective": "namespace"}}]
function namespace:float_mul4
execute if score $sig namespace matches 0..1073741824 run scoreboard players remove $exp namespace 1
execute if score $sig namespace matches 0..1073741824 run scoreboard players operation $sig namespace *= $2 namespace
#tellraw @a ["mul:",{"score": {"name": "$exp", "objective": "namespace"}}]
#tellraw @a ["mul:",{"score": {"name": "$expa", "objective": "namespace"}}]
#tellraw @a ["mul:",{"score": {"name": "$expb", "objective": "namespace"}}]
#scoreboard players operation $a0 namespace = $aval namespace
#function namespace:method_float_print
function namespace:round_pack