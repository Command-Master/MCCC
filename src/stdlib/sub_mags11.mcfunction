execute unless score $expa namespace matches 0 run scoreboard players remove $expa namespace 1
execute store result score $sign namespace if score $aval namespace matches ..-1
execute if score $sigdiff namespace matches ..-1 store result score $sign namespace if score $sign namespace matches 0
execute if score $sigdiff namespace matches ..-1 run scoreboard players operation $sigdiff namespace *= $-1 namespace
scoreboard players operation $a namespace = $sigdiff namespace
function namespace:count_leading_zeros
scoreboard players remove $count namespace 8
scoreboard players operation $exp namespace = $expa namespace
scoreboard players operation $exp namespace -= $count namespace
execute if score $exp namespace matches ..-1 run scoreboard players operation $count namespace = $expa namespace
execute if score $exp namespace matches ..-1 run scoreboard players set $exp namespace 0
scoreboard players operation $sign namespace *= $-inf namespace
scoreboard players operation $out namespace = $sign namespace
scoreboard players operation $exp namespace *= $8388608 namespace
scoreboard players operation $out namespace += $exp namespace
scoreboard players operation $sig namespace = $sigdiff namespace
scoreboard players operation $2p namespace = $count namespace
function namespace:tree/power_of_two
scoreboard players operation $sig namespace *= $p2 namespace
scoreboard players operation $out namespace += $sig namespace
scoreboard players set $r namespace 1