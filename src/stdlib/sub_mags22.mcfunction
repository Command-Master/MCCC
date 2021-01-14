execute store result score $sign namespace if score sign namespace matches 0
execute if score $expb namespace matches 255 run scoreboard players operation $out namespace = $bval namespace
execute if score $expb namespace matches 255 run scoreboard players set $r namespace 1
scoreboard players operation $exp namespace = $expb namespace
scoreboard players remove $exp namespace 1
scoreboard players operation $sig namespace = $sigb namespace
scoreboard players operation $m2 namespace = $sig namespace
scoreboard players operation $m2 namespace /= $1073741824 namespace
scoreboard players operation $m2 namespace %= $2 namespace
execute if score $m2 namespace matches 0 run scoreboard players add $sig namespace 1073741824
scoreboard players operation $jam namespace = $siga namespace
execute unless score $expa namespace matches 0 run scoreboard players add $jam namespace 1073741824
execute if score $expa namespace matches 0 run scoreboard players operation $jam namespace += $jam namespace
scoreboard players operation $expdiff namespace *= $-1 namespace