#include <iostream>
using namespace std;

typedef pair<int, int> PII;

const int N = 20, INF = 1e9;

PII p[N];
double w[N][N];
double f[1 << N][N];

double get_distance(int i, int j)
{
    int x = p[i].first - p[j].first;
    int y = p[i].second - p[j].second;
    return sqrt(x * x + y * y);
}

int main()
{
    int n, d;
    cin >> n >> d;
    for (int i = 0; i < n; i ++) cin >> p[i].first >> p[i].second;
    
    for (int i = 0; i < n; i ++)
        for (int j = i + 1; j < n; j ++)
        {
            w[i][j] = w[j][i] = get_distance(i, j);
            if(w[i][j] > d) w[i][j] = w[j][i] = INF;
        }
        
    for (int k = 0; k < n; k ++)
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < n; j ++)
                w[i][j] = min(w[i][j], w[i][k] + w[k][j]);
                
    for (int i = 0; i < 1 << n; i ++)
        for (int j = 0; j < n; j ++)
            f[i][j] = INF;
            
    f[1][0] = 0;
    for (int i = 0; i < 1 << n; i ++)
        for (int j = 0; j < n; j ++)
            if(i >> j & 1)
                for (int k = 0; k < n; k ++)
                    if((i - (1 << j)) >> k & 1)
                        f[i][j] = min(f[i][j], f[i - (1 << j)][k] + w[k][j]);
                        
    double ans = INF;
    for (int i = 1; i < n; i ++)
        ans = min(ans, f[(1 << n) - 1][i] + w[i][0]);
        
    printf("%.2f", round(ans * 100) / 100);
    return 0;
}
