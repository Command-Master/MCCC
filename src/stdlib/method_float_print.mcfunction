scoreboard players operation $exp namespace = $l0 namespace
scoreboard players operation $exp namespace /= $8388608 namespace
scoreboard players operation $exp namespace %= $256 namespace
scoreboard players operation $sig namespace = $l0 namespace
scoreboard players operation $sig namespace %= $8388608 namespace
tellraw @a[tag=fdebug] ["exp: ", {"score": {"name": "$exp", "objective": "namespace"}}]
tellraw @a[tag=fdebug] ["sig: ", {"score": {"name": "$sig", "objective": "namespace"}}]
tellraw @a[tag=fdebug] ["all: ", {"score": {"name": "$a0", "objective": "namespace"}}]
# execute store result data storage namespace:main temp double 1 run scoreboard players add $sig namespace 8388608
function namespace:tree/scale_float
execute if score $l0 namespace matches 0.. run tellraw @a {"nbt": "temp", "storage":"namespace:main"}
execute if score $l0 namespace matches ..-1 run tellraw @a ["-", {"nbt": "temp", "storage":"namespace:main"}]