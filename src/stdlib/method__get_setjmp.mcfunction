execute store result score $r0 namespace run scoreboard players add $setjmpctr namespace 1
execute if score $setjmpctr namespace matches 1024.. run say ERROR! out of setjmp buffer space!!!
data modify storage namespace:main setjmp append value [[], []]
# first one is local stack
# second one is rec
# tellraw @a {"nbt":"rec", "storage": "namespace:main"}
data modify storage namespace:main setjmp[-1][0] set from storage namespace:main lstack
data modify storage namespace:main setjmp[-1][1] set from storage namespace:main rec
scoreboard players set $r1 namespace 0