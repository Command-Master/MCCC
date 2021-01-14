#tellraw @a [{"score": {"name": "$sig", "objective": "namespace"}}, " ", {"score": {"name": "$exp", "objective": "namespace"}}, " ", {"score": {"name": "$sign", "objective": "namespace"}}]
scoreboard players operation $a namespace = $sig namespace
function namespace:count_leading_zeros
scoreboard players remove $count namespace 1
scoreboard players operation $exp namespace -= $count namespace
scoreboard players set $r namespace 0
execute if score $count namespace matches 7.. if score $exp namespace matches ..252 run function namespace:norm_round1
execute if score $r namespace matches 0 run function namespace:norm_round2