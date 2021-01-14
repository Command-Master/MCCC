scoreboard players operation $exp namespace = $val namespace
scoreboard players operation $exp namespace /= $8388608 namespace
scoreboard players operation $exp namespace %= $256 namespace
scoreboard players operation $sig namespace = $val namespace
scoreboard players operation $sig namespace %= $8388608 namespace
#tellraw @a[tag=fdebug] ["exp: ", {"score": {"name": "$exp", "objective": "namespace"}}]
#tellraw @a[tag=fdebug] ["sig: ", {"score": {"name": "$sig", "objective": "namespace"}}]
#tellraw @a[tag=fdebug] ["all: ", {"score": {"name": "$a0", "objective": "namespace"}}]
function namespace:tree/scale_float
execute store result score $out namespace run data get storage namespace:main temp
execute if score $val namespace matches ..-1 run scoreboard players operation $out namespace *= $-1 namespace