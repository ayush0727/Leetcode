
import java.util.*;
class Solution {
    static class State {
        int row;
        int col;
        int energy;
        int mask;
        int moves;
        State(int row, int col, int energy, int mask, int moves) {
            this.row = row;
            this.col = col;
            this.energy = energy;
            this.mask = mask;
            this.moves = moves;
        }
    }
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length;
        int n = classroom[0].length();
        int startRow = 0;
        int startCol = 0;
        // Assign each litter a bit position
        int[][] litterId = new int[m][n];
        for (int[] row : litterId) {
            Arrays.fill(row, -1);
        }
        int litterCount = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char cell = classroom[i].charAt(j);
                if (cell == 'S') {
                    startRow = i;
                    startCol = j;
                } else if (cell == 'L') {
                    litterId[i][j] = litterCount++;
                }
            }
        }
        int fullMask = (1 << litterCount) - 1;
        // If no litter exists
        if (fullMask == 0) {
            return 0;
        }
        /*
         * bestEnergy[r][c][mask]
         *
         * Stores the maximum remaining energy with which
         * we have reached (r,c) after collecting "mask".
         *
         * If we come again with <= energy, that state
         * does not help us.
         */
        int[][][] bestEnergy = new int[m][n][1 << litterCount];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                Arrays.fill(bestEnergy[i][j], -1);
            }
        }
        Queue<State> queue = new ArrayDeque<>();
        queue.offer(
            new State(startRow, startCol, energy, 0, 0)
        );
        bestEnergy[startRow][startCol][0] = energy;
        int[][] directions = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };
        while (!queue.isEmpty()) {
            State current = queue.poll();
            // All litter collected
            if (current.mask == fullMask) {
                return current.moves;
            }
            // Cannot move if energy is 0
            if (current.energy == 0) {
                continue;
            }
            for (int[] dir : directions) {
                int newRow = current.row + dir[0];
                int newCol = current.col + dir[1];
                // Outside grid
                if (newRow < 0 || newRow >= m ||
                    newCol < 0 || newCol >= n) {
                    continue;
                }
                char cell = classroom[newRow].charAt(newCol);
                // Obstacle
                if (cell == 'X') {
                    continue;
                }
                // Moving costs one energy
                int newEnergy = current.energy - 1;
                // Reset energy if we reach R
                if (cell == 'R') {
                    newEnergy = energy;
                }
                int newMask = current.mask;
                // Collect litter
                if (cell == 'L') {
                    int id = litterId[newRow][newCol];
                    newMask |= (1 << id);
                }
                /*
                 * Reaching the same cell with the same litter
                 * collection status but with less/equal energy
                 * is useless.
                 */
                if (bestEnergy[newRow][newCol][newMask] >= newEnergy) {
                    continue;
                }
                bestEnergy[newRow][newCol][newMask] = newEnergy;
                queue.offer(
                    new State(
                        newRow,
                        newCol,
                        newEnergy,
                        newMask,
                        current.moves + 1
                    )
                );
            }
        }
        return -1;
    }
}