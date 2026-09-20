#include <stdbool.h>
#include <string.h>

bool dfs(int r, int c, int pr, int pc, char target, int m, int n, char** grid, int visited[500][500])
{
    visited[r][c] = 1;

  
    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    for (int i = 0; i < 4; i++)
    {
        int nr = r + dr[i];
        int nc = c + dc[i];

     
        if (nr >= 0 && nr < m && nc >= 0 && nc < n)
        {
            if (grid[nr][nc] == target)
            {
                if (visited[nr][nc] && (nr != pr || nc != pc))
                {
                    return true;
                }
                if (!visited[nr][nc])
                {
                    if (dfs(nr, nc, r, c, target, m, n, grid, visited)) return true;
                }
            }
        }
    }
    return false;
}

bool containsCycle(char** grid, int gridSize, int* gridColSize)
{
    int m = gridSize;
    int n = gridColSize[0];
    int visited[500][500];
    
    for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++) visited[i][j] = 0;
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j])
            {

                if (dfs(i, j, -1, -1, grid[i][j], m, n, grid, visited)) return true;
            }
        }
    }
    return false;
}
