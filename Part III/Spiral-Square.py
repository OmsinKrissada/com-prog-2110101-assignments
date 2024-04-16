# uncomment all these commented lines for a cool animation xd

# import time

direction_offset = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def spiral_square(n):
    square = [[0] * n for _ in range(n)]

    increment = 1
    current_direction = 0
    current_pos = (n // 2, n // 2)
    while increment <= n**2:
        next_direction = (current_direction + 1) % 4
        current_direction_offset = direction_offset[current_direction]
        next_direction_offset = direction_offset[next_direction]
        side_pos = (
            current_pos[0] + next_direction_offset[0],
            current_pos[1] + next_direction_offset[1],
        )
        forward_pos = (
            current_pos[0] + current_direction_offset[0],
            current_pos[1] + current_direction_offset[1],
        )

        # print()
        # print_square(square)
        # print()
        square[current_pos[0]][current_pos[1]] = increment
        if (
            forward_pos[0] == n
            or side_pos[0] == n
            or forward_pos[1] == n
            or side_pos[1] == n
            or forward_pos[0] == -1
            or side_pos[0] == -1
            or forward_pos[1] == -1
            or side_pos[1] == -1
            or square[side_pos[0]][side_pos[1]] == 0
        ):
            current_pos = side_pos
            current_direction = next_direction
        else:
            current_pos = forward_pos

        if current_pos == (n, n):
            break
        increment += 1
        # time.sleep(0.01)

    return square


def print_square(S):
    for i in range(len(S)):
        print(" ".join([(2 * " " + str(e))[-3:] for e in S[i]]))


# print_square(spiral_square(7))
exec(input().strip())
