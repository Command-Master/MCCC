execute if score $l0 namespace matches 1025.. run tellraw @a {"color": "red", "text": "ERROR: trying to allocate a too-big segment"}
data modify storage namespace:main temp set from storage namespace:main alloc[{used:0}].index
execute store result score $r0 namespace run data get storage namespace:main temp
function namespace:tree/mark_used
scoreboard players operation $r0 namespace *= $1024 namespace
scoreboard players add $r0 namespace 536870912