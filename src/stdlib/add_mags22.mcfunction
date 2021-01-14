execute if score $expa namespace matches 255 run scoreboard players operation $out namespace = $aval namespace
execute if score $expa namespace matches 255 run scoreboard players set $r namespace 1
scoreboard players operation $exp namespace = $expa namespace
execute unless score $expb namespace matches 0 run scoreboard players add $sigb namespace 536870912
execute if score $expb namespace matches 0 run scoreboard players operation $sigb namespace += $sigb namespace
scoreboard players operation $jam namespace = $sigb namespace
scoreboard players operation $jamby namespace = $expdiff namespace
function namespace:shift_right_jam
scoreboard players operation $sigb namespace = $jammed namespace