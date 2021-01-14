#say good jam boy!
execute store result score $signn namespace if score $jam namespace matches ..-1
scoreboard players operation $jammed namespace = $jam namespace
execute if score $signn namespace matches 1 run scoreboard players operation $jammed namespace += $-inf namespace
scoreboard players operation $2p namespace = $jamby namespace
function namespace:tree/power_of_two
scoreboard players operation $jammed namespace /= $p2 namespace
scoreboard players set $2p namespace 31
scoreboard players operation $2p namespace -= $jamby namespace
function namespace:tree/power_of_two
execute if score $signn namespace matches 1 run scoreboard players operation $jammed namespace += $p2 namespace
scoreboard players operation $m2 namespace = $jammed namespace
scoreboard players operation $m2 namespace %= $2 namespace
#tellraw @a {"score": {"name": "$p2", "objective": "namespace"}}
scoreboard players operation $p2 namespace *= $2 namespace
#tellraw @a {"score": {"name": "$p2", "objective": "namespace"}}
scoreboard players operation $p2 namespace *= $jam namespace
#tellraw @a {"score": {"name": "$p2", "objective": "namespace"}}
execute unless score $p2 namespace matches 0 if score $m2 namespace matches 0 run scoreboard players add $jammed namespace 1