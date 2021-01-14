scoreboard players set $count namespace 0
execute if score $a namespace matches ..65535 run scoreboard players set $count namespace 16
execute if score $a namespace matches ..65535 run scoreboard players operation $a namespace *= $65536 namespace
execute if score $a namespace matches ..16777215 run scoreboard players add $count namespace 8
execute if score $a namespace matches ..16777215 run scoreboard players operation $a namespace *= $256 namespace
#tellraw @a {"score": {"name": "$a", "objective": "namespace"}}

# this is bit magic:
execute store result score $signn namespace if score $a namespace matches ..-1
execute if score $signn namespace matches 1 run scoreboard players operation $a namespace += $-inf namespace
scoreboard players operation $a namespace /= $16777216 namespace
execute if score $signn namespace matches 1 run scoreboard players add $a namespace 128
# bit magic end

#tellraw @a {"score": {"name": "$a", "objective": "namespace"}}

function namespace:tree/count_leading_zeros_8