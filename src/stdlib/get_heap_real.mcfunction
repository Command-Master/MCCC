execute store result score $search1 namespace run scoreboard players operation $search2 namespace = $index namespace
scoreboard players operation $search1 namespace /= $1024 namespace
data modify storage namespace:main heap[].selected set value 0
function namespace:tree/heap_select
scoreboard players operation $search2 namespace %= $1024 namespace
function namespace:tree/heap_get