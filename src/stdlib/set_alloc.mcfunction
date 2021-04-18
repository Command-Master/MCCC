execute store result score $search1 namespace run scoreboard players operation $search2 namespace = $index namespace
scoreboard players operation $search1 namespace /= $1024 namespace
scoreboard players remove $search1 namespace 524288
execute unless score $search1 namespace = $lastb namespace run data modify storage namespace:main alloc[].selected set value 0
execute unless score $search1 namespace = $lastb namespace run function namespace:tree/alloc_select
scoreboard players operation $lastb namespace = $search1 namespace
scoreboard players operation $search2 namespace %= $1024 namespace
function namespace:tree/alloc_set