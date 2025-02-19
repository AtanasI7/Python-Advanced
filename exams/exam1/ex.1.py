from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while challenges:
    if not tools or not substances:
        print(f"Harry is lost in the temple. Oblivion awaits him.")
        break

    cur_tool = tools.popleft()
    cur_subs = substances.pop()

    result = cur_tool * cur_subs

    if result in challenges:
        challenges.remove(result)

    else:
        tools.append(cur_tool + 1)
        cur_subs -= 1
        if cur_subs == 0:
            continue
        else:
            substances.append(cur_subs)


else:
    print(f"Harry found an ostracon, which is dated to the 6th century BCE.")


if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")

if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")