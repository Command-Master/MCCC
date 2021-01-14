scoreboard players operation $sign namespace *= $-inf namespace
scoreboard players operation $out namespace = $sign namespace
scoreboard players operation $exp namespace *= $8388608 namespace
scoreboard players operation $out namespace += $exp namespace
execute store result score $signn namespace if score $sig namespace matches ..-1
execute if score $signn namespace matches 1 run scoreboard players operation $sig namespace += $-inf namespace
scoreboard players operation $sig namespace /= $2 namespace
execute if score $signn namespace matches 1 run scoreboard players add $sig namespace 1073741824
scoreboard players operation $out namespace += $sig namespace
scoreboard players set $r namespace 1