#include <vector>
using namespace std;

class Solution
{
public:
    int singleNumber(vector<int>& nums) 
    {
        int oness = 0, twoss = 0;
        for (int num : nums) 
        {
            oness = (oness ^ num) & ~twoss;
            twoss = (twoss ^ num) & ~oness;
        }
        return oness;
    }
};
