
def generate(l, r, namespace, callback, objective, name, scale=1, score='$index'):
    # Check base case
    if r == l:
        file = open(f'{name}.mcfunction', 'w')
        file.write(callback(l))
        file.close()
        return f'{name}'
    elif r > l:
        lm = l + (r - l) // 3
        rm = l + 2 * (r - l) // 3

        # If element is present at the middle itself
        file = open(f'{name}.mcfunction', 'w')
        left = generate(l, lm, namespace, callback, objective, name+'0', scale, score)
        if left != -1:
            file.write(f'execute if score {score} {objective} matches ..{lm*scale + scale - 1} run function {namespace}:{left}\n')
        mid = generate(lm+1, rm, namespace, callback, objective, name+'1', scale, score)
        if mid != -1:
            file.write(f'execute if score {score} {objective} matches {(lm+1)*scale}..{rm*scale + scale - 1} run function {namespace}:{mid}\n')
        right = generate(rm+1, r, namespace, callback, objective, name+'2', scale, score)
        if right != -1:
            file.write(f'execute if score {score} {objective} matches {(rm+1)*scale}.. run function {namespace}:{right}')
        return f'{name}'
    else:
        return -1