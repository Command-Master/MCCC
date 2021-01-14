execute if score $expa namespace matches 255 run scoreboard players operation $out namespace = $aval namespace
execute if score $expa namespace matches 255 run scoreboard players set $r namespace 1
scoreboard players operation $exp namespace = $expa namespace
scoreboard players remove $exp namespace 1
scoreboard players operation $sig namespace = $siga namespace
scoreboard players operation $m2 namespace = $sig namespace
scoreboard players operation $m2 namespace /= $1073741824 namespace
scoreboard players operation $m2 namespace %= $2 namespace
execute if score $m2 namespace matches 0 run scoreboard players add $sig namespace 1073741824
scoreboard players operation $jam namespace = $sigb namespace
execute unless score $expb namespace matches 0 run scoreboard players add $jam namespace 1073741824
execute if score $expb namespace matches 0 run scoreboard players operation $jam namespace += $jam namespace