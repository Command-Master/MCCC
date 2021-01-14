execute store result score $sign namespace if score $aval namespace matches ..-1
scoreboard players operation $siga namespace *= $128 namespace
scoreboard players operation $sigb namespace *= $128 namespace
execute if score $expdiff namespace matches 0.. run function namespace:sub_mags21
execute if score $expdiff namespace matches ..-1 run function namespace:sub_mags22
# sigX = sig, sigY = jam
scoreboard players operation $jamby namespace = $expdiff namespace
function namespace:shift_right_jam
scoreboard players operation $sig namespace -= $jammed namespace
#tellraw @a [{"score": {"name": "$sign", "objective": "namespace"}}, ", ", {"score": {"name": "$exp", "objective": "namespace"}}, ", ", {"score": {"name": "$sig", "objective": "namespace"}}]
execute if score $r namespace matches 0 run function namespace:norm_round_pack
#tellraw @a ["OUT: ", {"score": {"name": "$out", "objective": "namespace"}}]