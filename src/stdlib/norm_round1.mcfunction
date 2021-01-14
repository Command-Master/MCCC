#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}, " ", {"score": {"name": "$exp", "objective": "namespace"}}, " ", {"score": {"name": "$sign", "objective": "namespace"}}]
scoreboard players set $r namespace 1
execute if score $sig namespace matches 0 run scoreboard players set $exp namespace 0
scoreboard players operation $sign namespace *= $-inf namespace
scoreboard players operation $out namespace = $sign namespace
scoreboard players operation $exp namespace *= $8388608 namespace
scoreboard players operation $out namespace += $exp namespace
execute store result score $2p namespace run scoreboard players remove $count namespace 7
function namespace:tree/power_of_two
scoreboard players operation $sig namespace *= $p2 namespace
#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}]
scoreboard players operation $out namespace += $sig namespace