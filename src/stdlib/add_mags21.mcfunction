execute if score $expb namespace matches 255 run scoreboard players operation $out namespace = $bval namespace
execute if score $expb namespace matches 255 run scoreboard players set $r namespace 1
scoreboard players operation $exp namespace = $expb namespace
execute unless score $expa namespace matches 0 run scoreboard players add $siga namespace 536870912
execute if score $expa namespace matches 0 run scoreboard players operation $siga namespace += $siga namespace
scoreboard players operation $jam namespace = $siga namespace
scoreboard players operation $jamby namespace = $expdiff namespace
scoreboard players operation $jamby namespace *= $-1 namespace
function namespace:shift_right_jam
scoreboard players operation $siga namespace = $jammed namespace